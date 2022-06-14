# Colors for the cube faces.
class Colors:
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    ORANGE = "orange"
    WHITE = "white"

    # Codes for printing color blocks in the console.
    class Print:
        red='\033[41m'
        green='\033[42m'
        orange='\033[45m'
        blue='\033[46m'
        yellow='\033[43m'
        white='\033[47m'


# Rows of a cube face.
class Rows:
    TOP = "top"
    DOWN = "down"
    RIGHT = "right"
    LEFT = "left"

    # List of tiles corresponding to each row of a face.
    class Tiles:
        top = [0, 1, 2]
        right = [2, 3, 4]
        down = [4, 5, 6]
        left = [6, 7, 0]
