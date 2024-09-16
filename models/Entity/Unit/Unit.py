class Unit:

    def __init__(self,type,training_time,hp,attack,speed,cost):
        self.type=type
        self.training_time=training_time
        self.hp=hp
        self.attack=attack
        self.speed=speed
        self.cost=cost


class Horseman(Unit):
    def __init__(self, type, training_time, hp, attack, speed, cost):
        super().__init__(type, training_time, hp, attack, speed, cost)

class Archer(Unit):
    def __init__(self, type, training_time, hp, attack, speed, cost):
        super().__init__(type, training_time, hp, attack, speed, cost)

class Villager(Unit):
    def __init__(self, type, training_time, hp, attack, speed, cost):
        super().__init__(type, training_time, hp, attack, speed, cost)
        

