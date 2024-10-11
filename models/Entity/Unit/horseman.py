from unit import Unit

class Horseman(Unit):
    def __init(self, position, hp, name, representation, SQ_size, player, cost, training_time, speed, attack):
        super().__init(position, player, name,hp=45, representation="h", SQ_size=1, cost={"F":80,"G":20}, training_time=30, speed=1.2, attack=4)
    

