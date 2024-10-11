from building import Building

class TownCenter(Building):
    def __init__(player ,build, SQ_size, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(player, SQ_size=4, build_time=150, cost={"W":350}, build=False, hp=1000, walkable=False, drop_point=True, population=5)

    def spawn():
        pass