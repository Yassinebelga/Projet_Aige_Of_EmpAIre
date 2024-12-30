from Entity.Building.TrainingBuilding.trainingbuilding import *
class Stable(TrainingBuilding):

    def __init__(self, cell_Y, cell_X, position, team,representation = 'S', sq_size = 3, hp = 500, cost = 175, build_time = 50, trainable_units = ['h']):
        global STABLE_ARRAY_1D

        super().__init__(cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time, trainable_units)
        self.image = STABLE_ARRAY_1D
        self.animation_frame= 0
        self.last_time_animation = pygame.time.get_ticks()

    def update_animation_frame(self,current_time):
        global ONE_SEC
        if current_time - self.last_time_animation >= (2*ONE_SEC)/len(self.image):
            self.last_time_animation = current_time
            self.animation_frame = (self.animation_frame + 1)%len(self.image)

    def display(self,current_time, screen, camera, g_width, g_height):
        self.update_animation_frame(current_time)
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
            camera.draw_box(screen, self)
            display_image(META_SPRITES_CACHE_HANDLE(camera.zoom, list_keys = [self.representation, self.animation_frame],camera = camera),iso_x, iso_y, screen, 0x04)
            draw_percentage_bar(screen, camera, iso_x, iso_y, self.hp, self.max_hp, self.sq_size, self.team)
