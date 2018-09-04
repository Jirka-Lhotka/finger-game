import game_state
from generic_player import GenericPlayer, logger


class CustomPlayer(GenericPlayer):
    def __init__(self, name):
        GenericPlayer.__init__(self, name)
        self.game_table = game_state.get_transposition_table()

    def move(self):
        gs = game_state.GameState([self.get_my_left(), self.get_my_right(), self.get_opponent_left(), self.get_opponent_right()])
        logger.info(self.game_table[gs.hash])
        return self.game_table[gs.hash].best_move


### CHANGE THE NAME
perfect_player = CustomPlayer("perfektni player")
### END CHANGE
