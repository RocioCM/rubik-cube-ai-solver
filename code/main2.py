from cube import RubikCube
from genetic import GeneticAlgorithm
import copy
import time

pList = [
    [20, 150, 0.05, 0, 2],
    [20, 250, 0.5, 0.2, 2],
    [30, 250, 0.5, 0.2, 4],
    [30, 150, 0.05, 0.2, 2],
    [30, 150, 0.2, 0.2, 4],
    [20, 300, 0.5, 0.4, 4],
    [30, 250, 0.5, 0.2, 2]
]

# for j in range(30):
#     cube0 = RubikCube()
#     cube0.randomMix(30)
#     cube0.history = []

#     for params in pList:

#         # ---- GENETIC ALGORITHM ---- #

#         startTime = time.time()
#         gen = GeneticAlgorithm(cube0, *params)
#         gen.run()
#         execTime = (time.time() - startTime)

#         print(gen.result[0], ",", end="")
#     print("")


for i in range(10):
    cube0 = RubikCube()
    cube0.randomMix(30)
    cube0.history = []
    print("---")

    # ---- RANDOM ALGORITHM ---- #

    acc = 0
    maxScore = 0
    gen = GeneticAlgorithm(RubikCube())
    it = gen.maxTime * gen.populationSize
    best = None

    startTime = time.time()
    for i in range(it):
        cube = copy.deepcopy(cube0)
        cube.randomMix(20)
        score = cube.getScore()
        acc += score
        if (score > maxScore):
            best = cube
            maxScore = score
    execTime = (time.time() - startTime)

    print(len(best.getHistory()))
    print(maxScore)
    print(execTime)
    print("--")

    # ---- GENETIC ALGORITHM ---- #

    startTime = time.time()
    gen = GeneticAlgorithm(cube0, *pList[6])
    gen.run()
    execTime = (time.time() - startTime)

    print(len(gen.result[1].getHistory()))
    print(gen.result[0])
    print(execTime)
