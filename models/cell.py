from enum import Enum

class CellType(Enum):
    GRASS = 1

CellType = Enum('CellType',['GRASS'])

class Cell:
    
    def __init__(self,_X,_Y):

        self.X = _X
        self.Y = _Y
        self.type = CellType.GRASS
        self.free = True
        self.linked_entity = None


    def is_free(self):
        return self.free
    
    def set_occupied(self):
        self.free = False

    def set_free(self):
        self.free = True
    
    def link_entity(self, _entity):
        self.linked_entity = _entity
    
    def unlink_entity(self, _entity):
        self.linked_entity = None