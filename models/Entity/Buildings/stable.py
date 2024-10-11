from building import Building

class Stable(Building):
    def __init__(self, player ,build, SQ_size, representation, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(self, player, SQ_size=3, representation="S", build_time=50, cost={"W":175}, build=False, hp=500, walkable=False, drop_point=False)

    def spawn_horsemen(self):
        if self.build:
            pass