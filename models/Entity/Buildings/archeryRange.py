from building import Building

class archeryRange(Building):
    def __init__(self, position, team, name = "Archery Range", representation = "A", SQ_size = 3, hp = 500, cost = {"W" : 175}, build_time = 50, walkable = False, unit_spawn = None):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)
        self.unit_spawn = unit_spawn
        
    def spawn_archers():
        pass
