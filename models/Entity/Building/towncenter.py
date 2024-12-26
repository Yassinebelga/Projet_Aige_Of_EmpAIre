from Entity.Building.building import *

class TownCenter(Building):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'T', hp = 1000, cost = 350, build_time = 150*ONE_SEC, sq_size = 4):
        global TOWNCENTER
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.image = TOWNCENTER