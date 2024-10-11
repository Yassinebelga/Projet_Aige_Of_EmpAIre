from ...entity import Entity

class Unit(Entity):

    def __init(self, position, name, team, representation, SQ_size , hp, cost,training_time,speed,attack,range=1):
        super().__init(position, name, team, representation, SQ_size=1)
        self.hp = hp
        self.training_time=training_time
        self.attack=attack
        self.speed=speed
        self.cost=cost
        self.range=range
    
    def attacking(self,entity):
        lost_time_collect=time_time()       #module de pygame a implementé
        vecteur_position=PVector2(self.position[0],self.position[1])            # classe vecteur créer par Ali
        vecteur_position_adverse =PVector2(entity.position[0],entity.position[1])
        while is_alive(entity) and abs_distance(vecteur_position_adverse) <=self.range:     # méthode de la classe vecteur créer par Ali
            if time_time()-lost_time_collect==1:                            #module de pygame a implementé
                entity.hp-=self.attack
        if not is_alive(entity):
            map.remove_entity(entity)