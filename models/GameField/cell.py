from GLOBAL_VAR import *
from Entity.entity import Entity 

class Cell:

    def __init__(self, _Y, _X, _position):

        self.Y = _Y
        self.X = _X
        self.position = _position
        self.representation = "G"

    def display(self, screen, camera):
        iso_x, iso_y = camera.convert_to_isometric_2d( self.position.x, self.position.y)
        
        display_image(META_SPRITES.get(self.representation).get(ZOOM_LEVELS[camera.zoom]), iso_x, iso_y, screen, 0x04)