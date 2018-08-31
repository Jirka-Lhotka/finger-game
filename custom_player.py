from generic_player import GenericPlayer
from test_player import test_player
from moves import Move
from game import Game

class CustomPlayer(GenericPlayer):
    def move(self):
        ### EDIT CODE HERE ###
        return Move.RIGHT_TO_LEFT
        ### END CHANGE ###

### CHANGE THE NAME
custom_player = CustomPlayer("name-of-your-bot")
### END CHANGE
