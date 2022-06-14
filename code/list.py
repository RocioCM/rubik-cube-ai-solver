from consts import Rows

# Single tile of a cube face.
class Tile:
    color = None
    id = None

    # Create node of a given color.
    def __init__(self, color, i):
        self.color = color
        self.id = str(i)


# List of the mobile pieces of a cube face.
class TilesRingList: 
    head = None
    array = None
    length = 0

    def __init__(self, color):
        self.array = []
        # Create the 8 mobile pieces of the face and push it to the array.
        for i in range(8):
            self.array.append(Tile(color, i))
            self.length += 1

    # Return given row of the face.
    def getLine(self, rowName):
        tiles = getattr(Rows.Tiles, rowName)

        nodes = []
        for i in tiles:
            nodes.append(self.array[i])
        return nodes

    # Replace given row of the face with a new one and return the old one.
    def replaceLine(self, rowName, newLine):
        tiles = getattr(Rows.Tiles, rowName)
        oldNodes = []
        for i in tiles:
            oldNodes.append(self.array[i])
            self.array[i] = newLine.pop(0)
        return oldNodes

    def printList(self):
        print("List: [ ", end="")
        for node in self.array:
            print(node.color, node.id, end=", ")
        print("]")

