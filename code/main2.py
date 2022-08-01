from cube import RubikCube
from genetic import GeneticAlgorithm
import copy
import time

for i in range(10):
    cube0 = RubikCube()
    # cube0.enableLogs()
    cube0.randomMix(30)
    # cube0.print()
    cube0.history = []
    # cube0.logs = False
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

    # print("--RANDOM--")
    # print("Promedio:", acc/it)
    print(len(best.getHistory()))
    print(maxScore)
    print(execTime)
    print("--")

    # ---- GENETIC ALGORITHM ---- #

    startTime = time.time()
    gen = GeneticAlgorithm(cube0)
    gen.run()
    execTime = (time.time() - startTime)

    # cube.initialState.print()
    # cube.result[1].print()
    print(len(gen.result[1].getHistory()))
    print(gen.result[0])
    print(execTime)
