from .unit import Unit
from ..Buildings.building import Building
from time import*

class Villager(Unit):

    def __init__(self,position,SQ_size, player, training_time, hp, attack, speed, cost,carry,collect,inventory):
        super().__init__(player,position,SQ_size=1, training_time=25, hp=25, attack=2, speed=0.8, cost={"F":50},collect=25,carry=20,inventory={"W":0,"G":0,"F":0})

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

