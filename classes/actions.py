

class Action:
    def __init__(self, desc, velocity, **kwargs):
        self.desc: str = desc
        self.velocity: float = velocity | 100.00


class Attack(Action):
    def __init__(self, damage, piercing, **kwargs):
        super().__init__(**kwargs)
        self.damage: float = damage
        self.piercing: float = piercing


class Defense(Action):
    def __init__(self, ratio, stamina_consumption, **kwargs):
        super().__init__(**kwargs)
        self.ratio: float = ratio
        self.stamina_consumption: float = stamina_consumption


class Jump(Action):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
