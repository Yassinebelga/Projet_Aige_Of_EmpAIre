from building import Building

class Camp(Building):
    def __init__(self, player ,build, SQ_size, representation, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(self, player, SQ_size=3, representation="C", build_time=25, cost={"W":100}, build=False, hp=200, walkable=False, drop_point=True)