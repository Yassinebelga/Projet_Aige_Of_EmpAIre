class Entity():
    def __init__(self, position, name, hp, SQ_size, representation):
        self.position = position
        self.name = name
        self.hp = hp
        self.SQ_size = SQ_size
        self.representation = representation


    def is_alive(self):
        return self.hp > 0
    
    ##def attacking(self, entity):
    ##    entity.hp -= self.attack