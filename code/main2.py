from cube import RubikCube
from genetic import GeneticAlgorithm

cube = RubikCube()
cube.enableLogs()
cube.randomMix(30)
cube.ui()
print(cube.getHistory())
cube.logs = False

print("---------")
coso = GeneticAlgorithm(cube)
coso.run()
print(coso.initialState)
print(coso.initialState.history)
print(coso.initialState.ui())
print(coso.initialHistory)
print(coso.result)
print(coso.time)
print(coso.initialStateMovements)
print(coso.populationSize)
print(coso.maxTime)
print(coso.mutationProbability)
print(coso.splitPercent)
print(coso.childrenPerParents)


# print(coso.run())
# cubo = coso.result[1]
# print(cubo.getHistory())
# cubo.ui()
# print("MAX: ", RubikCube().getScore())


# cube2 = RubikCube()
# cube2.logs = True
# cube2.applyMovements([0, 1, 1, 2, 8, 6, 5, 9, 11, 11, 6, 8, 10, 7, 9, 0, 8, 8, 9, 6, 3, 2, 8, 11, 6, 0, 5, 9, 8, 11])
# cube2.ui()
# print(cube2.getHistory())
# print(cube2.getScore())