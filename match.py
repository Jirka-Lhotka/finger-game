from game import Game
from perfect_player import perfect_player
from random_player import test_player
from custom_player_blue import custom_player_blue

player_a = first_player = perfect_player
player_b = second_player = custom_player_blue
game = Game(player_a, player_b)
result = {
    player_a.name: 0,
    player_b.name: 0,
    "ties": 0
}

for i in range(0, 1000):
    print("===== GAME {} =====".format(i))
    winner = game.play(first_player=first_player, second_player=second_player)
    print("\n")
    if winner is None:
        result["ties"] += 1
        first_player, second_player = second_player, first_player
        continue
    result[winner.name] = result[winner.name] + 1
    first_player, second_player = second_player, first_player

print("\n")
print("THE RESULT ARE:")
print(result)
print("")
