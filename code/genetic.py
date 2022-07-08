from cube import RubikCube
from math import ceil
import copy
import random

class GeneticAlgorithm:
    initialState = None
    initialHistory = None
    result = None
    time = 0
    initialStateMovements = 30
    populationSize = 150
    maxTime = 500
    mutationProbability = 0.2
    splitPercent = 0.2
    childrenPerParents = 2


    def __init__(self, initialCube):
        self.initialHistory = initialCube.getHistory()
        initialCube.history = []
        self.initialState = initialCube


    def __formatPopulationWithFitness(self, population): return list(
        map(lambda individual:
            (individual.getScore(), individual), population))


    def __initPopulation(self):
        def Individual():
            cube = copy.deepcopy(self.initialState)
            cube.randomMix(self.initialStateMovements)
            return cube

        population = [Individual() for i in range(self.populationSize)]
        return self.__formatPopulationWithFitness(population)


    def __reachedSolution(self, bestIndividual):
        if (bestIndividual == None):
            return False
        fitness = bestIndividual[0]
        desiredScore = RubikCube().getScore()
        if (fitness == desiredScore):
            return True
        return False


    def __selectParentsWithProbability(self, population):
        parents = []
        populationCopy = population.copy()
        maxFitness = RubikCube().getScore() 
        for i in range(2):
            randomNumber = random.random()
            random.shuffle(populationCopy)
            parent = None
            while (parent == None):
                individual = populationCopy.pop()
                probabilityToReproduce = individual[0] / maxFitness
                if (randomNumber <= probabilityToReproduce):
                    parent = individual
                elif ((i == 0 and len(populationCopy) == 1)
                    or (i == 1 and len(populationCopy) == 0)):
                    parent = individual  #Only if no more parents are available.
            parents.append(parent[1])
        return parents


    def __reproduce(self, parents):
        [parent1, parent2] = parents
        children = []
        childrenPairs = self.childrenPerParents // 2
        if (self.childrenPerParents // 2 != self.childrenPerParents / 2):
            childrenPairs += 1
        for i in range(childrenPairs):
            parent1History = parent1.getHistory()
            parent2History = parent2.getHistory()
            splitIndex1 = random.randrange(len(parent1History))
            splitIndex2 = random.randrange(len(parent2History))
            child1History = parent1History[0:splitIndex1]
            child1History.extend(parent2History[splitIndex2:len(parent2History)])
            child2History = parent2History[0:splitIndex2]
            child2History.extend(parent1History[splitIndex1:len(parent1History)])
            child1 = copy.deepcopy(self.initialState)
            child1.applyMovements(child1History)
            child2 = copy.deepcopy(self.initialState)
            child2.applyMovements(child2History)
            children.extend([child1, child2])
        return children[0:self.childrenPerParents]


    def __mutateWithProbability(self, individual, probability):
        randomNumber = random.random()
        if (randomNumber <= probability):
            newHistory = individual.getHistory().copy()
            for i in range(3):
                index = random.randrange(len(newHistory))
                newValue = random.randrange(12)
                newHistory[index] = newValue
            newIndividual = copy.deepcopy(self.initialState)
            newIndividual.applyMovements(newHistory)
            return newIndividual
        return individual


    def __getBestNextGeneration(self, parents, children):
        size = len(parents)
        children.sort(key=lambda tuple: tuple[0]) # Sort children by fitness. Parents are already sorted.
        # Keeps the best _splitPercent_ percentage of the previous generation and the other bests from the new generation.
        keptParents = parents[size - ceil(self.splitPercent * size):size]
        keptChildren = children[ceil(self.splitPercent * size):size]
        newPopulation = keptChildren
        newPopulation.extend(keptParents)
        return newPopulation


    def run(self):
        self.result = None
        # 1. Create a population with n random-mixed RubikCubes.
        population = self.__initPopulation()
        population.sort(key=lambda tuple: tuple[0])
        self.time = 0
        best = None

        while (self.time < self.maxTime and not (self.__reachedSolution(best))):
            # 1. Create the nextGeneration:
            children = []
            # 2. For reproduction, choose n random pairs.
            for i in range(self.populationSize // self.childrenPerParents):
                # 2.1 Each parent would be selected with probability proportional to their fitness.
                parents = self.__selectParentsWithProbability(population)
                # 3. From each pair of parents, create a new pair (2) of children, not just one child.
                # 3.1 Cut them at random index x and join them both.
                newChildren = self.__reproduce(parents)
                children.extend(newChildren)
            # 3.2. Each child has m probability of mutating a random position.
            for i in range(len(children)):
                child = children[i]
                children[i] = self.__mutateWithProbability(child, self.mutationProbability)
            # 4. Calculate the fitness for each new children.
            children = self.__formatPopulationWithFitness(children)
            # 5. Kill the worst (and keep the best from parents and children).
            population = self.__getBestNextGeneration(population, children)
            # 6. Order it (more fitting, more probability to reproduce. I mean, priority queue by fitness).
            population.sort(key=lambda tuple: tuple[0])
            # 7. Of that population, keep the record of the best individual. So if the individual is fit enough (threatened=0, the loop stops, else, it will stop anyway after z iterations).
            bestOfGeneration = population[-1]  # The last item is the most fitting.
            if (self.time == 0 or best[0] < bestOfGeneration[0]):
                best = bestOfGeneration
            self.time += 1
            print(self.time, best[0])
        # 8. Return the record of the best individual you got across the whole algorithm (that is not necessary the last best, just the best across all).
        self.result = (best[0], best[1], self.time)
        return self.result

