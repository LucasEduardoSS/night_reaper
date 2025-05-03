from classes.characters import *

player1 = Player(
    name = "Player 1",
    health = 100,
    defense = 100,
    mana = 100,
    stamina = 100,
    score = 0,
    lives = 3
)

print(player1)
player1.create_attack()
