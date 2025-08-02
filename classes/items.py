class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Potion(Item):
    def __init__(self, name, description, healing_amount, player):
        super().__init__(name, description)
        self.healing_amount = healing_amount
        self.player = player
