from .unit import Unit

class Swordsman(Unit):
    def __init(self, position, name, team, representation, SQ_size , hp, cost,training_time,speed,attack):
        super().__init(position, name, team, representation="s", SQ_size=1, hp=40, cost={"F":50,"G":20}, training_time=20, speed=0.9, attack=4)
