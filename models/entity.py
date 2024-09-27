class Entity():
    def __init__(self, position, name, hp, size, representation):
        self.position = position
        self.name = name
        self.hp = hp
        self.size = size
        self.representation = representation


    def is_alive(self):
        return self.hp > 0
    
    ##def attacking(self, entity):
    ##    entity.hp -= self.attack