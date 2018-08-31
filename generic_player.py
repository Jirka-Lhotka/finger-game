import logging

logger = logging.getLogger("player")
logger.setLevel("INFO")

class GenericPlayer:
    def __init__(self, name):
        self.name = name
        self._my_left_hand = 1
        self._my_right_hand = 1
        self._opponent_right_hand = 1
        self._opponent_left_hand = 1
        self._history = []
        self._current_round = 0
        self._starting_player = None
    
    def __eq__(self, player_a):
        return self.name == player_a.name
    
    def move(self):
        raise Exception("Not implemented.")
    
    def apply_opponent_move(self, right=0, left=0, switch=False):
        if switch:
            logger.debug("Player {} is SWITCHing hands.".format(self.name))
            self._my_left_hand, self._my_right_hand = left, right
            return None
        if right > 0:
            logger.debug("Player {} if increasing RIGHT hand by {}.".format(self.name, right))
            self._my_right_hand += right
            if self._my_right_hand >= 5:
                self._my_right_hand = 0
        if left > 0:
            logger.debug("Player {} if increasing LEFT hand by {}.".format(self.name, left))
            self._my_left_hand += left
            if self._my_left_hand >= 5:
                self._my_left_hand = 0
    
    def is_empty(self):
        return self._my_left_hand == 0 and self._my_right_hand == 0
    
    def store_move(self, move):
        self._current_round += 1
        self._history.append(move)
    
    def get_my_right(self):
        return self._my_right_hand
    
    def get_my_left(self):
        return self._my_left_hand
    
    def get_opponent_right(self):
        return self._opponent_right_hand
    
    def get_opponent_left(self):
        return self._opponent_left_hand
    
    def get_history(self):
        return self._history
    
    def get_current_round(self):
        return self._current_round
    
    def get_starting_player(self):
        return self._starting_player
    