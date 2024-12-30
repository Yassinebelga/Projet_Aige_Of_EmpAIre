from Entity.Unit.MeleeUnit.meleeunit import *
class Villager(MeleeUnit):

    def __init__(self, cell_Y, cell_X, position, team, representation = 'v', hp = 25, cost = 50, training_time = 25*ONE_SEC, speed = 0.8, attack = 2, attack_speed= 1.4):
        super().__init__(cell_Y, cell_X, position, team, representation, hp, cost, training_time, speed, attack, attack_speed)
        self.image = VILLAGER_ARRAY_3D
        self.animation_speed = [60, 30, 60/self.attack_speed, 30, 60]