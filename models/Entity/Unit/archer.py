from Entity.Unit.unit import *
from Projectile.arrow import *

class Archer(Unit):

    def __init__(self, cell_Y, cell_X, position, team, representation = 'a', hp = 30, cost = 25, training_time = 35*ONE_SEC, speed = 1, attack =4, attack_speed = 1.2, _range =4):
        global ARCHER_ARRAY_4D
        super().__init__(cell_Y, cell_X, position, team, representation, hp, cost, training_time, speed, attack, attack_speed, _range)
        self.image = ARCHER_ARRAY_4D
        self.last_time_sent_arrow = pygame.time.get_ticks()
        self.arrow_array = []
        self.animation_speed = [60,30,30/self.attack_speed,30]


    #tmp function just to test the projecctiles, manage attacks and targeting entities will work differently and in a proper way
    def attacking(self, current_time, entity_to_target):
        if (current_time - self.last_time_sent_arrow> self.attack_speed * ONE_SEC):
            global UNIT_ATTACKING
            global TILE_SIZE_2D
            self.last_time_sent_arrow = current_time

            self.state = UNIT_ATTACKING
            self.set_target(entity_to_target)

            self.direction = self.position.alpha_angle(self.entity_target.position)
            self.will_attack = True
            self.set_direction_index()
            

        if ( self.state == UNIT_ATTACKING and self.animation_frame == 18 and self.will_attack ): # animation index of the moment when the archer throws the arrow in the sprite of the archer 
            self.will_attack = False
            arrow = Arrow(PVector2(self.position.x -TILE_SIZE_2D/2 , self.position.y -TILE_SIZE_2D/2), self.entity_target)
            self.arrow_array.append(arrow)

    def display(self, current_time, screen, camera, g_width, g_height):
        
        super().display(current_time, screen, camera, g_width, g_height)
        
        for arrow_index in range(len(self.arrow_array)): # tmp test
            
             
            self.arrow_array[arrow_index].update_position(current_time)
            o_x, o_y = camera.convert_to_isometric_3d(self.arrow_array[arrow_index].position.x, self.arrow_array[arrow_index].position.y,self.arrow_array[arrow_index].projectile_z_pos)

            self.arrow_array[arrow_index].display(current_time, screen, camera)
