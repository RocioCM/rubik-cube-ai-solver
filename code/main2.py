from cube import RubikCube
from genetic import GeneticAlgorithm

print("MAX: ", RubikCube().getScore())

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
print(coso.result[1].ui())
print(coso.result[1].getHistory())


print("MAX: ", RubikCube().getScore())
print("PERCENT: ", coso.result[0]/RubikCube().getScore())

# cube2 = RubikCube()
# cube2.logs = True
# cube2.applyMovements([0, 1, 1, 2, 8, 6, 5, 9, 11, 11, 6, 8, 10, 7, 9, 0, 8, 8, 9, 6, 3, 2, 8, 11, 6, 0, 5, 9, 8, 11])
# cube2.ui()
# print(cube2.getHistory())
# print(cube2.getScore())