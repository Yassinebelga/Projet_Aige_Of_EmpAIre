from entity import Entity

class Building(Entity):
    def __init__(self, position, team, name, representation, SQ_size, hp, cost, build_time, walkable):
        super().__init__(position, team, name, representation, SQ_size)
        self.hp=hp
        self.cost=cost
        self.build_time=build_time
        self.walkable=walkable
    
    def building():
        pass


    def building_time():
        pass