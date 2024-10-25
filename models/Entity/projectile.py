import math
import time

class PVector2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __add__(self,other_vector):
        return PVector2(self.x + self.y, other_vector.x + other_vector.y)
    
    def __mul__(self,const):
        return PVector2(self.x * const,self.y * const)
    
    def __rmul__(self,const):
        return PVector2(self.x * const,self.y * const)
    
    def __sub__(self,other_vector):
        return PVector2(self.x - other_vector.x, self.y - other_vector.y)
    
    def __rsub__(self,other_vector):
        return PVector2( other_vector.x - self.x, other_vector.y - self.y)
    
    def abs_distance(self,other_vector):
        return math.sqrt((self.x - other_vector.x)**2 + (self.y - other_vector.y)**2)
    
    def alpha_angle(self,other_vector):
        return math.atan2(other_vector.y - self.y, other_vector.x - self.x)

class Projectile:
    def __init__(self,position,damage):
        self.position=position
        self.damage=damage
        self.last_time_changed_pos=time.time()

    def update_position(self,entity_position,speed):
        if time.time()-self.last_time_changed_pos>0.008: #environ 60fps
            theta=self.position.alpha_angle(entity_position)
            self.position=PVector2(
                self.position.x + math.cos(theta) * speed,
                self.position.y + math.sin(theta) * speed
            )
            self.last_time_changed_pos=time.time()
    
    def is_almost(self,entity_position,distance=5):
        return self.position.abs_distance(entity_position)<distance
