from building import Building

class Barracks(Building):
    def __init__(self, player ,build, SQ_size, representation, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(self, player, SQ_size=3, build_time=50, representation="B", cost={"W":175}, build=False, hp=500, walkable=False, drop_point=False)

    def spawn_swordsmen(self):
        if self.build:
            pass