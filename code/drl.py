from cube import DRLCube

import random
import numpy as np
from keras import Sequential
from collections import deque
from keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import json
import time


class DQN:
    """ Deep Q Network """

    def __init__(self, params):
        self.action_space = params['action_space']
        self.state_space = params['state_space']
        self.epsilon = params['epsilon']
        self.gamma = params['gamma']
        self.batch_size = params['batch_size']
        self.epsilon_min = params['epsilon_min']
        self.epsilon_decay = params['epsilon_decay']
        self.learning_rate = params['learning_rate']
        self.layer_sizes = params['layer_sizes']
        self.memory = deque(maxlen=2500)
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        for i in range(len(self.layer_sizes)):
            if i == 0:
                model.add(Dense(self.layer_sizes[i], input_shape=(
                    self.state_space,), activation='relu'))
            else:
                model.add(Dense(self.layer_sizes[i], activation='relu'))
        model.add(Dense(self.action_space, activation='softmax'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_space)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self):
        if len(self.memory) < self.batch_size:
            return

        minibatch = random.sample(self.memory, self.batch_size)
        states = np.array([i[0] for i in minibatch])
        actions = np.array([i[1] for i in minibatch])
        rewards = np.array([i[2] for i in minibatch])
        next_states = np.array([i[3] for i in minibatch])
        dones = np.array([i[4] for i in minibatch])

        states = np.squeeze(states)
        next_states = np.squeeze(next_states)

        targets = rewards + self.gamma * \
            (np.amax(self.model.predict_on_batch(next_states), axis=1))*(1-dones)
        targets_full = self.model.predict_on_batch(states)

        ind = np.array([i for i in range(self.batch_size)])
        targets_full[[ind], [actions]] = targets

        self.model.fit(states, targets_full, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay


class DataCollected:
    def __init__(self, episode, reward, time):
        self.episode = episode
        self.reward = reward
        self.time = time

    def __str__(self) -> str:
        res = 'Ep : '+str(self.episode)+' | '+str(self.reward) + \
            ' puntos en '+str(self.time)+' seg.'
        return res


def train_dqn(episodes, env, params):
    rewards_per_episode = list()
    sum_of_rewards = []
    agent = DQN(params)
    for e in range(episodes):
        # This is one episode:
        print("EPISODE", e)
        start = time.time()
        score_episode = 0
        env.reset()
        state = env.getState()
        state = np.reshape(state[0], (1, params["state_space"]))
        score = 0
        max_movs = 400
        for mov in range(max_movs):
            # This is one movement/rotation:
            action = agent.act(state)
            # print(action)
            prev_state = state
            (next_state, reward, done, new_score_episode) = env.step(action)
            score += reward
            next_state = np.reshape(next_state, (1, params["state_space"]))
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if params['batch_size'] > 1:
                agent.replay()
            if done:
                print(f'final state before win: {str(prev_state)}')
                print(f'episode: {e+1}/{episodes}, score: {score}')
                break
            else:
                score_episode = new_score_episode
        print(env.print())

        sum_of_rewards.append(score)
        end = time.time()
        dc = DataCollected(e, score_episode, end-start)
        rewards_per_episode.append(dc)
    return (sum_of_rewards, rewards_per_episode)


if __name__ == '__main__':

    params = dict()
    params['name'] = None
    params['epsilon'] = 1
    params['gamma'] = .95
    params['batch_size'] = 500
    params['epsilon_min'] = .01
    params['epsilon_decay'] = .995
    params['learning_rate'] = 0.00025
    params['layer_sizes'] = [128, 128, 128]
    params['action_space'] = 12
    params['state_space'] = 48
    episodes = 600
    results = dict()

    env = DRLCube(30)
    env.print()
    (sum_of_rewards, export) = train_dqn(episodes, env, params)

    #--- DISPLAY RESULTS ---#
    data_dump = dict()
    for i in range(episodes):
        data_dump[i] = export[i].__dict__
    out_file = open("./output_drl.json", "w")

    json.dump(data_dump, out_file, indent=2)

    out_file.close()
