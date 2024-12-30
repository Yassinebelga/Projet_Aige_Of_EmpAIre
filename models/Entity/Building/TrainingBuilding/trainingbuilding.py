from Entity.Building.building import *
class TrainingBuilding(Building):

    def __init__(self, cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time, trainable_units):
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.trainable_units = trainable_units