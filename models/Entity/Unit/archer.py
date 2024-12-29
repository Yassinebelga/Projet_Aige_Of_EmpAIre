from Entity.Unit.unit import *
from Projectile.arrow import *

class Archer(Unit):

    def __init__(self, cell_Y, cell_X, position, team, representation = 'a', hp = 30, cost = 25, training_time = 35*ONE_SEC, speed = 1, attack =4, attack_speed = 1.2, _range = 7):
        super().__init__(cell_Y, cell_X, position, team, representation, hp, cost, training_time, speed, attack, attack_speed, _range)
        self.image = ARCHER_ARRAY_3D
        self.last_time_sent_arrow = pygame.time.get_ticks()
        self.arrow_array = []
        self.animation_speed = [60,30,30/self.attack_speed,30]
        self.attack_frame = 17

    def display(self, current_time, screen, camera, g_width, g_height):
        
        super().display(current_time, screen, camera, g_width, g_height)
        
        """
        for arrow_index in range(len(self.arrow_array)): # tmp test
            
             
            self.arrow_array[arrow_index].update_position(current_time)
            o_x, o_y = camera.convert_to_isometric_3d(self.arrow_array[arrow_index].position.x, self.arrow_array[arrow_index].position.y,self.arrow_array[arrow_index].projectile_z_pos)

            self.arrow_array[arrow_index].display(current_time, screen, camera)
        """
    
    def check_in_range_with(self, entity):
        return self.position.abs_distance(entity.position) < (self.linked_map.tile_size_2d * self.range)
    

    def try_to_damage(self, current_time, _entity, camera):
        
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

                arrow = Arrow(self.cell_Y, self.cell_X, PVector2(self.position.x, self.position.y), _entity, self.linked_map)
                self.linked_map.add_projectile(arrow)

            elif self.animation_frame == (self.len_current_animation_frames() - 1):
                self.check_range_with_target = False # we need to recheck if it is still in range
                self.change_state(UNIT_IDLE) # if the entity is killed we stop


    def try_to_attack(self,current_time, entity, camera):
        if (entity != None): 

            if (entity.is_dead() == False):
                
                   
                if not(self.check_range_with_target):
                    if (self.check_in_range_with(entity)):
                        self.check_range_with_target = True
                        
                        print(f"animation_frame:{self.animation_frame}")
                        
                    else:
                        if not(self.state == UNIT_WALKING): # we need to reach it in range
                            self.change_state(UNIT_WALKING)
                        self.first_time_pass = True
                        self.try_to_move(current_time, entity.position, camera)
                else: # enemy in range  
                    self.direction = self.position.alpha_angle(entity.position)
                    dist_to_entity = self.position.abs_distance(entity.position)

                    if (dist_to_entity <= (self.range * (entity.sq_size) * TILE_SIZE_2D + entity.box_size + self.box_size)):
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