from .unit import Unit

class Swordsman(Unit):
    def __init(self, position, team, name = "Swordsman", representation="s", SQ_size=1, hp=40, cost={"F":50,"G":20}, training_time=20, speed=0.9, attack=4):
        super().__init(position, team, name, representation, SQ_size, hp, cost, training_time, speed, attack)
