from unit import Unit

class Horseman(Unit):
    def __init(self, position, team, name = "Horseman", representation = "h", SQ_size =1 , hp = 45, cost = {"F":80,"G":20},training_time = 30 ,speed = 1.2 ,attack = 4):
        super().__init(position, team, name, representation, SQ_size, hp, cost, training_time, speed, attack)
    

