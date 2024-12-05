from GLOBAL_VAR import *
class Entity():
    def __init__(self, cell_Y, cell_X, position, team, representation, sq_size = 1):
        self.cell_Y = cell_Y
        self.cell_X = cell_X
        self.position = position
        self.team = team
        self.representation = representation
        self.sq_size = sq_size
        self.image = None

    
    def __str__(self):
        return f"ent<{self.representation}>"