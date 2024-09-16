
class Building(Entity):
    def __init__(self,cost,build_time,hp,size):
        self.cost=cost
        self.build_time=build_time
        self.hp=hp
        self.size=size

class TownCenter(Building):
    def __init__(self, cost, build_time, hp, size):
        super().__init__(cost, build_time, hp, size)

class House(Building):
    def __init__(self, cost, build_time, hp, size):
        super().__init__(cost, build_time, hp, size)

class Camp(Building):
    def __init__(self, cost, build_time, hp, size):
        super().__init__(cost, build_time, hp, size)

class Farm(Building):
    def __init__(self, cost, build_time, hp, size):
        super().__init__(cost, build_time, hp, size)

class Barracks(Building):
    def __init__(self, cost, build_time, hp, size):
        super().__init__(cost, build_time, hp, size)

class Stable(Building):
    def __init__(self, cost, build_time, hp, size):
        super().__init__(cost, build_time, hp, size)

class Archery(Building):
    def __init__(self, cost, build_time, hp, size):
        super().__init__(cost, build_time, hp, size)

class Keep(Building):
    def __init__(self, cost, build_time, hp, size):
        super().__init__(cost, build_time, hp, size)