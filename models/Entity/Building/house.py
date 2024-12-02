from Entity.Building.building import *
class House(Building):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'H', hp = 200, cost = 25, build_time = 25*ONE_SEC, sq_size = 2):
        global HOUSES_ARRAY_1D
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.image = HOUSES_ARRAY_1D
        self.display_choice = random.randint(0, len(HOUSES_ARRAY_1D) - 1)
    
    def display(self, current_time, screen, camera, g_width, g_height):
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
            camera.draw_box(screen, self)
            display_image(META_SPRITES_CACHE_HANDLE(camera.zoom, list_keys = [self.representation, self.display_choice]),iso_x, iso_y, screen, 0x04)
            draw_percentage_bar(screen, camera, iso_x, iso_y, self.hp, self.max_hp, self.sq_size)