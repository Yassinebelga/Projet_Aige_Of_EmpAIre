from unit import Unit

class Archer(Unit):
    def __init(self, position, name, team, representation, SQ_size , hp, cost,training_time,speed,attack,range=4):
        super().__init(position,name,team, representation = "a", SQ_size = 1, hp = 30, cost={"W":25,"G":45}, training_time=35, speed=1, attack=4,range=4)



