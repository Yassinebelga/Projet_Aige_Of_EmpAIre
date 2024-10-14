from building import Building

class House(Building):
    def __init__(self, position, team, name = "House", representation = "H", SQ_size = 2, hp = 200, cost = {"W" : 25}, build_time = 25, walkable = False, population = 5):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)
        self.population = population