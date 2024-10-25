import math

class PVector2:
    
    def __init__(self,_x,_y):
        self.x = _x #float
        self.y = _y #float
 
    def __add__(self,other_vector):
        return PVector2(self.x + self.y,other_vector.x + other_vector.y)

    def __mul__(self,const):
        return PVector2(self.x * const, self.y * const)

    def __rmul__(self,const):
        return PVector2(self.x * const, self.y * const)
    
    def __sub__(self,other_vector):
        return PVector2(self.x - other_vector.x,self.y - other_vector.y)

    def __rsub__(self,other_vector):
        return PVector2(other_vector.x - self.x, other_vector.y - self.y)

    def abs_distance(self,other_vector):
        return math.sqrt((self.x - other_vector.x)**2 + (self.y - other_vector.y)**2)

    def alpha_angle(self, other_vector):
        delta_x = other_vector.x - self.x
        delta_y = other_vector.y - self.y
        return math.atan2(delta_y, delta_x)




    