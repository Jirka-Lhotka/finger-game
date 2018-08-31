from generic_player import GenericPlayer
from test_player import test_player
from moves import Move
from game import Game

class CustomPlayer(GenericPlayer):
    def move(self):
        print(self.get_history())
        return Move.RIGHT_TO_LEFT

### CHANGE THE NAME
custom_player = CustomPlayer("black")
### END CHANGE
