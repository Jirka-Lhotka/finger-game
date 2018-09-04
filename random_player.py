from generic_player import GenericPlayer
from moves import Move
import itertools
import random


class RandomPlayer(GenericPlayer):
    def move(self):
        print(self.get_all_moves())
        return random.choice(self.get_all_moves())

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
            if move[0] + move[1] != me['left'] + me['right'] \
                    or move[0] > 5 or move[1] > 5 \
                    or (move[0] == me['left'] and move[1] == me['right']) \
                    or (move[0] == me['right'] and move[1] == me['left']):
                return False
        return True

    def get_all_moves(self):
        all_possibilities = [Move.RIGHT_TO_RIGHT, Move.RIGHT_TO_LEFT, Move.LEFT_TO_LEFT, Move.LEFT_TO_RIGHT] + \
                            [Move.SWITCH(x[0], x[1]) for x in
                             itertools.combinations(range(self.get_my_right() + self.get_my_left()), 2)]
        return [move for move in all_possibilities if self.is_move_legal(move)]


### CHANGE THE NAME
test_player = RandomPlayer("nahodak")
### END CHANGE
