import math
from GLOBAL_VAR import TILE_SIZE_2D
def is_almost(a, b, p=1e-7):
    return abs(a - b) < p

class PVector2:
    def __init__(self,_x,_y, _z = 0):
        self.x = _x #float
        self.y = _y #float
        self.z = _z # float
        
    def __add__(self,other_vector):
        return PVector2(self.x + other_vector.x,self.y + other_vector.y)

    def __mul__(self,const):
        return PVector2(self.x * const, self.y * const)

    def __rmul__(self,const):
        return PVector2(self.x * const, self.y * const)
    
    def __sub__(self,other_vector):
        return PVector2(self.x - other_vector.x,self.y - other_vector.y)

    def __eq__(self, other):
        return is_almost(self.x, other.x, TILE_SIZE_2D/20) and is_almost(self.y, other.y, TILE_SIZE_2D/20)
    
    def __lt__(self, other):
        return self.x <= other.x and self.y <= other.y 

    def __gt__(self, other):
        return self.x >= other.x and self.y >= other.y

    def abs_distance(self,other_vector):
        return math.sqrt((self.x - other_vector.x)**2 + (self.y - other_vector.y)**2)

    def alpha_angle(self, other_vector):
        delta_x = other_vector.x - self.x
        delta_y = other_vector.y - self.y
        return (math.atan2(delta_y, delta_x) + 2*math.pi)%(2*math.pi)
    
    
    def __str__(self):
        return f"({self.x},{self.y})"