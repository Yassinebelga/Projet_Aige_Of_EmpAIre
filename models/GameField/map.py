from GameField.cell import *
from GLOBAL_IMPORT import *
class Map:

    def __init__(self,_nb_CellX , _nb_CellY):
        

        self.nb_CellX = _nb_CellX
        self.nb_CellY = _nb_CellY
        self.tile_size_2d = TILE_SIZE_2D
        self.static_entity_matrix = {} #sparse matrix
        self.dynamic_entity_matrix = {} # also sparse
    
    def add_entity(self,_entity):
        assert (_entity != None), 0x0001 # to check if the entity is not null in case there were some problem in the implementation

        entity_in_matrix = (_entity.cell_X - (_entity.sq_size - 1) >= 0 and _entity.cell_Y - (_entity.sq_size - 1) >= 0) and ( _entity.cell_X < self.nb_CellX and _entity.cell_Y < self.nb_CellY)

        if (entity_in_matrix == False):
            
            return 0 # to check if all the cells that will be occupied by the entity are in the map
        
       
        for Y_to_check in range(_entity.cell_Y,_entity.cell_Y - _entity.sq_size, -1):
            for X_to_check in range(_entity.cell_X,_entity.cell_X - _entity.sq_size, -1):

                if self.static_entity_matrix.get((Y_to_check,X_to_check),None) != None:
                    
                    return 0 # not all the cells are free to put the entity 
                if self.dynamic_entity_matrix.get((Y_to_check, X_to_check),None)!= None:
                    return 0 

        if (not(isinstance(_entity, Unit))): # for static entities
            for Y_to_set in range(_entity.cell_Y,_entity.cell_Y - _entity.sq_size, -1):
                for X_to_set in range(_entity.cell_X,_entity.cell_X - _entity.sq_size, -1):
                    self.static_entity_matrix[(Y_to_set, X_to_set)] = _entity

            topleft_cell = PVector2(self.tile_size_2d/2 + ( _entity.cell_X - (_entity.sq_size - 1))*self.tile_size_2d, self.tile_size_2d/2 + (_entity.cell_Y - (_entity.sq_size - 1))*self.tile_size_2d) 
            bottomright_cell =  PVector2(self.tile_size_2d/2 + ( _entity.cell_X )*self.tile_size_2d, self.tile_size_2d/2 + (_entity.cell_Y )*self.tile_size_2d) 

            _entity.position = (bottomright_cell + topleft_cell ) * (0.5)
            _entity.box_size = bottomright_cell.x - _entity.position.x + TILE_SIZE_2D/2 # distance from the center to the corners of the collision box

            sorted_keys = sorted(self.static_entity_matrix.keys(), key=lambda k: (k[0], k[1]))

            # update with the new order 
            self.static_entity_matrix = {key: self.static_entity_matrix[key] for key in sorted_keys}

        else: # for units ( dynamic )
            
            _entity.position = PVector2(self.tile_size_2d/2 + _entity.cell_X*self.tile_size_2d, self.tile_size_2d/2 + _entity.cell_Y*self.tile_size_2d)
            _entity.box_size = TILE_SIZE_2D/(2*2) 

            unit_list = self.dynamic_entity_matrix.get((_entity.cell_Y, _entity.cell_X), None)

            if (unit_list):
                self.dynamic_entity_matrix[(_entity.cell_Y, _entity.cell_X)].add(_entity)
            else:
                self.dynamic_entity_matrix[(_entity.cell_Y, _entity.cell_X)] = set()
                self.dynamic_entity_matrix[(_entity.cell_Y, _entity.cell_X)].add(_entity)

        
        return 1 # added the entity succesfully
    
    def remove_entity(self,_entity):

        assert(_entity != None), 0x0011
        
        del self.static_entity_matrix[(_entity.Cell_Y, _entity.Cell_X)] # not finished yet !!!
        
    
        return 1 # added the entity succesfully

    def update_dynamic_entity_matrix(self):
        for Y_to_check, X_to_check in list(self.static_entity_matrix.keys()):
            current_cell = self.static_entity_matrix.get((Y_to_check, X_to_check), None)
            
            if (current_cell):
                if (current_cell.entity_representation != "-"):
                    self.static_entity_matrix[(current_cell.linked_entity.cell_Y, current_cell.linked_entity.cell_X)] = self.static_entity_matrix.pop((Y_to_check, X_to_check))
    
    def display(self, current_time, screen, camera, g_width, g_height):
        

        tmp_cell = Cell(0,0,PVector2(0,0))
        tmp_iso_x = 0
        tmp_iso_y = 0
        start_X, start_Y, end_X, end_Y = camera.indexes_in_point_of_view(self.nb_CellY, self.nb_CellX, g_width, g_height)

        entity_to_display = set()


        for Y_to_display in range(start_Y, end_Y + 1):
            for X_to_display in range(start_X, end_X + 1):
                tmp_cell.position.x = X_to_display*camera.tile_size_2d + camera.tile_size_2d/2
                tmp_cell.position.y = Y_to_display*camera.tile_size_2d + camera.tile_size_2d/2
                tmp_cell.display(screen, camera) 

                static_entity = self.static_entity_matrix.get((Y_to_display, X_to_display), None)
                if (static_entity):
                    entity_to_display.add(static_entity) # add the current cell to display it
                else:
                    dynamic_entities = self.dynamic_entity_matrix.get((Y_to_display, X_to_display),None)
                    if (dynamic_entities):
                        for dynamic_entity in dynamic_entities:
                            entity_to_display.add(dynamic_entity)

                    
        for current_entity in sorted(entity_to_display, key=lambda entity: (entity.position.y + entity.position.x, entity.position.y)):
            current_entity.display(current_time, screen, camera, g_width, g_height)
        
    
    def generate_map(self, num_players=2):
        
        # Ensure consistent random generation
        random.seed(0xba)
        
        
        self._place_player_starting_areas(num_players)

        
        self._generate_forests()
        self._generate_gold()

    
    def _generate_forests(self, forest_count=20, forest_size_range=(7, 17)):
        
        for _ in range(forest_count):
            # Randomly pick a forest center
            center_X = random.randint(0, self.nb_CellX - 1)
            center_Y = random.randint(0, self.nb_CellY - 1)
            forest_size = random.randint(*forest_size_range)

            GEN_DIS = 3
            for _ in range(forest_size):
                # Generate trees around the center
                offset_X = random.randint(-GEN_DIS, GEN_DIS)
                offset_Y = random.randint(-GEN_DIS, GEN_DIS)
                tree_X = center_X + offset_X
                tree_Y = center_Y + offset_Y

                # Add tree if position is valid and unoccupied
                if 0 <= tree_X < self.nb_CellX and 0 <= tree_Y < self.nb_CellY:
                    if self.static_entity_matrix.get((tree_Y, tree_X), None) == None:
                        tree = Tree(tree_Y, tree_X, None)
                        self.add_entity(tree)
    
    def _generate_gold(self, gold_veins=16, vein_size_range=(4, 15)):
        
        for _ in range(gold_veins):
            # Randomly pick a vein center
            center_X = random.randint(0, self.nb_CellX - 1)
            center_Y = random.randint(0, self.nb_CellY - 1)
            vein_size = random.randint(*vein_size_range)

            GEN_DIS = 2

            for _ in range(vein_size):
                # Generate gold around the center
                offset_X = random.randint(-GEN_DIS, GEN_DIS)
                offset_Y = random.randint(-GEN_DIS, GEN_DIS)
                
                gold_X = center_X + offset_X
                gold_Y = center_Y + offset_Y

                # Add gold if position is valid and unoccupied
                if 0 <= gold_X < self.nb_CellX and 0 <= gold_Y < self.nb_CellY:
                    if self.static_entity_matrix.get((gold_Y, gold_X), None) == None:
                        gold = Gold(gold_Y, gold_X, None)
                        self.add_entity(gold)
    
    def _place_player_starting_areas(self, num_players):
        
        spacing = self.nb_CellX // num_players 
        for i in range(num_players):
            # Base position for this player's starting area
            base_X = spacing * i + spacing // 2
            base_Y = self.nb_CellY // 2

            
            offset_X = random.randint(-3, 3)  # Random horizontal offset
            offset_Y = random.randint(-self.nb_CellY//num_players, self.nb_CellY//num_players)  # Random vertical offset
            center_X = max(0, min(self.nb_CellX - 1, base_X + offset_X))  # Keep within bounds
            center_Y = max(0, min(self.nb_CellY - 1, base_Y + offset_Y))  

            if self.static_entity_matrix.get((center_Y, center_X), None) == None :
                town_center = TownCenter(center_Y, center_X, None, team=i + 1)
                self.add_entity(town_center)
                
                self._add_starting_resources(center_Y, center_X)
    
    def _add_starting_resources(self, center_Y, center_X):
        GEN_DIS_G = 2
        GEN_DIS_T = 1
        for offset_X, offset_Y in [(-GEN_DIS_G, GEN_DIS_G), (GEN_DIS_G, -GEN_DIS_G), (GEN_DIS_G, GEN_DIS_G)]:
            gold_X = center_X + offset_X
            gold_Y = center_Y + offset_Y
            if self.static_entity_matrix.get((gold_Y, gold_X), None) == None :
                
                gold = Gold(gold_Y, gold_X, None)
                self.add_entity(gold)

        for offset_X, offset_Y in [(GEN_DIS_T, GEN_DIS_T), (GEN_DIS_T, -GEN_DIS_T), (-GEN_DIS_T, GEN_DIS_T)]:
            tree_X = center_X + offset_X
            tree_Y = center_Y + offset_Y
            if self.static_entity_matrix.get((tree_Y, tree_X), None) == None:
                
                tree = Tree(tree_Y, tree_X, None)
                self.add_entity(tree)