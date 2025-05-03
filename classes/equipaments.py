class Equipment:
    def __init__(self, player):
        self.player = player


class Armor(Equipment):
    def __init__(self, player):
        super().__init__(player)


class Weapon(Equipment):
    def __init__(self, player):
        super().__init__(player)
