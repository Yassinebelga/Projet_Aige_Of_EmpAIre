from building import Building

class archeryRange(Building):
<<<<<<< HEAD
    def __init__(self, player ,build, SQ_size, representation, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(player, SQ_size=3, representation="A", build_time=50, cost={"W":175}, build=False, hp=500, walkable=False, drop_point=False)

    def spawn_archers(self):
        if self.build:
            pass
        
=======
    def __init__(self, position, team, name = "Archery Range", representation = "A", SQ_size = 3, hp = 500, cost = {"W" : 175}, build_time = 50, walkable = False, unit_spawn = None):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)
        self.unit_spawn = unit_spawn
        
    def spawn_archers():
        pass
>>>>>>> 372ab19cbfd441ee86fdb1b044712fa73c5c349b
