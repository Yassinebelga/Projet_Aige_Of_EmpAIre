from Entity.Building.building import *
class Keep(Building):
    def __init__(self, cell_Y, cell_X, position, team,representation = 'K', hp = 800, cost = 35, build_time = 80*ONE_SEC, sq_size = 1):
        global KEEP_ARRAY_1D 
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.image = KEEP_ARRAY_1D