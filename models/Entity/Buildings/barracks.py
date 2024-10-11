from building import Building

class Barracks(Building):
    def __init__(player ,build, SQ_size, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(player, SQ_size=3, build_time=50, cost={"W":175}, build=False, hp=500, walkable=False, drop_point=False)

    def spawn_swordsmen():
        pass