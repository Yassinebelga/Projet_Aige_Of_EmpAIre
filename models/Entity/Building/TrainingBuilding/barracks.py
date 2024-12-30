from Entity.Building.TrainingBuilding.trainingbuilding import *
class Barracks(TrainingBuilding):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'B', sq_size = 3, hp = 500, cost = 175, build_time = 50*ONE_SEC, trainable_units = ['s']):
        global BARRACKS
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time, trainable_units)
        self.image = BARRACKS
        