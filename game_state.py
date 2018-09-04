import copy
import itertools

from moves import Move
from typing import List

MY_LEFT = 0
MY_RIGHT = 1
OPP_LEFT = 2
OPP_RIGHT = 3


def hash_gs(state):
    return state[0] * 5 ** 3 + state[1] * 5 ** 2 + state[2] * 5 ** 1 + state[3] * 5 ** 0


class GameState():
    def __init__(self, state):
        self.state = state
        self.best_move = None
        self.hash = hash_gs(self.state)
        self.value = -1 if (self.state[0] == 0 and self.state[1] == 0) else (
            1 if self.state[2] == 0 and self.state[3] == 0 else 0)
        self.end_state = self.value in (-1, 1)

    def __str__(self):
        return "my_left: " + str(self.state[MY_LEFT]) + " my right: " + str(self.state[MY_RIGHT]) + \
               " opp_left: " + str(self.state[OPP_LEFT]) + " opp right: " + str(self.state[OPP_RIGHT]) + \
               " value: " + str(self.value) + " best_move: " + str(self.best_move)

    def __eq__(self, other):
        return self.hash == other.hash

    def is_move_legal(self, move):
        me = (self.state[MY_LEFT], self.state[MY_RIGHT])
        opponent = (self.state[OPP_LEFT], self.state[OPP_RIGHT])
        if move == Move.LEFT_TO_RIGHT:
            if me[0] <= 0 or opponent[1] <= 0:
                return False
        elif move == Move.LEFT_TO_LEFT:
            if me[0] <= 0 or opponent[0] <= 0:
                return False
        elif move == Move.RIGHT_TO_LEFT:
            if me[1] <= 0 or opponent[0] <= 0:
                return False
        elif move == Move.RIGHT_TO_RIGHT:
            if me[1] <= 0 or opponent[1] <= 0:
                return False
        elif type(move) == tuple:
            if move[0] + move[1] != me[0] + me[1] \
                    or move[0] >= 5 or move[1] >= 5 \
                    or (move[0] == me[0] and move[1] == me[1]) \
                    or (move[0] == me[1] and move[1] == me[0]):
                return False
        return True

    def apply_move(self, move):
        a_new_state = copy.deepcopy(self.state)
        if type(move) == tuple:
            a_new_state[MY_LEFT], a_new_state[MY_RIGHT] = move[0], move[1]
        elif move == Move.RIGHT_TO_LEFT:
            a_new_state[OPP_LEFT] += a_new_state[MY_RIGHT]
        elif move == Move.RIGHT_TO_RIGHT:
            a_new_state[OPP_RIGHT] += a_new_state[MY_RIGHT]
        elif move == Move.LEFT_TO_RIGHT:
            a_new_state[OPP_RIGHT] += a_new_state[MY_LEFT]
        elif move == Move.LEFT_TO_LEFT:
            a_new_state[OPP_LEFT] += a_new_state[MY_LEFT]
        else:
            raise Exception("Illegal move in apply move.")
        a_new_state = [x if x < 5 else 0 for x in a_new_state]
        a_new_state = [a_new_state[OPP_LEFT], a_new_state[OPP_RIGHT], a_new_state[MY_LEFT], a_new_state[MY_RIGHT]]
        return GameState(a_new_state)

    def generate_moves(self):
        all_possibilities = [Move.RIGHT_TO_RIGHT, Move.RIGHT_TO_LEFT, Move.LEFT_TO_LEFT, Move.LEFT_TO_RIGHT] + \
                            [Move.SWITCH(*x) for x in
                             itertools.product(range(self.state[MY_LEFT] + self.state[MY_RIGHT]), repeat=2)
                             if sum(x) == self.state[MY_LEFT] + self.state[MY_RIGHT]]
        return [move for move in all_possibilities if self.is_move_legal(move)]

    def generate_new_boards(self):
        to_return = []
        for move in self.generate_moves():
            new_board = self.apply_move(move)
            if (move, new_board) not in to_return:
                to_return.append((move, new_board))
        return to_return


def populate_table() -> List[GameState]:
    all_states = [None] * 625
    for x1 in range(5):
        for x2 in range(5):
            for x3 in range(5):
                for x4 in range(5):
                    gs = GameState([x1, x2, x3, x4])
                    if all_states[gs.hash] is not None:
                        print("Collision!!!")
                        print("Currently there: ", all_states[gs.hash])
                        print("Trying to insert: ", gs)
                        print("hash: ", gs.hash)
                        raise Exception("Hashes collide.")
                    else:
                        all_states[gs.hash] = gs
    return all_states


def check_states_list_full(states_list):
    for i, state in enumerate(states_list):
        if state is None:
            raise Exception("None state at index ", i)


def check_states_have_best_moves(states_list):
    for a_state in states_list:
        if a_state.best_move is None and not a_state.end_state:
            raise Exception("No best move found for a non-end state")


def get_transposition_table():
    all_states = populate_table()
    check_states_list_full(all_states)

    changes = 1
    i = 0
    while changes > 0:
        i += 1
        if i != 1:
            print("Changes: ", changes)
        print("Updating table for the {0}th time".format(i))
        changes = 0
        for state in all_states:
            if state.end_state:
                # end state, don't change it
                continue
            else:
                candidates = [(move_candidate, all_states[new_state.hash].value * -1) for (move_candidate, new_state) in
                              state.generate_new_boards()]
                best_res = max(candidates, key=lambda x: x[1])
                if (best_res[1] != state.value and best_res[1] != state.value - 2 ** (-13)) or state.best_move is None \
                        or state.best_move != best_res[0]:
                    changes += 1
                    all_states[state.hash].best_move, all_states[state.hash].value = best_res[0], (
                        best_res[1] + 2 ** (-13) if best_res[1] < 0 else best_res[1])
                # if state.hash == hash_gs([0, 1, 1, 3]):
                    # print(state)
                    # print("Candidates: ", *candidates, sep=', ')
    check_states_list_full(all_states)
    input("The table is finished! Press enter to proceed.")
    return all_states


if __name__ == '__main__':
    ts = get_transposition_table()
