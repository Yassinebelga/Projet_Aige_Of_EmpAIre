from Entity.Building.building import *
class Barracks(Building):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'B', hp= 500, cost = 175, build_time = 50*ONE_SEC, sq_size = 3):
        global BARRACKS
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.image = BARRACKS
        