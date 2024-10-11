from building import Building

class Camp(Building):
    def __init__(player ,build, SQ_size, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(player, SQ_size=3, build_time=25, cost={"W":100}, build=False, hp=200, walkable=False, drop_point=True)