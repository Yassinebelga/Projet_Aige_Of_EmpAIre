from Entity.Building.building import *

class TownCenter(Building):

    def __init__(self, cell_Y, cell_X, position, team, representation = 'T', sq_size = 4, hp = 1000, cost = 350, build_time = 150):
        global TOWNCENTER_ARRAY_3D
        super().__init__(cell_Y, cell_X, position, team, representation, sq_size, hp, cost, build_time)
        self.image = TOWNCENTER_ARRAY_3D