from Entity.entity import *
class Resources(Entity):

    def __init__(self, cell_X, cell_Y, position, representation, storage_capacity, team = 0):
        super().__init__(cell_X, cell_Y, position, team, representation)
        self.storage = storage_capacity 
        self.display_choice = 0
    def display(self, current_time, screen, camera):
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        #if (camera.check_in_point_of_view(iso_x, iso_y)):
        display_image(self.image[camera.zoom][self.display_choice], iso_x, iso_y, screen, 0x04)
