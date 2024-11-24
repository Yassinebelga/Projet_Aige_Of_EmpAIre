from GLOBAL_VAR import *
from Entity.entity import Entity 

class Cell:

    def __init__(self, _Y, _X, _position):

        self.Y = _Y
        self.X = _X
        self.position = _position
        self.linked_entity = None
        self.entity_representation = None



    def link_entity(self, _entity):
        self.linked_entity = _entity
    
    def unlink_entity(self, _entity):
        self.linked_entity = None

    def display(self, screen, camera):
        iso_x, iso_y = camera.convert_to_isometric_2d( self.position.x, self.position.y)
        
        display_image(GRASS_ARRAY_1D[camera.zoom], iso_x, iso_y, screen, 0x04)