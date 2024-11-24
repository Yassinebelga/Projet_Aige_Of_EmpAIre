from Entity.Unit.unit import *
class SwordMan(Unit):

    def __init__(self, cell_Y, cell_X, position, team, representation = 's', hp = 40, cost = 50, training_time = 20*ONE_SEC, speed = 0.9, attack = 4):
        super().__init__(cell_Y, cell_X, position, team, representation, hp, cost, training_time, speed, attack)
        self.image = None

