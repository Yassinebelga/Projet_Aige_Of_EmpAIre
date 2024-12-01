from Entity.Resources.resources import *
class Tree(Resources):
    
    def __init__(self, cell_X, cell_Y, position, representation = 'w', storage= TREE_CAPACITY):
        super().__init__(cell_X, cell_Y, position, representation, storage)
        self.image = TREES_ARRAY_1D
        self.display_choice = random.randint(0,len(TREES_ARRAY_1D) - 1)
