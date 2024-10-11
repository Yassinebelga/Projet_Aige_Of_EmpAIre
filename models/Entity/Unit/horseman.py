from unit import Unit

class Horseman(Unit):
    def __init(self, position, name, team, representation, SQ_size , hp, cost,training_time,speed,attack):
        super().__init(position, name, team, representation="h", SQ_size=1, hp=45, cost={"F":80,"G":20}, training_time=30, speed=1.2, attack=4)
    

