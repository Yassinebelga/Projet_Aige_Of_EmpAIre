from Entity.entity import * 
class Building(Entity):

    def __init__(self, cell_X, cell_Y, position, team,representation, sq_size, hp, cost, build_time, walkable = False):
        super().__init__(cell_X, cell_Y, position, team, representation, sq_size)
        self.hp = hp
        self.cost = cost
        self.build_time = build_time
        self.walkable = walkable

    def display(self,current_time, screen, camera, g_width, g_height):

        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
            camera.draw_box(screen, self)
            display_image(self.image[camera.zoom],iso_x, iso_y, screen, 0x04)