from cube import RubikCube
from genetic import GeneticAlgorithm
import copy
import time

cube0 = RubikCube()
cube0.enableLogs()
cube0.randomMix(30)
cube0.print()
cube0.logs = False

# ---- RANDOM ALGORITHM ---- #

acc = 0
maxScore = 0
gen = GeneticAlgorithm(RubikCube())
it = gen.maxTime * gen.populationSize
results = []

startTime = time.time()
for i in range(it):
    cube = copy.deepcopy(cube0)
    cube.randomMix(20)
    score = cube.getScore()
    results.append(score)
    acc += score
    if (score > maxScore):
        maxScore = score
execTime = (time.time() - startTime)

print("--RANDOM--")
print("Promedio:", acc/it)
print("SCORE:", maxScore)
print("Random time:", execTime)
print("---------")


# ---- GENETIC ALGORITHM ---- #

startTime = time.time()
cube = GeneticAlgorithm(cube0)
cube.run()
execTime = (time.time() - startTime)

cube.initialState.print()
print(cube.result)
cube.result[1].print()
print("Genetic time:", execTime)
