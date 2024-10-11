from building import Building

class House(Building):
    def __init__(player ,build, SQ_size, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(player, SQ_size=2, build_time=25, cost={"W":25}, build=False, hp=200, walkable=False, drop_point=False, population=5)