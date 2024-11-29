from GLOBAL_VAR import *

class Camera:
    def __init__(self, position = PVector2(0,0), _tile_size_2iso = TILE_SIZE_2ISO, _tile_size_2d = TILE_SIZE_2D, max_zoom = MAX_ZOOM): 

        self.zoom = INITIAL_ZOOM 
        
        self.cell_X = 0
        self.cell_Y = 0
        self.tile_size_2d = _tile_size_2d
        self.tile_size_2iso = _tile_size_2iso #display size
        self.img_scale = _tile_size_2iso/50 # img_scale is a value to scale the loaded images so the tiles are aligned, 50 is the choosen value after many tries
        
        self.max_zoom = MAX_ZOOM
        self.last_time_adjusted_zoom = pygame.time.get_ticks()
        self.num_zoom_per_sec = 3
        
        self.view_port = ViewPort(position,SCREEN_WIDTH, SCREEN_HEIGHT)

    def convert_to_isometric_2d(self, x, y): #convert (x,y) cooridnates to iso_x iso_y

        iso_x = int((y - x)*(self.tile_size_2iso/self.tile_size_2d) * (self.zoom + 1) + self.view_port.position.x * (self.zoom + 1))
        iso_y = int(((y + x)/2)*(self.tile_size_2iso/self.tile_size_2d) * (self.zoom + 1) + self.view_port.position.y * (self.zoom + 1))

        return iso_x, iso_y

    def convert_from_isometric_2d(self, iso_x, iso_y):

        x_p = (iso_x/(self.zoom + 1) - self.view_port.position.x )*(self.tile_size_2d/self.tile_size_2iso)
        y_p = (iso_y/(self.zoom + 1) - self.view_port.position.y )*(self.tile_size_2d/self.tile_size_2iso)

        x = (2*y_p - x_p)/2
        y = (2*y_p + x_p)/2

        return x, y

    def convert_to_isometric_3d(self, x, y, z): #convert (x,y,z) projectile cooridnates to iso_x iso_y
        iso_x = int((y - x)*(self.tile_size_2iso/self.tile_size_2d) * (self.zoom + 1) + self.view_port.position.x * (self.zoom + 1))
        iso_y = int(((y + x - z)/2)*(self.tile_size_2iso/self.tile_size_2d) * (self.zoom + 1) + self.view_port.position.y * (self.zoom + 1))
        
        return iso_x, iso_y 

    def indexes_in_point_of_view(self,nb_CellY, nb_CellX, g_width = None, g_height = None, corner_x = 0,corner_y = 0,ext_x =0, ext_y = 0):
        
        vp_x = corner_x
        vp_y = corner_y

        if g_width and g_height:
            height = g_height
            width = g_width
        else:
            height = corner_y
            width = corner_x

        topleft_x, topleft_y = self.convert_from_isometric_2d(vp_x, vp_y) #gives us starting y
        bottomright_x, bottomright_y= self.convert_from_isometric_2d(vp_x + width, vp_y + height) #gives us ending y

        topright_x, topright_y = self.convert_from_isometric_2d(vp_x + width, vp_y) #gives usstarting x
        bottomleft_x, bottomleft_y= self.convert_from_isometric_2d(vp_x, vp_y + height)#gives us ending x


        start_X = round(max(0,topright_x/(self.tile_size_2d ) - 1))
        start_Y = round(max(0,topleft_y/(self.tile_size_2d ) - 1))
        end_X = round(min(bottomleft_x/(self.tile_size_2d ) + 1, nb_CellX - 1))
        end_Y = round(min(bottomright_y/(self.tile_size_2d ) + 1, nb_CellY - 1))
        
        #print(f"startX = {start_X} startY = {start_Y} , endX = {end_X} endY = {end_Y}")
        return start_X, start_Y, end_X, end_Y

    def check_in_point_of_view(self, x_to_check, y_to_check, g_width , g_height):
        if (-TILE_SIZE_2ISO * (self.zoom + 1) * 3 < x_to_check and x_to_check<g_width + TILE_SIZE_2ISO * (self.zoom + 1)* 3  and -TILE_SIZE_2ISO * (self.zoom + 1)* 3 <y_to_check and y_to_check < g_height + TILE_SIZE_2ISO * (self.zoom + 1)* 3 ):
            return True

    def adjust_zoom(self, amount):
        
        if pygame.time.get_ticks() - self.last_time_adjusted_zoom > ONE_SEC / self.num_zoom_per_sec :
            self.last_time_adjusted_zoom = pygame.time.get_ticks()
            self.zoom = max(0, min(self.max_zoom - 1, self.zoom + amount))  # Clamp zoom between 0 and max_zoom

    def draw_box(self, screen, _entity):
        topleft_x, topleft_y = _entity.position.x - _entity.box_size, _entity.position.y - _entity.box_size
        topright_x, topright_y = _entity.position.x + _entity.box_size, _entity.position.y - _entity.box_size

        bottomleft_x, bottomleft_y = _entity.position.x - _entity.box_size, _entity.position.y + _entity.box_size
        bottomright_x, bottomright_y = _entity.position.x + _entity.box_size, _entity.position.y + _entity.box_size

        d_topleft_x, d_topleft_y = self.convert_to_isometric_2d(topleft_x, topleft_y)
        d_topright_x, d_topright_y = self.convert_to_isometric_2d(topright_x, topright_y)

        d_bottomleft_x, d_bottomleft_y = self.convert_to_isometric_2d(bottomleft_x, bottomleft_y)
        d_bottomright_x, d_bottomright_y = self.convert_to_isometric_2d(bottomright_x, bottomright_y)

        pygame.draw.polygon(screen, (255, 255, 255), [(d_topleft_x, d_topleft_y),(d_topright_x, d_topright_y),(d_bottomright_x, d_bottomright_y),(d_bottomleft_x, d_bottomleft_y)], 1)

