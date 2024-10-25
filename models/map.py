from Entity import *

class Map:

    def __init__(self,_nb_CellX = 120,_nb_CellY = 120,_draw_position):
        self.nb_CellX = _nb_CellX
        self.nb_CellY = _nb_CellY
        self.draw_position = _draw_position
        self.cell_matrix = [[Cell(_X,_Y) for _X in range(_nb_CellX)] for _Y in range(_nb_CellY)]

    def add_entity(self,_Y_to_add,_X_to_add,_entity):
        assert (_entity != None), 0x0001 # to check if the entity is not null in case there were some problem in the implementation

        entity_in_matrix = (_X_to_add >= 0 and _Y_to_add >= 0) and (_X_to_add + (_entity.sq_size - 1)< self.nb_CellX and _Y_to_add + (_entity.sq_size - 1)< self.nb_CellY)

        assert (entity_in_matrix), 0x0002 # to check if all the cells that will be occupied by the entity are in the map


        for Y_to_check in range(_Y_to_add,_Y_to_add + _entity.sq_size):
            for X_to_check in range(_X_to_add,_X_to_add + _entity.sq_size):

                if self.cell_matrix[Y_to_check][X_to_check].is_free() == False:
                    return 0 # not all the cells are free to put the entity 


        for Y_to_set in range(_Y_to_add, _Y_to_add + _entity.sq_size):
            for X_to_set in range(_X_to_add, _X_to_add + _entity.sq_size):

                self.cell_matrix[Y_to_set][X_to_set].set_occupied() # set the cell to occupied ( cell.free = false )
                self.cell_matrix[Y_to_set][X_to_set].link_entity(_entity) # link the entity to this cell

        return 1 # added the entity succesfully
    
    def remove_entity(self,_entity):

        assert(_entity != None), 0x0011
        
        for Y_to_remove in range(self.nb_CellY):
            for X_to_remove in range(self.nb_CellX):

                if self.cell_matrix[Y_to_remove][X_to_remove].linked_entity == _entity:
                    self.cell_matrix[Y_to_remove][X_to_remove].set_free()
                    self.cell_matrix[Y_to_remove][X_to_remove].unlink_entity( _entity)
    
        return 1 # added the entity succesfully

    def display(self):
        for Y_to_display in range(self.nb_CellY):
            for X_to_display in range(self.nb_CellX):

                if self.cell_matrix[Y_to_display][X_to_display].is_free():
                    print("- ",end="")
                else:
                    print(self.cell_matrix[Y_to_display][X_to_display].linked_entity.representation,end="")
            print()
                


    



        

        


        

