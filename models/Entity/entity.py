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

    def find_insert_position(self, entity_array):
        low_ind, high_ind = 0, len(entity_array) 
        while low_ind < high_ind:
            mid_ind = (low_ind + high_ind) // 2
            # Compare based on y, then x
            if (entity_array[mid_ind].position.y <= self.position.y and entity_array[mid_ind].position.x <  self.position.x):
                low_ind = mid_ind + 1
            else:
                high_ind = mid_ind
        return low_ind
    
    def __str__(self):
        return f"ent<{self.representation}>"