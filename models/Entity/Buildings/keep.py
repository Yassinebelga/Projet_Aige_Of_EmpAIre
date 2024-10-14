from building import Building

class Keep(Building):
    def __init__(self, position, team, name = "Keep", representation = "K", SQ_size = 1, hp = 800, cost = {"W" : 35, "G" : 125}, build_time = 80, walkable = False):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)