import random
import logging
from moves import Move

GAME_LIMIT = 1000

logging.basicConfig()
logger = logging.getLogger("game")
logger.setLevel("DEBUG")

class Game():
    def __init__(self, player_a, player_b):
        self.player_a = player_a
        self.player_b = player_b
        self.current_round = 0
    
    def first_player(self):
        if random.random() > 0.5:
            logger.info("First player is: {}".format(self.player_a.name))
            self.player_a._starting_player = self.player_b._starting_player = self.player_a.name
            return self.player_a, self.player_b
        self.player_a._starting_player = self.player_b._starting_player = self.player_b.name
        logger.info("First player is: {}".format(self.player_b.name))
        return self.player_b, self.player_a
    
    def validate_move(self, current_player, next_player, move):
        if move == Move.LEFT_TO_RIGHT:
            if current_player.get_my_left() <= 0:
                raise Exception("Player {} played with LEFT which has {} fingers.".format(current_player.name, current_player.get_my_left()))
            if next_player.get_my_right() <= 0:
                raise Exception("Player {} played on opponents RIGHT hand which has {} fingers.".format(current_player.name, next_player.get_my_right()))
        elif move == Move.LEFT_TO_LEFT:
            if current_player.get_my_left() <= 0:
                raise Exception("Player {} played with LEFT which has {} fingers.".format(current_player.name, current_player.get_my_left()))
            if next_player.get_my_left() <= 0:
                raise Exception("Player {} played on opponents LEFT hand which has {} fingers.".format(current_player.name, next_player.get_my_left()))
        elif move == Move.RIGHT_TO_LEFT:
            if current_player.get_my_right() <= 0:
                raise Exception("Player {} played with RIGHT which has {} fingers.".format(current_player.name, current_player.get_my_right()))
            if next_player.get_my_left() <= 0:
                raise Exception("Player {} played on opponents LEFT hand which has {} fingers.".format(current_player.name, next_player.get_my_left()))
        elif move == Move.RIGHT_TO_RIGHT:
            if current_player.get_my_right() <= 0:
                raise Exception("Player {} played with RIGHT which has {} fingers.".format(current_player.name, current_player.get_my_right()))
            if next_player.get_my_right() <= 0:
                raise Exception("Player {} played on opponents RIGHT hand which has {} fingers.".format(current_player.name, next_player.get_my_right()))
        elif type(move) == tuple:
            if move[0] + move[1] != current_player.get_my_left() + current_player.get_my_right():
                raise Exception("Player {} wants to switch hands to {} {} which does not equal current status of {} {} fingers.".format(current_player.name, move[0], move[1], current_player.get_my_left(), current_player.get_my_right()))
            elif move[0] > 5 or move[1] > 5:
                raise Exception("Player {} wants to switch hands to {} {} where one hand has more than 5 fingers.".format(current_player.name, current_player.get_my_left(), current_player.get_my_right()))
            elif move[0] == current_player.get_my_left() and move[1] == current_player.get_my_right():
                raise Exception("Player {} wants to switch hands to {} {} which is the same as current status of {} {} fingers.".format(current_player.name, move[0], move[1], current_player.get_my_left(), current_player.get_my_right()))
            elif move[0] == current_player.get_my_right() and move[1] == current_player.get_my_left():
                raise Exception("Player {} wants to switch hands to {} {} which is just reflection of current status of {} {} fingers.".format(current_player.name, move[0], move[1], current_player.get_my_left(), current_player.get_my_right()))

    def play(self, first_player=None, second_player=None):
        self.current_round = 0
        logger.info("Starting game: {} vs {}".format(self.player_a.name, self.player_b.name))
        if first_player is not None and second_player is not None:
            current_player, next_player = first_player, second_player
        else:
            current_player, next_player = self.first_player()
        while not self.player_a.is_empty() and not self.player_b.is_empty() and self.current_round < GAME_LIMIT:
            logger.info("Current player: {}".format(current_player.name))
            move = current_player.move()
            logger.info("Player {} plays {}".format(current_player.name, "SWITCH {} {}".format(move[0], move[1]) if type(move) == tuple else move.value))
            try:
                self.validate_move(current_player, next_player, move)
            except Exception as e:
                logger.error(e)
                logger.info("Player {} has made an incorrect move.".format(current_player.name))
                logger.info("Winner is {}".format(next_player.name))
                return next_player
            self.player_a.store_move(move)
            self.player_b.store_move(move)
            self.current_round += 1
            if move == Move.LEFT_TO_RIGHT:
                next_player.apply_opponent_move(right=current_player.get_my_left())
                current_player._opponent_left_hand, current_player._opponent_right_hand = next_player.get_my_left(), next_player.get_my_right()
            elif move == Move.LEFT_TO_LEFT:
                next_player.apply_opponent_move(left=current_player.get_my_left())
                current_player._opponent_left_hand, current_player._opponent_right_hand = next_player.get_my_left(), next_player.get_my_right()
            elif move == Move.RIGHT_TO_LEFT:
                next_player.apply_opponent_move(left=current_player.get_my_right())
                current_player._opponent_left_hand, current_player._opponent_right_hand = next_player.get_my_left(), next_player.get_my_right()
            elif move == Move.RIGHT_TO_RIGHT:
                next_player.apply_opponent_move(right=current_player.get_my_right())
                current_player._opponent_left_hand, current_player._opponent_right_hand = next_player.get_my_left(), next_player.get_my_right()
            elif type(move) == tuple:
                current_player.apply_opponent_move(switch=True, left=move[0], right=move[1])
                next_player._opponent_left_hand, next_player._opponent_right_hand = current_player.get_my_left(), current_player.get_my_right()
            logger.info("Current status for player {}: Left hand {}, Right hand {}".format(next_player.name, next_player.get_my_left(), next_player.get_my_right()))
            logger.info("Current status for player {}: Left hand {}, Right hand {}".format(current_player.name, current_player.get_my_left(), current_player.get_my_right()))
            current_player, next_player = next_player, current_player
        if self.current_round >= GAME_LIMIT:
            logger.info("It's a tie. Game has more than {} rounds.".format(GAME_LIMIT))
            return None
        logger.info("Game ended.")
        if self.player_a.is_empty():
            logger.info("Winner is {}".format(self.player_b.name))
            return self.player_b
        else:
            logger.info("Winner is {}".format(self.player_a.name))
            return self.player_a
