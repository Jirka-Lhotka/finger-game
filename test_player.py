from generic_player import GenericPlayer
from moves import Move

class TestPlayer(GenericPlayer):
    def move(self):
        left = self.get_my_left()
        right = self.get_my_right()
        if left == right:
            if left == 0:
                return Move.LEFT_TO_LEFT
            else:
                return Move.RIGHT_TO_LEFT
        return Move.SWITCH(right, left)
    
test_player = TestPlayer("test")
