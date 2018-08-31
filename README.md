## Finger game

### Introduction
This game is about writing a program that beats another program in a Finger game. You will implement a method in `CustomPlayer` class located in `src/custom_player.py`. Please, **do not** modify any other code than that identified, otherwise you will be disqualified.

### Rules of the game
1) Each player starts with 5 finger on each hand, left and right.
2) On your turn, you can choose to hit one of the opponents hand with one of your hands. The opponent's hand will decrease that many fingers with which you hit it.
3) On your turn you can also switch fingers in your hands. The sum of fingers after switching **must** equal the number of fingers on your hand currently. Given this, you can switch to any number of fingers. E.g. Current hand has 3 4 fingers, you can switch hands to 5 2, or 0 3 change to 1 2. See [exceptions](#disqualifications).
4) If opponents hand after your hit has 0 (or less) fingers, he loses that hand. Note that he may gain fingers back in the future by switching.
5) Whoever loses both hands first, loses the game.

### Disqualifications
- If a game lasts more than 5000 rounds, both players lose.
- If you perform an incorrect move, you lose. This includes:
    - Hitting oponnents hand which has 0 fingers.
    - Hitting with a hand that has 0 fingers.
    - Switching hands so that the sum after switching does not equal current sum.
    - Switching hands so that they are the same as they are now, e.g. 3 4 to 3 4, or 5 5 to 5 5.
    - Switching hands so that one of the hands has more than 5 fingers, e.g. 3 4 to 6 1.
- Returning incorrect data type in the `move` method.
- Timeout of 1 second.

### Your task
Your task is to complete the `move` method in `CustomPlayer` class. This method **must** return one of the following types:
```python
return Move.LEFT_TO_RIGHT
or
return Move.LEFT_TO_LEFT
or
return Move.RIGHT_TO_RIGHT
or
return Move.RIGHT_TO_LEFT
or
return Move.SWITCH(3, 4)
```
Returning `Move.LEFT_TO_RIGHT` means that you want to hit opponent's RIGHT hand with your LEFT.
Whereas `Move.SWITCH(3, 4)` means that you want to switch fingers to 3 on your LEFT and 4 on your RIGHT.

There are helpful methods of the `GenericPlayer` class which you can use. For example:

```python
self.get_my_left() # Returns current number of fingers on your left hand
self.get_my_right() # Returns current number of fingers on your right hand
self.get_opponent_left() # Returns current number of fingers on opponents left hand
self.get_opponent_right() # Returns current number of fingers on opponents right hand
self.get_history() # Returns and array of all the moves within the game.
self.get_current_round() # Returns the number of current round
self.get_starting_player() # Returns the name of the starting player
```

### Testing
For testing run the `match.py` script. In command line run:

```
python match.py
```

### Matches
There will be matches of each player against every other player. Each match will be 1000 rounds played. 
