from Projectile.projectile import *

class Arrow(Projectile):

    def __init__(self, position, entity_target, damage = 4):
        global ARROW_ARRAY_3D
        super().__init__(position, entity_target, damage)
        self.image = ARROW_ARRAY_3D