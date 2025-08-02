from actions import *

class Character:
    def __init__(self, name, health, defense, mana, stamina, **kwargs):
        self.name: str = name
        self.health: float = health | 100
        self.defense: float = defense | 100
        self.mana: float = mana | 100
        self.stamina: float = stamina | 100
        self.attacks: dict = {}  # Initialize as empty dictionary
        self.armor: dict = {}    # Initialize as empty dictionary
        self.weapons: dict = {}  # Initialize as empty dictionary

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Health: {self.health}\n"
                f"Defense: {self.defense}\n"
                f"Mana: {self.mana}\n"
                f"Stamina: {self.stamina}")

    def create_attack(self, name: str, damage: float, mana_cost: float = 0, stamina_cost: float = 0):
        """Create a new attack and add it to the character's attacks dictionary.
        
        Args:
            name: Name of the attack
            damage: Amount of damage the attack does
            mana_cost: Amount of mana required to use the attack (default 0)
            stamina_cost: Amount of stamina required to use the attack (default 0)
        """
        self.attacks[name] = {
            'damage': damage,
            'mana_cost': mana_cost,
            'stamina_cost': stamina_cost
        }
        return self.attacks[name]


class Player(Character):
    def __init__(self, score, lives, **kwargs):
        super().__init__(**kwargs)
        self.score = score
        self.lives = lives

    def __str__(self):
        base = super().__str__()
        return f"{base}\nScore: {self.score}\nLives: {self.lives}\n"