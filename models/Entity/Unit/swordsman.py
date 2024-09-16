from .Unit

class Swordsman(Unit):
    def __init__(self, type, training_time, hp, attack, speed, cost):
        super().__init__(type, training_time, hp, attack, speed, cost)
