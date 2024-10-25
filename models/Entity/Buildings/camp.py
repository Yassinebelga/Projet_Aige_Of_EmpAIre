from building import Building

class Camp(Building):
    def __init__(self, position, team, name = "Camp", representation = "C", SQ_size = 2, hp = 200, cost = {"W" : 100}, build_time = 25, walkable = False, drop_point = True):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)
        self.drop_point = drop_point
