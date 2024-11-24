from Entity.Building.building import *
class House(Building):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'H', hp = 200, cost = 25, build_time = 25*ONE_SEC, sq_size = 2):
        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.image = HOUSES_ARRAY_2D
        self.display_choice = random.randint(0, len(HOUSES_ARRAY_2D[0]) - 1)
    
    def display(self, current_time, screen, camera):
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        if (camera.check_in_point_of_view(iso_x, iso_y)):
            display_image(self.image[camera.zoom][self.display_choice],iso_x, iso_y, screen, 0x04)
