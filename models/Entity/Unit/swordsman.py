from .unit import Unit

class Swordsman(Unit):
    def __init(self, position, hp, name, representation, SQ_size, player, cost, training_time, speed, attack):
        super().__init(position, player, name,hp=40, representation="s", SQ_size=1, cost={"F":50,"G":20}, training_time=20, speed=0.9, attack=4)
