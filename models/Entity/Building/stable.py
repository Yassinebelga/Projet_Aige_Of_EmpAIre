from Entity.Building.building import *
class Stable(Building):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'S', hp = 500, cost = 175, build_time = 50*ONE_SEC, sq_size = 3):
        global STABLE_ARRAY_2D

        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time)
        self.image = STABLE_ARRAY_2D
        self.animation_index = 0
        self.last_time_animation = pygame.time.get_ticks()

    def update_animation_frame(self,current_time):
        global ONE_SEC
        if current_time - self.last_time_animation >= (2*ONE_SEC)/len(self.image[0]):
            self.last_time_animation = current_time
            self.animation_index = (self.animation_index + 1)%len(self.image[0])

    def display(self,current_time, screen, camera, g_width, g_height):
        self.update_animation_frame(current_time)
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
            camera.draw_box(screen, self)
            display_image(self.image[camera.zoom][self.animation_index],iso_x, iso_y, screen, 0x04)
