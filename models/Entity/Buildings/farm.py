from building import Building

class Farm(Building):
<<<<<<< HEAD
    def __init__(self, player ,build, SQ_size, representation, build_time, cost, hp, walkable, drop_point, population):
        super().__init__(self, player, SQ_size=2, representation="F", build_time=10, cost={"W":60}, build=False, hp=100, walkable=True, drop_point=False, food={"F":300})
=======
    def __init__(self, position, team, name = "Farm", representation = "F", SQ_size = 2, hp = 100, cost = {"W" : 60}, build_time = 10, walkable = True, inventory = {"F" : 0}, max_food = 300):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)
        self.inventory = inventory
        self.max_food = max_food
>>>>>>> 372ab19cbfd441ee86fdb1b044712fa73c5c349b
