from Entity.Building.building import *
class Farm(Building):

    def __init__(self,cell_Y, cell_X, position, team,representation = 'F', sq_size = 2, hp = 100, cost = {"gold":0,"wood":175,"food":0}, build_time = 50):
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time, walkable = True)
        self.image = FARM_ARRAY_3D