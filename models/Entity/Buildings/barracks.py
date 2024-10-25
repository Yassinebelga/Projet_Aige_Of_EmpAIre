from building import Building

class Barracks(Building):
<<<<<<< HEAD
    def __init__(self, player ,build, SQ_size, representation, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(self, player, SQ_size=3, build_time=50, representation="B", cost={"W":175}, build=False, hp=500, walkable=False, drop_point=False)
=======
    def __init__(self, position, team, name = "Barracks", representation = "B", SQ_size = 3, hp = 500, cost = {"W" : 175}, build_time = 50, walkable = False, unit_spawn = None):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)
        self.unit_spawn = unit_spawn
>>>>>>> 372ab19cbfd441ee86fdb1b044712fa73c5c349b

    def spawn_swordsmen(self):
        if self.build:
            pass