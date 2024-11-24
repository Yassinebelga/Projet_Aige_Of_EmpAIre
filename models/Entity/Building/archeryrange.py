from Entity.Building.building import *
class ArcheryRange(Building):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'A', hp = 500, cost = 175, build_time = 50*ONE_SEC, sq_size = 3):
        global ARCHERYRANGE_1D
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.image = ARCHERYRANGE_1D