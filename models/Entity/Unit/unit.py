from Entity.entity import *
from AITools.a_star import *

class Unit(Entity):

    def __init__(self, cell_Y, cell_X, position, team, representation, hp, cost, training_time, speed, attack, attack_speed = 1, _range=1):
        super().__init__(cell_Y, cell_X, position, team, representation)
        self.hp = hp
        self.max_hp = hp
        self.training_time=training_time
        self.cost=cost


        
        self.attack = attack
        self.attack_speed = attack_speed
        self.range= _range
        self.last_time_attacked = pygame.time.get_ticks()
        self.will_attack = False
        self.attack_frame = 0
        self.entity_target = None
        self.check_range_with_target = False
        self.first_time_pass = True

        self.speed=speed
        self.last_time_moved = pygame.time.get_ticks()
        self.move_per_sec = TILE_SIZE_2D # 1 tile per speed of each unit ( tile size in the 2d mechanics plane)
        
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

    def set_direction_index(self):
        self.animation_direction = MAP_ANGLE_INDEX(self.direction, UNIT_ANGLE_MAPPING) # map the animation index for the direction with repect to the sprites sheet



    def len_current_animation_frames(self):
        return len(self.image.get(self.state,None).get(0, None)) #the length changes with respect to the state but the zoom and direction does not change the animation frame count
 
    def update_animation_frame(self, current_time):
        global ONE_SEC
        if current_time - self.last_animation_time > ONE_SEC/self.animation_speed[self.state]:
            self.last_animation_time = current_time

            self.animation_frame = (self.animation_frame + 1)%(self.len_current_animation_frames()) #the length changes with respect to the state but the zoom and direction does not change the animation frame count
    
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

            uself = self.linked_map.remove_entity(self) # remove from the current cell
            self.cell_X, self.cell_Y = updated_cell_X, updated_cell_Y # update the cell
            self.change_cell_on_map()

    def change_cell_on_map(self):
        region = self.linked_map.entity_matrix.get((self.cell_Y//self.linked_map.region_division, self.cell_X//self.linked_map.region_division))

        if (region):
            current_set = region.get((self.cell_Y, self.cell_X))

            if(current_set):
                current_set.add(self)
            else:
                current_set = set()
                current_set.add(self)
                region[(self.cell_Y, self.cell_X)] = current_set
        else:
            region = {}
            current_set = set()
            current_set.add(self)
            region[(self.cell_Y, self.cell_X)] = current_set

            self.linked_map.entity_matrix[(self.cell_Y//self.linked_map.region_division, self.cell_X//self.linked_map.region_division)] = region    




    def move_to_position(self,current_time, position, camera):
        if (current_time - self.last_time_moved > ONE_SEC/(self.move_per_sec*self.speed)):

            self.last_time_moved = current_time
            print(self.path_to_position)

            if self.path_to_position != None and self.current_to_position == position:
                
                if (self.check_collision_around()):
                    self.check_and_set_path(position)

                end_index = None
                end_path_X = None
                end_path_Y = None

                if self.path_to_position: # if not empty 
                    end_index = len(self.path_to_position) - 1
                    end_path_X = self.path_to_position[end_index][0]
                    end_path_Y = self.path_to_position[end_index][1]

                if self.path_to_position == [] or (self.cell_X == end_path_X and self.cell_Y == end_path_Y): # if we entered the last last cell we dont go to the center of the cell, straight to the position
                    
                    
                    self.direction = self.position.alpha_angle(position)

                    amount_x = math.cos(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
                    amount_y = math.sin(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
                    
                    self.position.x += amount_x
                    self.position.y += amount_y 

                    if self.position == position:
                        self.path_to_position = None
                else:
                    
                    # for debugging purposes
                    for i in range(len(self.path_to_position) - 1):
                        
                        (X1, Y1) = self.path_to_position[i]
                        (X2, Y2) = self.path_to_position[i + 1]
                        
                        
                        iso_x1, iso_y1 = camera.convert_to_isometric_2d(X1 * TILE_SIZE_2D + TILE_SIZE_2D/2, Y1 * TILE_SIZE_2D + TILE_SIZE_2D/2)
                        iso_x2, iso_y2 = camera.convert_to_isometric_2d(X2 * TILE_SIZE_2D + TILE_SIZE_2D/2, Y2 * TILE_SIZE_2D + TILE_SIZE_2D/2)
                        
                        # Draw a line between these two points
                        pygame.draw.line(screen, (255, 0, 0), (iso_x1, iso_y1), (iso_x2, iso_y2), 2)
                    




                    current_path_node_position = PVector2(self.path_to_position[0][0] * TILE_SIZE_2D + TILE_SIZE_2D/2, self.path_to_position[0][1] * TILE_SIZE_2D + TILE_SIZE_2D/2)
                    self.direction = self.position.alpha_angle(current_path_node_position)

                    amount_x = math.cos(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
                    amount_y = math.sin(self.direction)*(TILE_SIZE_2D/self.move_per_sec)
                    
                    self.position.x += amount_x
                    self.position.y += amount_y 

                    if self.position == current_path_node_position:
                        self.path_to_position = self.path_to_position[1:]
            else:
                self.check_and_set_path(position)

            self.track_cell_position()

    def check_and_set_path(self, position):
        self.path_to_position = A_STAR(self.cell_X, self.cell_Y, math.floor(position.x/TILE_SIZE_2D), math.floor(position.y/TILE_SIZE_2D), self.linked_map)
                
        if self.path_to_position != None:
            self.current_to_position = PVector2(position.x, position.y)
            self.path_to_position = self.path_to_position[1:] # we skip the tile we are on, no need to pass by the center of the unit cell
        else : 
            self.change_state(UNIT_IDLE)

    def try_to_move(self, current_time, position, camera):
        if self.position == position:
            self.change_state(UNIT_IDLE)
        else:
            if not(self.state == UNIT_WALKING):
                self.change_state(UNIT_WALKING)
            self.move_to_position(current_time, position, camera)

        
    def change_state(self, new_state):
        self.animation_frame = 0 
        # to avoid index out of bound in the animationframes list, 
        # for exmample for Archer 
        # idle has 60 frames, move has 30
        # the unit moves on the 58th frame
        # the state changes, now it is moving, but the frame index is 58
        # and move has max 30, 58 > 30 ==> unsupported type (Nonetype)

        self.state = new_state  


    def display(self, current_time, screen, camera, g_width, g_height):
        
        iso_x, iso_y = camera.convert_to_isometric_2d(self.position.x, self.position.y)
        
        px, py = camera.convert_to_isometric_2d(self.cell_X*TILE_SIZE_2D + TILE_SIZE_2D/2, self.cell_Y*TILE_SIZE_2D + TILE_SIZE_2D/2)
        if (camera.check_in_point_of_view(iso_x, iso_y, g_width, g_height)):
            
            camera.draw_box(screen, self)
            self.update_animation_frame(current_time)
            self.set_direction_index()
            display_image(META_SPRITES_CACHE_HANDLE(camera.zoom, list_keys = [self.representation, self.state, self.animation_direction, self.animation_frame], camera = camera), iso_x, iso_y, screen, 0x04, 1)
            draw_percentage_bar(screen, camera, iso_x, iso_y, self.hp, self.max_hp, self.sq_size, self.team)
            draw_point(screen, (0, 0, 0), px, py, radius=5)

    def check_collision_with(self, _entity):

        topleft = PVector2(self.position.x - self.box_size, self.position.y - self.box_size)
        bottomright = PVector2(self.position.x + self.box_size, self.position.y + self.box_size)
        topright = PVector2(self.position.x + self.box_size, self.position.y - self.box_size)
        bottomleft = PVector2(self.position.x - self.box_size, self.position.y + self.box_size)


        ent_topleft = PVector2(_entity.position.x - _entity.box_size, _entity.position.y - _entity.box_size)
        ent_bottomright = PVector2(_entity.position.x + _entity.box_size, _entity.position.y + _entity.box_size )

        return (topleft>ent_topleft and topleft<ent_bottomright) or \
                (bottomright>ent_topleft and bottomright<ent_bottomright) or \
                 (topright>ent_topleft and topright<ent_bottomright) or \
                  (bottomleft>ent_topleft and bottomleft<ent_bottomright) 

    def check_collision_around(self): # this function is only made to se if we need to recalculate the path for the unit
        collided = False

        for offsetY in [-1, 0, 1]:
            for offsetX in [-1, 0, 1]:

                currentY = self.cell_Y + offsetY
                currentX = self.cell_X + offsetX

                if not(self.cell_X != currentX and self.cell_Y != currentY):
                    current_region = self.linked_map.entity_matrix.get((currentY//self.linked_map.region_division, currentX//self.linked_map.region_division))

                    if (current_region):
                        current_set = current_region.get((currentY, currentX))

                        if (current_set):
                            for entity in current_set:
                                if isinstance(entity, Building) and not(entity.walkable):
                                    if (self.check_collision_with(entity)):
                                        collided = True # all we need is to get one collision with a non walkable entity
                                        break 
                                elif isinstance(entity, Resources):
                                    if (self.check_collision_with(entity)):
                                        collided = True 
                                        break
                if (collided):
                    break
            if (collided):
                break
        
        return collided 

    def is_dead(self):
        return self.hp <= 0
    
    def try_to_damage(self, current_time, entity, camera):
        
        if self.first_time_pass or (current_time - self.last_time_attacked > self.attack_speed * ONE_SEC):
            if (self.first_time_pass):
                self.first_time_pass = False
            if not(self.state == UNIT_ATTACKING):
                self.change_state(UNIT_ATTACKING)
            self.last_time_attacked = current_time

            self.will_attack = True
        
        if self.state == UNIT_ATTACKING:
            if self.animation_frame == self.attack_frame and self.will_attack:
                self.will_attack = False
                entity.hp -= self.attack

                if entity.is_dead():
                    self.linked_map.remove_entity(entity)
                    

            elif self.animation_frame == (self.len_current_animation_frames() - 1):
                self.check_range_with_target = False # we need to recheck if it is still in range
                self.change_state(UNIT_IDLE) # if the entity is killed we stop 



            

    def try_to_attack(self,current_time, entity, camera):
        if (entity != None): 

            if (entity.is_dead() == False):
                
                
                if (self.range == 1): # for melee attack 
                    if not(self.check_range_with_target):
                        if (self.check_collision_with(entity)):
                            self.check_range_with_target = True
                            
                            print(f"animation_frame:{self.animation_frame}")
                            
                        else:
                            if not(self.state == UNIT_WALKING):
                                self.change_state(UNIT_WALKING)
                            self.first_time_pass = True
                            self.try_to_move(current_time, entity.position, camera)
                    else: # collided 
                        self.direction = self.position.alpha_angle(entity.position)
                        dist_to_entity = self.position.abs_distance(entity.position)

                        if (dist_to_entity <= (self.range * entity.sq_size * TILE_SIZE_2D)):
                            self.try_to_damage(current_time, entity, camera)
                        else:
                            self.check_range_with_target = False
                            if not(self.state == UNIT_IDLE):
                                self.change_state(UNIT_IDLE)
            
            
            else:
                if not(self.state == UNIT_IDLE):
                    self.change_state(UNIT_IDLE)
        else:        
            if not(self.state == UNIT_IDLE):
                self.change_state(UNIT_IDLE)


    
 