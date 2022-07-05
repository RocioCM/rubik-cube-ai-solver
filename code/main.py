from list import Tile, TilesRingList
from cube import CubeFace, RubikCube

# Test Tile
tile = Tile("coso",1)
print(tile)
print(tile.color)
print(tile.id)

# Test Tiles List
tilesList = TilesRingList("red")
print(tilesList)
tilesList.printList()

# Test colors and formatting
for j in range(3):
    for i in range(41, 48):
        print("\033["+str(i) + "m {}\033[00m" .format("  "), end="")
    print("")

# Test Cube Face
face = CubeFace("red")
print(face)
print(face.color)
print(face.piecesList)
face.piecesList.printList()

# Test cube
cube = RubikCube()
cube.enableLogs()
# print(cube.front.getPrintedRow(0))
# print(cube.front.getPrintedRow(1))
# print(cube.front.getPrintedRow(2))
cube.ui()
print(cube.getScore())

# print(cube.rotateBack())
# print(cube.rotateBack())
# print(cube.rotateFront())
# print(cube.rotateFront())
# print(cube.rotateRight())
# print(cube.rotateRight())
# print(cube.rotateLeft())
# print(cube.rotateLeft())
# print(cube.rotateDown())
# print(cube.rotateDown())
# print(cube.rotateTop())
# print(cube.rotateTop())

cube.ui()
print(cube.getScore())

# print(cube.rotateBack())
# print(cube.rotateBackReverse())
# print(cube.rotateDown())
# print(cube.rotateDownReverse())
# print(cube.rotateFront())
# print(cube.rotateFrontReverse())
# print(cube.rotateLeft())
# print(cube.rotateLeftReverse())
# print(cube.rotateRight())
# print(cube.rotateRightReverse())
# print(cube.rotateTop())
# print(cube.rotateTopReverse())

# Test cube movements.
cube.randomMix(20)
cube.ui()
print(cube.getScore())
print(cube.getHistory())


cube2 = RubikCube()
cube2.enableLogs()
cube2.ui()
movs = cube2.getRandomRotations(15)
print(movs)
cube2.applyMovements(movs)
cube2.ui()
print(cube2.getScore())
