import random
from consts import Colors, Rows
from list import TilesRingList

class CubeFace:
    color = None
    piecesList = None

    # Create a cube face of a given color.
    def __init__(self, color):
        self.color = color
        self.piecesList = TilesRingList(color)

    # Print one horizontal row of the cube face.
    def getPrintedRow(self, index):
        tile = lambda id: " "+id+"|"
        out = ""
        if (index == 0):
            for i in range(3):
                out += getattr(Colors.Print, self.piecesList.array[i].color) + tile(self.piecesList.array[i].id)
        elif (index == 1): 
            firstPiece = getattr(Colors.Print, self.piecesList.array[7].color) + tile(self.piecesList.array[7].id) 
            secondPiece = getattr(Colors.Print, self.color) + tile("8")
            thirdPiece = getattr(Colors.Print, self.piecesList.array[3].color) + tile(self.piecesList.array[3].id)
            out = firstPiece + secondPiece + thirdPiece
        elif (index == 2):
            for i in [6, 5, 4]:
                out += getattr(Colors.Print, self.piecesList.array[i].color) + tile(self.piecesList.array[i].id)
        return out + '\033[0m'

# Rubik Cube with faces (attributes) and rotation movements (methods).
class RubikCube:
    front = None
    back = None
    right = None
    left = None
    top = None
    down = None
    history = None
    logs = False

    def __init__(self):
        self.front = CubeFace(Colors.BLUE)
        self.back = CubeFace(Colors.GREEN)
        self.right = CubeFace(Colors.ORANGE)
        self.left = CubeFace(Colors.RED)
        self.top = CubeFace(Colors.YELLOW)
        self.down = CubeFace(Colors.WHITE)
        self.history = []
        self.maxScore = self.getScore()

    def getHistory(self):
        return self.history

    def enableLogs(self):
        self.logs = True
        
    # Display the state of the cube: UI, history of movements and current score.
    def print(self):
        self.ui()
        print("HISTORY:", self.history)
        score = self.getScore()
        print("SCORE:", score, "of", self.maxScore, "(" + str(100*score/self.maxScore) + "%)")

    # Print the cube in 2D the terminal.
    def ui(self):
        emptyRow = lambda n: n*"          "

        for i in range(3):
            print(emptyRow(1), end="")
            print(self.top.getPrintedRow(i), end="")
            print(emptyRow(2), end="")
            print("")

        for i in range(3):
            print(" "+self.left.getPrintedRow(i), end="")
            print(self.front.getPrintedRow(i), end="")
            print(self.right.getPrintedRow(i), end="")
            print(self.back.getPrintedRow(i), end="")
            print("")
        
        for i in range(3):
            print(emptyRow(1), end="")
            print(self.down.getPrintedRow(i), end="")
            print(emptyRow(2), end="")
            print("")

    @staticmethod
    # Get n random numbers between 0 and 11.
    def getRandomRotations(count):
        movements = []
        for i in range(count):
            randomNum = random.randrange(0, 12)
            movements.append(randomNum)
        return movements

    # Apply a series of rotations to the cube.
    def applyMovements(self, movementsToApply):
        moves = [
            self.rotateBack,
            self.rotateBackReverse,
            self.rotateDown,
            self.rotateDownReverse,
            self.rotateFront,
            self.rotateFrontReverse,
            self.rotateLeft,
            self.rotateLeftReverse,
            self.rotateRight,
            self.rotateRightReverse,
            self.rotateTop,
            self.rotateTopReverse
        ]
        for num in movementsToApply:
            rotation = moves[num]
            self.history.append(num)
            log = rotation()
            if (self.logs):
                print(log)

    # Apply n random movements to the cube.
    def randomMix(self, count):
        randomMovementsList = self.getRandomRotations(count)
        self.applyMovements(randomMovementsList)

    # Get score of the current cube state.
    # The maximum (best) score is 48 when the cube is completed.
    # The minimum (worst) possible score is 0.
    def getScore(self):
        score = 0
        faces = [self.front, self.back, self.left, self.right, self.top, self.down]
        for face in faces:
            for i in range(face.piecesList.length):
                tile = face.piecesList.array[i]
                if (tile.color == face.color):
                    # Add one point if the tile is in the correct position of the correct face.
                    if (int(tile.id) == i):
                        if (int(tile.id) in [1,3,5,7]):
                            score += 1.5 #Edge score.
                        else:
                            score += 1 #Vertex score.
        return score

    # Rotate a given face and the side pieces in the side faces.
    def __rotate(self, rotatedFace, sideFaces, reverse):
        # Rotate the front face.
        for i in range(2):
            if (reverse):
                head = rotatedFace.piecesList.array.pop(0)
                rotatedFace.piecesList.array.append(head)
            else:
                tail = rotatedFace.piecesList.array.pop()
                rotatedFace.piecesList.array.insert(0, tail)

        # Rotate the side faces.
        prevFaceNodes = sideFaces[3][1].piecesList.getLine(sideFaces[3][0])
        for (row, face) in sideFaces:
            prevFaceNodes = face.piecesList.replaceLine(row, prevFaceNodes)

    def rotateFront(self):
        self.__rotate(self.front, [(Rows.DOWN, self.top), (Rows.LEFT, self.right), (Rows.TOP, self.down), (Rows.RIGHT, self.left)], False)
        return "Rotate Front"

    def rotateBack(self):
        self.__rotate(self.back, [(Rows.TOP, self.top), (Rows.LEFT, self.left), (Rows.DOWN, self.down), (Rows.RIGHT, self.right)], False)
        return "Rotate Back"
        
    def rotateRight(self):
        self.__rotate(self.right, [(Rows.RIGHT, self.top), (Rows.LEFT, self.back), (Rows.RIGHT, self.down), (Rows.RIGHT, self.front)], False)
        return "Rotate Right"
        
    def rotateLeft(self):
        self.__rotate(self.left, [(Rows.LEFT, self.top), (Rows.LEFT, self.front), (Rows.LEFT, self.down), (Rows.RIGHT, self.back)], False)
        return "Rotate Left"
        
    def rotateTop(self):
        self.__rotate(self.top, [(Rows.TOP, self.front), (Rows.TOP, self.left), (Rows.TOP, self.back), (Rows.TOP, self.right)], False)
        return "Rotate Top"
        
    def rotateDown(self):
        self.__rotate(self.down, [(Rows.DOWN, self.front), (Rows.DOWN, self.right), (Rows.DOWN, self.back), (Rows.DOWN, self.left)], False)
        return "Rotate Down"
        
    def rotateFrontReverse(self):
        self.__rotate(self.front, [(Rows.DOWN, self.top), (Rows.RIGHT, self.left), (Rows.TOP, self.down), (Rows.LEFT, self.right)], True)
        return "Rotate Front Reverse"
        
    def rotateBackReverse(self):
        self.__rotate(self.back, [(Rows.TOP, self.top), (Rows.RIGHT, self.right), (Rows.DOWN, self.down), (Rows.LEFT, self.left)], True)
        return "Rotate Back Reverse"
        
    def rotateRightReverse(self):
        self.__rotate(self.right, [(Rows.RIGHT, self.top), (Rows.RIGHT, self.front), (Rows.RIGHT, self.down), (Rows.LEFT, self.back)], True)
        return "Rotate Right Reverse"
        
    def rotateLeftReverse(self):
        self.__rotate(self.left, [(Rows.LEFT, self.top), (Rows.RIGHT, self.back), (Rows.LEFT, self.down), (Rows.LEFT, self.front)], True)
        return "Rotate Left Reverse"
        
    def rotateTopReverse(self):
        self.__rotate(self.top, [(Rows.TOP, self.front), (Rows.TOP, self.right), (Rows.TOP, self.back), (Rows.TOP, self.left)], True)
        return "Rotate Top Reverse"
        
    def rotateDownReverse(self):
        self.__rotate(self.down, [(Rows.DOWN, self.front), (Rows.DOWN, self.left), (Rows.DOWN, self.back), (Rows.DOWN, self.right)], True)
        return "Rotate Down Reverse"


class DRLCube(RubikCube):
    initialHistory = []
    prevScore = 0

    def __init__(self, movsCount):
        super().__init__()
        self.randomMix(movsCount)
        self.initialHistory = self.getHistory()
        self.history = []

    def reset(self):
        super().__init__()
        super().applyMovements(self.initialHistory)
        self.history = []

    def step(self, action):
        self.prevScore = self.getScore()
        self.applyMovements([action])
        return self.getState()

    def getState(self):
        score = self.getScore()
        return (self.toArray(), score-self.prevScore, score==self.maxScore, score)

    def toArray(self):
        cubeArray = []
        faces = [self.front, self.back, self.left, self.right, self.top, self.down]
        colors = dict()
        colors[Colors.BLUE] = 0
        colors[Colors.GREEN] = 1
        colors[Colors.RED] = 2
        colors[Colors.ORANGE] = 3
        colors[Colors.YELLOW] = 4
        colors[Colors.WHITE] = 5

        for face in faces:
            facePieces = list(
            map(lambda piece: (colors[piece.color]*10 + int(piece.id)), face.piecesList.array))
            cubeArray.extend(facePieces)
        return cubeArray

