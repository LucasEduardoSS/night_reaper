from actions import *

class Character:

    attacks: dict
    armor: dict
    weapons: dict

    def __init__(self, name: str, health: float, defense: float, mana: float, stamina: float, **kwargs):
        self.name = name
        self.health = health
        self.defense = defense
        self.mana = mana
        self.stamina = stamina

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Health: {self.health}\n"
                f"Defense: {self.defense}\n"
                f"Mana: {self.mana}\n"
                f"Stamina: {self.stamina}")

    def create_attack(self):
        self.attack: Attack


class Player(Character):
    def __init__(self, score, lives, **kwargs):
        super().__init__(**kwargs)
        self.score = score
        self.lives = lives

    def __str__(self):
        base = super().__str__()
        return f"{base}\nScore: {self.score}\nLives: {self.lives}\n"
