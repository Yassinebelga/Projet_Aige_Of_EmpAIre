from entity import Entity
from cell import Cell
from vector import Vector


class Map:
    n = 120
    m = 120

    def __init__ (self, n ,m):
        self.m = m
        self.n = n

    def generate_map(self):
        for i in range (self.n):
            for j in range (self.m):
                self.tab[i][j] = Cell()

    def add_entity(entity):
        if(self.tab[entity.position[0]][entity.position[1]].occupied == True):
            return 0
        else:
            self.tab[entity.position[0]][entity.position[1]].entity = entity 
            return 1

    def show_map(self):
        for i in range (self.n):
            for j in range (self.m):
                if(self.tab[i][j].occupied == True):
                    print(f"{cell.entity.representation}", end=" ")
                else:
                    print(" ")

    def remove_entity(entity):
        if(self.tab[entity.position[0]][entity.position[1]].occupied == True):
            self.tab[entity.position[0]][entity.position[1]].entity = None
            return 1
        else:
            return 0