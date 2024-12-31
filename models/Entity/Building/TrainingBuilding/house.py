from Entity.Building.TrainingBuilding.trainingbuilding import *
class House(TrainingBuilding):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'H', sq_size = 2, hp = 200, cost = 25, build_time = 25, trainable_units = ['v']):
        global HOUSES_ARRAY_3D
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time, trainable_units)

        self.image = HOUSES_ARRAY_3D
        self.display_choice = random.randint(0, len(HOUSES_ARRAY_3D) - 1)
    
    