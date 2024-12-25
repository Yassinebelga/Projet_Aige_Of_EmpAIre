from GameField.cell import *
from GLOBAL_IMPORT import *
from ImageProcessingDisplay.minimap import *
from AITools.isorange import *
from AITools.raycastingrange import *

class Map:

    def __init__(self,_nb_CellX , _nb_CellY):
        

        self.nb_CellX = _nb_CellX
        self.nb_CellY = _nb_CellY
        self.tile_size_2d = TILE_SIZE_2D
        self.region_division = REGION_DIVISION
        self.entity_matrix = {} #sparse matrix

        self.last_time_refershed = pygame.time.get_ticks() # refresh for the terminal display


        # for the minimap
        self.minimap = MiniMap(PVector2(1000,300), _nb_CellX, _nb_CellY)

    def check_cell(self, Y_to_check, X_to_check):
        REG_Y_to_check, REG_X_to_check = Y_to_check//self.region_division, X_to_check//self.region_division

        region = self.entity_matrix.get((REG_Y_to_check, REG_X_to_check),None)

        if (region):
            if region.get((Y_to_check, X_to_check), None) != None:
                return True 
        
        return False 

    def add_entity(self, _entity):
        assert (_entity != None), 0x0001 # to check if the entity is not null in case there were some problem in the implementation

        entity_in_matrix = (_entity.cell_X - (_entity.sq_size - 1) >= 0 and _entity.cell_Y - (_entity.sq_size - 1) >= 0) and ( _entity.cell_X < self.nb_CellX and _entity.cell_Y < self.nb_CellY)

        if (entity_in_matrix == False):
            
            return 0 # to check if all the cells that will be occupied by the entity are in the map
        
       
        for Y_to_check in range(_entity.cell_Y,_entity.cell_Y - _entity.sq_size, -1):
            for X_to_check in range(_entity.cell_X,_entity.cell_X - _entity.sq_size, -1):
                
                if self.check_cell(Y_to_check, X_to_check):
                    return 0 # not all the cells are free to put the entity 
        
        for Y_to_set in range(_entity.cell_Y,_entity.cell_Y - _entity.sq_size, -1):
            for X_to_set in range(_entity.cell_X,_entity.cell_X - _entity.sq_size, -1):

                REG_Y_to_set, REG_X_to_set = Y_to_set//self.region_division, X_to_set//self.region_division
                current_region = self.entity_matrix.get((REG_Y_to_set, REG_X_to_set),None)

                if (current_region == None):
                    self.entity_matrix[(REG_Y_to_set, REG_X_to_set)] = {}
                    current_region = self.entity_matrix.get((REG_Y_to_set, REG_X_to_set),None)

                current_cell = current_region.get((Y_to_set, X_to_set), None)
                
                if (current_cell == None):
                    current_region[(Y_to_set, X_to_set)] = set()
                    current_cell = current_region.get((Y_to_set, X_to_set), None)
                
                current_cell.add(_entity)

        topleft_cell = PVector2(self.tile_size_2d/2 + ( _entity.cell_X - (_entity.sq_size - 1))*self.tile_size_2d, self.tile_size_2d/2 + (_entity.cell_Y - (_entity.sq_size - 1))*self.tile_size_2d) 
        bottomright_cell =  PVector2(self.tile_size_2d/2 + ( _entity.cell_X )*self.tile_size_2d, self.tile_size_2d/2 + (_entity.cell_Y )*self.tile_size_2d) 

        _entity.position = (bottomright_cell + topleft_cell ) * (0.5)
        _entity.box_size = bottomright_cell.x - _entity.position.x  # distance from the center to the corners of the collision box

        if isinstance(_entity, Unit):
            _entity.box_size += TILE_SIZE_2D/(2 * 3)
            _entity.linked_map = self
        else:
            _entity.box_size += TILE_SIZE_2D/(2 * 2)
        
        return 1 # added the entity succesfully
    
    def remove_entity(self,_entity):

        assert(_entity != None), 0x0011
        
        del self.entity_matrix[(_entity.Cell_Y, _entity.Cell_X)] # not finished yet !!!
        
    
        return 1 # added the entity succesfully

    def update_dynamic_entity_matrix(self):
        pass 
    
    def display(self, current_time, screen, camera, g_width, g_height):
        

        tmp_cell = Cell(0, 0, PVector2(0,0))
        tmp_topleft = PVector2(0, 0)
        tmp_bottomright = PVector2(0, 0)

        (top_Y, top_X), (left_Y, left_X), (right_Y, right_X), (bottom_Y, bottom_X) = camera.indexes_in_point_of_view(g_width, g_height)
        
        top_Xt = max(0, min(top_X, self.nb_CellX - 1))
        top_Yt = max(0, min(top_Y, self.nb_CellY - 1))

        right_Xt = max(0, min(right_X, self.nb_CellX - 1))
        right_Yt = max(0, min(right_Y, self.nb_CellY - 1))

        left_Xt = max(0, min(left_X, self.nb_CellX - 1))
        left_Yt = max(0, min(left_Y, self.nb_CellY - 1))

        bottom_Xt = max(0, min(bottom_X, self.nb_CellX - 1))
        bottom_Yt  = max(0, min(bottom_Y, self.nb_CellY - 1))
        
        top = (top_Yt, top_Xt)
        left = (left_Yt, left_Xt)
        right = (right_Yt, right_Xt)
        bottom = (bottom_Yt, bottom_Xt)

        range_top = (top[0] // self.region_division, top[1] // self.region_division)
        range_left = (left[0] // self.region_division, left[1] // self.region_division)
        range_right = (right[0] // self.region_division, right[1] // self.region_division) 
        range_bottom = (bottom[0] // self.region_division, bottom[1] // self.region_division) 
 
        #print(f"top:{top}, left:{left}, right:{right}")

        entity_to_display = set()
        
        for region_Y_to_display, region_X_to_display in isoRange(range_top, range_left, range_right, range_bottom):

                if region_Y_to_display >= 0 and region_Y_to_display < self.nb_CellY//self.region_division \
                    and region_X_to_display>=0 and region_X_to_display < self.nb_CellX//self.region_division:
                    #print(f"REG_Y: {region_Y_to_display}, REG_X: {region_X_to_display}")

                    # these are the real X Y of the region in the sparse matrix

                    REG_X, REG_Y = region_X_to_display * (self.region_division ), region_Y_to_display * (self.region_division )
                    
                    tmp_topleft.x = TILE_SIZE_2D/2 + REG_X*TILE_SIZE_2D
                    tmp_topleft.y = TILE_SIZE_2D/2 + REG_Y*TILE_SIZE_2D

                    tmp_bottomright.x = TILE_SIZE_2D/2 + (REG_X + (self.region_division - 1))*TILE_SIZE_2D
                    tmp_bottomright.y = TILE_SIZE_2D/2 + (REG_Y + (self.region_division - 1))*TILE_SIZE_2D

                    tmp_cell.position = (tmp_bottomright + tmp_topleft) * (0.5)

                    tmp_cell.display(screen, camera)

                    #check if this region contains entity
                    region_entities = self.entity_matrix.get((region_Y_to_display, region_X_to_display), None)
                    if region_entities != None:

                        for entities in region_entities.values(): # each value the region is a dict of the cells
                            for entity in entities:
                                entity_to_display.add(entity)
        """             
        for Y_to_display in range(start_Y, end_Y + 1):
            for X_to_display in range(start_X, end_X + 1):
                
                tmp_cell.position.x = X_to_display*camera.tile_size_2d + camera.tile_size_2d/2
                tmp_cell.position.y = Y_to_display*camera.tile_size_2d + camera.tile_size_2d/2
                iso_x, iso_y = camera.convert_to_isometric_2d(tmp_cell.position.x, tmp_cell.position.y)

                pygame.draw.circle(screen, (255, 0, 0), (iso_x, iso_y), 1, 0) 
        """ # debug purposes 
                                                                                # priority to the farm ( they are like grass so the ground is displayed first) then the normal deep sort 
        for current_entity in sorted(entity_to_display, key=lambda entity: (not(isinstance(entity, Farm)), entity.position.y + entity.position.x, entity.position.y)):
        
            current_entity.display(current_time, screen, camera, g_width, g_height)
        
        



        # minimap display 
        self.minimap.update_position(g_width, g_height)
        
        self.minimap.display_ground(screen)

        for current_region in self.entity_matrix.values():
            for entity_set in current_region.values():
                for entity in entity_set:
                    if not(isinstance(entity, Building)):
                        self.minimap.display_on_cart(screen, entity)
        
        self.minimap.display_camera(screen, top_X, top_Y, bottom_X, bottom_Y)

        

    def terminal_display(self, current_time, terminal_camera):

        if current_time - self.last_time_refershed >= ONE_SEC*(0.05):

            startX, startY, endX, endY = terminal_camera.indexes_in_point_of_view_terminal()

            # Clear the terminal screen for animation
            
            os.system('cls' if os.name == 'nt' else 'clear') # cls if windows clear if

            sys.stdout.write(f"[+] View Start: ({startX}, {startY}), View End: ({endX}, {endY})\n")
            endY -= 1 # we took a line for the display info

            for currentY in range(startY, endY + 1):
                current_string=""
                for currentX in range(startX, endX + 1):
                    if 0 <= currentX < self.nb_CellX and 0 <= currentY < self.nb_CellY:
                        REG_X, REG_Y = currentX // 5, currentY // 5

                        current_region = self.entity_matrix.get((REG_Y, REG_X))
                        if current_region:

                            current_entity_set = current_region.get((currentY, currentX))
                            if current_entity_set:

                                for current_entity in current_entity_set:
                                    current_string += current_entity.representation
                                    break
                            else:
                                current_string += "."
                        else:
                            current_string += "."
                    else:
                        current_string += " "
                        
                sys.stdout.write(current_string)
                
                sys.stdout.flush()
                   
            self.last_time_refershed = current_time
                                
        

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
                    if not(self.check_cell(tree_Y, tree_X)):
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
                    if not(self.check_cell(gold_Y, gold_X)):
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

            if not(self.check_cell(center_Y, center_X)) :
                town_center = TownCenter(center_Y, center_X, None, team=i + 1)
                self.add_entity(town_center)
                
                self._add_starting_resources(center_Y, center_X)
    
    def _add_starting_resources(self, center_Y, center_X):
        GEN_DIS_G = 2
        GEN_DIS_T = 1
        for offset_X, offset_Y in [(-GEN_DIS_G, GEN_DIS_G), (GEN_DIS_G, -GEN_DIS_G), (GEN_DIS_G, GEN_DIS_G)]:
            gold_X = center_X + offset_X
            gold_Y = center_Y + offset_Y
            if not(self.check_cell(gold_X, gold_Y)):
                
                gold = Gold(gold_Y, gold_X, None)
                self.add_entity(gold)

        for offset_X, offset_Y in [(GEN_DIS_T, GEN_DIS_T), (GEN_DIS_T, -GEN_DIS_T), (-GEN_DIS_T, GEN_DIS_T)]:
            tree_X = center_X + offset_X
            tree_Y = center_Y + offset_Y
            if not(self.check_cell(tree_Y, tree_Y)):  
                tree = Tree(tree_Y, tree_X, None)
                self.add_entity(tree)