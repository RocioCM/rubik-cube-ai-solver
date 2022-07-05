from cube import RubikCube
from math import ceil
import random

def formatPopulationWithFitness(population): return list(
    map(lambda individual:
        (individual.getScore(), individual), population))


def initPopulation(populationSize, randomMovementsSize):
    def Individual():
        cube = RubikCube()
        cube.randomMix(randomMovementsSize)
        return cube

    population = [Individual() for i in range(populationSize)]
    return formatPopulationWithFitness(population)


def reachedSolution(bestIndividual):
    if (bestIndividual == None):
        return False
    fitness = bestIndividual[0]
    desiredScore = RubikCube().getScore()
    if (fitness == desiredScore):
        return True
    return False


def selectParentsWithProbability(population):
    parents = []
    populationCopy = population.copy()
    maxFitness = RubikCube().getScore() # TODO: test if this works cool or increase this number.
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


def reproduce(parents, childrenNumber):
    [parent1, parent2] = parents
    children = []
    for i in range(childrenNumber // 2 + 1):
        # TODO: test this mix and children works well .
        parent1History = parent1.getHistory()
        parent2History = parent2.getHistory()
        splitIndex1 = random.randrange(len(parent1History))
        splitIndex2 = random.randrange(len(parent2History))
        child1History = parent1History[0:splitIndex1]
        child1History.extend(parent2History[splitIndex2:len(parent2History)])
        child2History = parent2History[0:splitIndex2]
        child2History.extend(parent1History[splitIndex1:len(parent1History)])
        child1 = RubikCube()
        child1.applyMovements(child1History)
        child2 = RubikCube()
        child2.applyMovements(child2History)
        children.extend([child1, child2])
    return children[0:childrenNumber]


def mutateWithProbability(individual, probability):
    randomNumber = random.random()
    if (randomNumber <= probability):
        index = random.randrange(len(individual.getHistory()))
        newValue = random.randrange(12)
        newHistory = individual.getHistory().copy()
        newHistory[index] = newValue
        newIndividual = RubikCube()
        newIndividual.applyMovements(newHistory)
        return newIndividual
    return individual


def getBestNextGeneration(parents, children, splitPercent):
    size = len(parents)
    parents.sort(key=lambda tuple: tuple[0])
    children.sort(key=lambda tuple: tuple[0])
    # Keeps the best _splitPercent_ percentage of the previous generation and the other bests from the new generation.
    keptParents = parents[size - ceil(splitPercent * size):size]
    keptChildren = children[ceil(splitPercent * size):size]
    newPopulation = keptChildren
    newPopulation.extend(keptParents)
    return newPopulation


def genetic(populationSize, maxTime, mutationProbability, splitPercent, childrenPerParents):
    initialStateMovements = 30
    populationSize = 100
    maxTime = 200
    mutationProbability = 0.05
    splitPercent = 0.1
    childrenPerParents = 2

    # 1. Create a population with n random-mixed RubikCubes.
    population = initPopulation(populationSize, initialStateMovements)
    population.sort(key=lambda tuple: tuple[0])
    time = 0
    best = None
    while (time < maxTime and not (reachedSolution(best))):
        # 1. Create the nextGeneration:
        children = []
        # 2. For reproduction, choose n random pairs.
        for i in range(populationSize // childrenPerParents):
            # 2.1 Each parent would be selected with probability proportional to their fitness.
            parents = selectParentsWithProbability(population)
            # 3. From each pair of parents, create a new pair (2) of children, not just one child.
            # 3.1 Cut them at random index x and join them both.
            newChildren = reproduce(parents, childrenPerParents)
            children.extend(newChildren)
        # 3.2. Each child has m probability of mutating a random position.
        for i in range(len(children)):
            child = children[i]
            children[i] = mutateWithProbability(child, mutationProbability)
        # 4. Calculate the fitness for each new children.
        children = formatPopulationWithFitness(children)
        # 5. Kill the worst (and keep the best from parents and children).
        population = getBestNextGeneration(population, children, splitPercent)
        # 6. Order it (more fitting, more probability to reproduce. I mean, priority queue by fitness).
        population.sort(key=lambda tuple: tuple[0])
        # 7. Of that population, keep the record of the best individual. So if the individual is fit enough (threatened=0, the loop stops, else, it will stop anyway after z iterations).
        bestOfGeneration = population[-1]  # The last item is the most fitting.
        if (time == 0 or best[0] < bestOfGeneration[0]):
            best = bestOfGeneration
        time += 1
    # 8. Return the record of the best individual you got across the whole algorithm (that is not necessary the last best, just the best across all).
    return (best[0], best[1], time)
