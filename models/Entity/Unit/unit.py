from Entity.entity import *

class Unit(Entity):

    def __init__(self, cell_Y, cell_X, position, team, representation, hp, cost, training_time, speed, attack, attack_speed = ONE_SEC, _range=1):
        super().__init__(cell_Y, cell_X, position, team, representation)
        self.hp = hp
        self.training_time=training_time
        self.cost=cost

        self.attack=attack
        self.attack_speed = attack_speed
        self.range= _range

        self.will_attack = False
        self.entity_target = None

        self.speed=speed
        self.last_time_moved = pygame.time.get_ticks()
        self.move_per_sec = TILE_SIZE_2D

        self.direction = 0
        self.state = UNIT_IDLE
        
        #animation attributes
        self.image = None
        self.animation_frame = 0
        self.animation_direction = 0 # direction index for display
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_speed = []  # Animation frame interval in milliseconds for each unit_state
    
    def set_target(self, entity_target):
        self.entity_target = entity_target

    def set_direction_index(self, unit_angle_mapping = UNIT_ANGLE_MAPPING):
        self.animation_direction = MAP_ANGLE_INDEX(self.direction, unit_angle_mapping) # map the animation index for the direction with repect to the sprites sheet

    def update_animation_frame(self, current_time):
        global ONE_SEC
        if current_time - self.last_animation_time > ONE_SEC/self.animation_speed[self.state]:
            self.last_animation_time = current_time

            self.animation_frame = (self.animation_frame + 1)%len(self.image[self.state][0][0]) #the length changes with respect to the state but the zoom and direction does not change the animation frame count

    def check_cell_position(self):
        distance_cell_to_unit = TILE_SIZE_2D * 10 # big enough to start the sort 
        updated_cell_X, updated_cell_Y =None, None
        current_cell_position = PVector2(self.cell_X*TILE_SIZE_2D +TILE_SIZE_2D/2, self.cell_Y*TILE_SIZE_2D +TILE_SIZE_2D/2)

        #if (self.position.abs_distance(current_cell_position) > TILE_SIZE_2D/2)

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
        if (current_time - self.last_time_moved > ONE_SEC/(self.speed*self.move_per_sec)):
            self.last_time_moved = current_time

            self.direction = self.position.alpha_angle(position)
            self.set_direction_index()

            self.position.x += math.cos(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
            self.position.y += math.sin(self.direction)*(TILE_SIZE_2D/self.move_per_sec)

            self.check_cell_position()

    def try_to_move(self,current_time,position):
        if self.state == UNIT_WALKING:
            if self.position == position:
                self.state = UNIT_IDLE
                self.animation_frame = 0
        
            if self.state == UNIT_WALKING:
                self.move_to_position(current_time, position)


    def display(self, current_time, screen, camera, g_width, g_height):
        
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        
        if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
            
            camera.draw_box(screen, self)
            self.update_animation_frame(current_time)
            display_image(self.image[self.state][camera.zoom][self.animation_direction][self.animation_frame], iso_x, iso_y, screen, 0x04)

    def check_collision_with(self, _entity):
        topleft = PVector2(self.position.x - self.box_size, self.position.y - self.box_size)
        bottomright = PVector2(self.position.x + self.box_size, self.position.y + self.box_size)

        ent_topleft = PVector2(_entity.position.x - _entity.box_size, _entity.position.y - _entity.box_size)
        ent_bottomright = PVector2(_entity.position.x + _entity.box_size, _entity.position.y + _entity.box_size )

        return (topleft>ent_topleft and topleft<ent_bottomright) or \
                (bottomright>ent_topleft and bottomright<ent_bottomright)