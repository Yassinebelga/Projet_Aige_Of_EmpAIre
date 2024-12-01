from GLOBAL_VAR import *
class Projectile:
    
    def __init__(self, position, entity_target, damage):
        global ONE_SEC
        global PROJECTILE_ANGLE_MAPPING

        self.position = position 
        self.damage = damage
        self.entity_target = entity_target

        self.time_to_get_target = ONE_SEC
        
        self.time_left = self.time_to_get_target
        self.distance_left = self.position.abs_distance(entity_target.position)
        self.last_time_changed_pos = pygame.time.get_ticks()
        self.direction = self.position.alpha_angle(entity_target.position)
        
        self.image = None
        self.last_animation_time = pygame.time.get_ticks()
        self.animation_direction = MAP_ANGLE_INDEX(self.direction, PROJECTILE_ANGLE_MAPPING)
        self.animation_frame = 0
        
        self.projectile_peak = self.position.abs_distance(entity_target.position)
        self.projectile_z_pos = 0
        self.representation = 'p'
    def update_position(self, current_time):
        time_elapsed = current_time - self.last_time_changed_pos
        
        if time_elapsed > 0:
            # Calculate the angle to the target
            if (self.entity_target):
                self.direction = self.position.alpha_angle(self.entity_target.position)
                self.distance_left = self.position.abs_distance(self.entity_target.position)
            if self.time_left > 0:
                distance_to_add = self.distance_left / (self.time_left / time_elapsed)
                self.position.x = self.position.x + math.cos(self.direction) * distance_to_add 
                self.position.y = self.position.y + math.sin(self.direction) * distance_to_add
                

                progress_ratio = (self.time_to_get_target - self.time_left)/self.time_to_get_target
                # f(x) = -a*(x**(b) - 0.5)**2 + peak , the function that returns the value of z where x is the ratio, lets find a 

                a = self.projectile_peak/(0.5)**2
                b = 2 
                # f(progress_ratio)
                self.projectile_z_pos = -a*((progress_ratio)**(b) - 0.5)**2 + self.projectile_peak
                

                self.time_left -= time_elapsed
                self.distance_left = - self.distance_left - distance_to_add
                self.last_time_changed_pos = current_time
            else:
                distance_to_add = self.distance_left   

                self.position.x = self.position.x + math.cos(self.direction) * distance_to_add 
                self.position.y = self.position.y + math.sin(self.direction) * distance_to_add


    def update_animation_frame(self, current_time):

        if current_time - self.last_animation_time > self.time_to_get_target/11:
            self.last_animation_time = current_time
            self.animation_frame = (self.animation_frame + 1)%len(self.image[0][0])
        
    def display(self, current_time, screen, camera):
        
        x, y = camera.convert_to_isometric_2d(self.position.x, self.position.y)

        self.update_animation_frame(current_time)
        iso_x, iso_y = camera.convert_to_isometric_3d(self.position.x, self.position.y,self.projectile_z_pos)
        display_image(META_SPRITES.get(self.representation, None)[camera.zoom][self.animation_direction][self.animation_frame],iso_x, iso_y, screen, 0x04)
