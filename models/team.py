class Team():
    def __init__(self, name, color, units, buildings, player):
        self.name = name
        self.color = color
        self.units = units
        self.buildings = buildings
        self.player = player
        self.resources = 0
        self.population = 0
        self.max_population = 0
        self.max_resources = 0
        self.resources_per_second = 0
        self.population_per_second = 0
        self.units_in_training = []
        self.buildings_in_construction