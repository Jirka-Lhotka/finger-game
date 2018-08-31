from game import Game
from custom_player import custom_player
from test_player import test_player

player_a = first_player = custom_player
player_b = second_player = test_player
game = Game(player_a, player_b)
result = {
    player_a.name: 0,
    player_b.name: 0,
    "ties": 0
}

for i in range(0, 100):
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
