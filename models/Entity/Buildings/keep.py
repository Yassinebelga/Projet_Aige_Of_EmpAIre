from building import Building

class Keep(Building):
    def __init__(player ,build, SQ_size, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(player, SQ_size=1, build_time=80, cost={"W":35,"G":125}, build=False, hp=800, walkable=False, drop_point=False)