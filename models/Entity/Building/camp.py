from Entity.Building.building import *
class Camp(Building):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'C', sq_size = 2, hp = 200, cost = {"gold":0,"wood":100,"food":0}, build_time = 25):
        global CAMP_ARRAY_3D

        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.image = CAMP_ARRAY_3D