from Entity.entity import *
class Resources(Entity):

    def __init__(self, cell_Y, cell_X, position, representation, storage_capacity, team = 0):
        super().__init__(cell_Y, cell_X, position, team, representation)
        self.storage = storage_capacity 
        self.max_storage = storage_capacity
        self.display_choice = 0
        self.linked_map = None

    def display(self, current_time, screen, camera, g_width, g_height):
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        camera.draw_box(screen, self)
        #if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
        display_image(META_SPRITES_CACHE_HANDLE(camera.zoom, list_keys = [self.representation, self.display_choice],camera = camera), iso_x, iso_y, screen, 0x04)
        draw_percentage_bar(screen, camera, iso_x, iso_y, self.storage, self.max_storage, self.sq_size)

    def is_dead(self):
        return self.storage <= 0