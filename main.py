from classes.characters import *

# Create a character
player = Player(name="Hero", health=100, defense=80, mana=100, stamina=100, score=0, lives=3)

# Create some attacks
player.create_attack("Slash", damage=20, stamina_cost=10)
player.create_attack("Fireball", damage=50, mana_cost=30)

# Print character info
print(player)
print("\nAttacks:", player.attacks)
