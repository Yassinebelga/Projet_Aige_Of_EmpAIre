from Entity.entity import *
from AITools.a_star import *

class Unit(Entity):

    def __init__(self, cell_Y, cell_X, position, team, representation, hp, cost, training_time, speed, attack, attack_speed = ONE_SEC, _range=1):
        super().__init__(cell_Y, cell_X, position, team, representation)
        self.hp = hp
        self.max_hp = hp
        self.training_time=training_time
        self.cost=cost

        self.attack = attack
        self.attack_speed = attack_speed
        self.range= _range

        self.will_attack = False
        self.entity_target = None

        self.speed=speed
        self.last_time_moved = pygame.time.get_ticks()
        self.move_per_sec = TILE_SIZE_2D
        self.path_to_position = None
        self.current_to_position = None
        self.direction = 0
        self.state = UNIT_IDLE
        
        #animation attributes
        self.image = None
        self.animation_frame = 0
        self.animation_direction = 0 # direction index for display
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_speed = []  # Animation frame interval in milliseconds for each unit_state
        self.linked_map = None

    def set_target(self, entity_target):
        self.entity_target = entity_target

    def set_direction_index(self, unit_angle_mapping = UNIT_ANGLE_MAPPING):
        self.animation_direction = MAP_ANGLE_INDEX(self.direction, unit_angle_mapping) # map the animation index for the direction with repect to the sprites sheet

    def update_animation_frame(self, current_time):
        global ONE_SEC
        if current_time - self.last_animation_time > ONE_SEC/self.animation_speed[self.state]:
            self.last_animation_time = current_time

            self.animation_frame = (self.animation_frame + 1)%len(self.image.get(self.state,None).get(0, None)) #the length changes with respect to the state but the zoom and direction does not change the animation frame count
    def changed_cell_position(self):
        topleft = PVector2(self.cell_X*TILE_SIZE_2D, self.cell_Y*TILE_SIZE_2D)
        bottomright = PVector2((self.cell_X + 1)*TILE_SIZE_2D, (self.cell_Y + 1)*TILE_SIZE_2D)

        return not(self.position < bottomright and self.position > topleft)

    def track_cell_position(self):
        if (self.changed_cell_position()):
            distance_cell_to_unit = TILE_SIZE_2D * 10 # big enough to start the sort 
            updated_cell_X, updated_cell_Y =None, None
            current_cell_position = PVector2(self.cell_X*TILE_SIZE_2D +TILE_SIZE_2D/2, self.cell_Y*TILE_SIZE_2D +TILE_SIZE_2D/2)

            for offset_Y in range(-1,2):
                for offset_X in range(-1,2):
                    current_cell_X = self.cell_X + offset_X
                    current_cell_Y = self.cell_Y + offset_Y

                    current_cell_position.x = current_cell_X*TILE_SIZE_2D + TILE_SIZE_2D/2
                    current_cell_position.y = current_cell_Y*TILE_SIZE_2D + TILE_SIZE_2D/2
                    
                    current_distance = self.position.abs_distance(current_cell_position)

                    if current_distance < distance_cell_to_unit:
                        distance_cell_to_unit = current_distance
                        updated_cell_X, updated_cell_Y = current_cell_X, current_cell_Y

            self.cell_X, self.cell_Y = updated_cell_X, updated_cell_Y

    def move_to_position(self,current_time, position):
        if (current_time - self.last_time_moved > ONE_SEC/(self.move_per_sec*self.speed)):

            self.last_time_moved = current_time
            #print(self.path_to_position)

            if self.path_to_position != None and self.current_to_position == position:
                
                
                if len(self.path_to_position) <= 1:
                    
                    self.direction = self.position.alpha_angle(position)
                    self.set_direction_index()

                    amount_x = math.cos(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
                    amount_y = math.sin(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
                    
                    self.position.x += amount_x
                    self.position.y += amount_y 

                    if self.position == position:
                        self.path_to_position = None
                else:
                    """
                    for i in range(len(self.path_to_position) - 1):
                        
                        (X1, Y1) = self.path_to_position[i]
                        (X2, Y2) = self.path_to_position[i + 1]
                        
                        
                        iso_x1, iso_y1 = camera.convert_to_isometric_2d(X1 * TILE_SIZE_2D + TILE_SIZE_2D/2, Y1 * TILE_SIZE_2D + TILE_SIZE_2D/2)
                        iso_x2, iso_y2 = camera.convert_to_isometric_2d(X2 * TILE_SIZE_2D + TILE_SIZE_2D/2, Y2 * TILE_SIZE_2D + TILE_SIZE_2D/2)
                        
                        # Draw a line between these two points
                        pygame.draw.line(screen, (255, 0, 0), (iso_x1, iso_y1), (iso_x2, iso_y2), 2)
                    """
                    current_path_node_position = PVector2(self.path_to_position[0][0] * TILE_SIZE_2D + TILE_SIZE_2D/2, self.path_to_position[0][1] * TILE_SIZE_2D + TILE_SIZE_2D/2)
                    self.direction = self.position.alpha_angle(current_path_node_position)
                    self.set_direction_index()

                    amount_x = math.cos(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
                    amount_y = math.sin(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
                    
                    self.position.x += amount_x
                    self.position.y += amount_y 

                    if self.position == current_path_node_position:
                        self.path_to_position = self.path_to_position[1:]
            else:
                self.path_to_position = A_STAR(self.cell_X, self.cell_Y, math.floor(position.x/TILE_SIZE_2D), math.floor(position.y/TILE_SIZE_2D), self.linked_map)
                self.current_to_position = PVector2(position.x, position.y)
                if self.path_to_position != None:
                    self.path_to_position = self.path_to_position[1:] # we skip the tile we are on, no need to pass by the center of the unit cell
                

            self.track_cell_position()
    def try_to_move(self,current_time,position):
        if self.state == UNIT_WALKING:
            if self.position == position:
                print("STOPPED")
                self.state = UNIT_IDLE
                self.animation_frame = 0
        
            if self.state == UNIT_WALKING:
                self.move_to_position(current_time, position)
        
                


    def display(self, current_time, screen, camera, g_width, g_height):
        
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        
        if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
            
            camera.draw_box(screen, self)
            self.update_animation_frame(current_time)
            display_image(META_SPRITES_CACHE_HANDLE(camera.zoom, list_keys = [self.representation, self.state, self.animation_direction, self.animation_frame], camera = camera), iso_x, iso_y, screen, 0x04, 1)
            draw_percentage_bar(screen, camera, iso_x, iso_y, self.hp, self.max_hp, self.sq_size)

    def check_collision_with(self, new_x, new_y, _entity):
        topleft = PVector2(new_x - self.box_size, new_y - self.box_size)
        bottomright = PVector2(new_x + self.box_size, new_y + self.box_size)

        ent_topleft = PVector2(_entity.position.x - _entity.box_size, _entity.position.y - _entity.box_size)
        ent_bottomright = PVector2(_entity.position.x + _entity.box_size, _entity.position.y + _entity.box_size )

        return (topleft>ent_topleft and topleft<ent_bottomright) or \
                (bottomright>ent_topleft and bottomright<ent_bottomright)

    def check_collision_around(self):
        pass


 