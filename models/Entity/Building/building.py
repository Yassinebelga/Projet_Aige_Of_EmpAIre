from Entity.entity import * 
class Building(Entity):

    def __init__(self, cell_Y, cell_X, position, team,representation, sq_size, hp, cost, build_time, walkable = False):
        super().__init__(cell_Y, cell_X, position, team, representation, sq_size)
        self.hp = hp
        self.max_hp = hp
        self.cost = cost
        self.build_time = build_time
        self.walkable = walkable
        self.linked_map = None

    def display(self,current_time, screen, camera, g_width, g_height):

        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
            camera.draw_box(screen, self)
            display_image(META_SPRITES_CACHE_HANDLE(camera.zoom, list_keys = [self.representation], camera = camera),iso_x, iso_y, screen, 0x04, 3)
            draw_percentage_bar(screen, camera, iso_x, iso_y, self.hp, self.max_hp, self.sq_size, self.team)

    def is_dead(self):
        return self.hp <= 0
    
    