
class Attack:
    def __init__(self, desc, damage, piercing):
        self.desc: str = desc
        self.damage: float = damage
        self.piercing: float = piercing


class Defense:
    def __init__(self, desc, ratio, stamina_consumption):
        self.desc: str = desc
        self.ratio: float = ratio
        self.stamina_consumption: float = stamina_consumption


class Movement:
    def __init__(self, desc, velocity):
        self.desc: str = desc
        self.velocity: float = velocity


class Jump(Movement):
    def __init__(self, desc, velocity):
        super().__init__(desc, velocity)
