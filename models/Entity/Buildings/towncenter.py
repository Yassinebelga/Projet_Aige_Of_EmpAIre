from building import Building

class TownCenter(Building):
    def __init__(self, position, team, name = "Town Center", representation = "T", SQ_size = 4, hp = 1000, cost = {"W" : 350}, build_time = 150, walkable = False, unit_spawn = None, drop_point = True, population = 5):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)
        self.unit_spawn = unit_spawn
        self.drop_point = drop_point
        self.population = population

    def spawn():
        pass