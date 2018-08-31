from enum import Enum

class Move(Enum):
    LEFT_TO_RIGHT = "LEFT TO RIGHT"
    LEFT_TO_LEFT = "LEFT TO LEFT"
    RIGHT_TO_RIGHT = "RIGHT TO RIGHT"
    RIGHT_TO_LEFT = "RIGHT TO LEFT"
    def SWITCH(right, left):
        return (right, left)
