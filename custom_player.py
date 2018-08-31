from generic_player import GenericPlayer
from test_player import test_player
from moves import Move
from game import Game
import itertools

class CustomPlayer(GenericPlayer):
    def move(self):
        print(self.get_history())
        return Move.RIGHT_TO_LEFT

    def is_move_legal(self, move):
        me = {'left': self.get_my_left(), 'right': self.get_my_right()}
        opponent = {'left': self.get_opponent_left(), 'right': self.get_opponent_right()}
        if move == Move.LEFT_TO_RIGHT:
            if me['left'] <= 0 or opponent['right'] <= 0:
                return False
        elif move == Move.LEFT_TO_LEFT:
            if me['left'] <= 0 or opponent['left'] <= 0:
                return False
        elif move == Move.RIGHT_TO_LEFT:
            if me['right'] <= 0 or opponent['left'] <= 0:
                return False
        elif move == Move.RIGHT_TO_RIGHT:
            if me['right'] <= 0 or opponent['right'] <= 0:
                return False
        elif type(move) == tuple:
            if move[0] + move[1] != me['left'] + me['right']\
                    or move[0]>5 or move[1]>5\
                    or (move[0] == me['left'] and move[1] == me['right'])\
                    or (move[0] == me['right'] and move[1] == me['left']):
                return False
        return True


### CHANGE THE NAME
custom_player = CustomPlayer("black")
### END CHANGE
