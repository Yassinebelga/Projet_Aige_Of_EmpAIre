from building import Building

class Farm(Building):
    def __init__(self, player ,build, SQ_size, representation, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(self, player, SQ_size=2, representation="F", build_time=10, cost={"W":60}, build=False, hp=100, walkable=True, drop_point=False, food={"F":300})