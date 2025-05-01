
class Attack:
    def __init__(self, desc, damage, piercing):
        self.desc: str
        self.damage: float
        self.piercing: float


class Character:
    def __init__(self):
        self.name: str
        self.health: float
        self.defense: float
        self.mana: float
        self.stamina: float

    def create_attack(self):
        self.attack: Attack


class Player(Character):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 100
        self.defense = 0
        self.mana = 100
        self.stamina = 50
        self.score = 0
        self.lives = 3
