from unit import Unit

class Archer(Unit):
    def __init(self, position, hp, name, representation, SQ_size, player, cost, training_time, speed, attack,range=4):
        super().__init(position,player,name, hp=30,representation="a", SQ_size=1, cost={"W":25,"G":45}, training_time=35, speed=1, attack=4,range=4)



