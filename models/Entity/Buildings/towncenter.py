from building import Building

class TownCenter(Building):
    def __init__(self, player ,build, SQ_size, representation, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(self, player, SQ_size=4, representation="T", build_time=150, cost={"W":350}, build=False, hp=1000, walkable=False, drop_point=True, population=500)

    def spawn(self):
        if self.build:
            pass