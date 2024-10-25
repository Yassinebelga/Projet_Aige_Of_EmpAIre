from .unit import Unit
from ..Buildings.building import Building
from time import*

class Villager(Unit):

    def __init__(self, position, team, name = "Villager", representation="v",SQ_size=1, hp=25, cost = {"F":50}, training_time=25, speed=0.8, attack=20, range=1, carry = 20, collect = 25, inventory= {"W":0,"G":0,"F":0}):
        super().__init__(position, team, name, representation, SQ_size , hp, cost,training_time,speed,attack,range)
        self.carry=carry, 
        self.collect=collect,
        self.inventory=inventory,

    def build_building(self,building):
        if map.is_area_free(self.position):
            for cle,values in building.cost:
                if self.player.inventory[cle]<= building.cost[cle]:
                    return 0
            building.build()
            map.add_entity(building)

    def gather_ressources(self,ressource):
        total_inventory=0
        lost_time_collect=time_time()#module de pygame a implementé
        for cle,values in self.inventory:
            total_inventory+=values
        while ressource.quantity!=0 and total_inventory<self.carry :
            if time_time()-lost_time_collect==60/self.collect:  #module de pygame a implementé
                self.inventory[ressource.name]+=1
                ressource.quantity-=1
        ressource.harvest

    def stocking_ressources(self,building):
        if building.drop_point :
            for keys,values in self.player.inventory:
                self.player.inventory[keys]+= self.inventory[keys]

