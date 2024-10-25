from building import Building

class Farm(Building):
    def __init__(self, position, team, name = "Farm", representation = "F", SQ_size = 2, hp = 100, cost = {"W" : 60}, build_time = 10, walkable = True, inventory = {"F" : 0}, max_food = 300):
        super().__init__(position, team, name, representation, SQ_size, hp, cost, build_time, walkable)
        self.inventory = inventory
        self.max_food = max_food
