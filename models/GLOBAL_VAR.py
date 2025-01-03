import math
import random
import os
import sys
import json

INITIAL_ZOOM = 1
MIN_ZOOM = 1
MAX_ZOOM = 7
TILE_SIZE_2ISO = 15
TILE_SIZE_2D = 40

ONE_SEC = 1000 # 1000 millisec
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
MAP_CELLX = 120
MAP_CELLY = 120
REGION_DIVISION = 5

MINIMAP_WIDTH = 220
MINIMAP_HEIGHT = MINIMAP_WIDTH
#colors
FPS = 240
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0,255, 0)
BLUE_COLOR = (0, 0, 255)

GOLD_COLOR = (255, 215, 0) 
BROWN_TREE_COLOR = (139, 69, 19)
MINIMAP_COLOR = (53, 94, 59)

TEAM_COLORS = {
    0: WHITE_COLOR, # white is for no one ( for all teams )
    1: BLUE_COLOR,
    2: RED_COLOR,
    3:GREEN_COLOR
    # ....
}

LEFT_CLICK = 1 
RIGHT_CLICK = 3 
#state

START = 0
PLAY = 1
PAUSE = 2


#map

MAP_NORMAL = 0
MAP_CENTERED = 1

#mode

LEAN = 0
MEAN = 1
MARINES = 2

#smart way for generation
MODE_GENERATION = {
    LEAN:{
        "resources":{"gold":50, "wood":200, "food":50},
        "entities":{
            "T":1,
            "v":3
        }

    },
    MEAN:{
        "resources":{"gold":2000, "wood":2000, "food":2000},
        "entities":{
            "T":1,
            "v":3
        }
    },
    MARINES:{
        "resources":{"gold":20000, "wood":20000, "food":20000},
        "entities":{
            "T":3,
            "v":15,
            "B":2,
            "S":2,
            "A":2
        }
    }
}

#display
TERMINAL = 0
ISO2D = 1

UNIT_IDLE = 0
UNIT_WALKING = 1
UNIT_ATTACKING = 2
UNIT_DYING = 3
UNIT_TASK = 4

BUILDING_INPROGRESS= 0
BUILDING_ACTIVE = 1
BUILDING_DYING = 2

TREE_CAPACITY = 100
GOLD_CAPACITY = 800
FARM_CAPACITY = 300

CAMP_MAX_HP = 200
FARM_MAX_HP = 100
HOUSE_MAX_HP = 100
KEEP_MAX_HP = 800 
STABLE_MAX_HP = 500 
TOWNCENTER_MAX_HP= 1000
ARCHERYRANGE_MAX_HP = 500
BARRACKS_MAX_HP = 500

ARCHER_MAX_HP= 30
HOSREMAN_MAX_HP = 45
SOWRDMAN_MAX_HP = 40
VILLAGER_MAX_HP = 25

BARBOX_WIDTH = 10
BARBOX_HEIGHT = 5
from pvector2 import *
from ImageProcessingDisplay.imagemethods import * 


UNIT_ANGLE_MAPPING = {
    0*math.pi/8:6,
    1*math.pi/8:5,
    2*math.pi/8:4,
    3*math.pi/8:3,
    4*math.pi/8:2,
    5*math.pi/8:1,
    6*math.pi/8:0,
    7*math.pi/8:15,
    8*math.pi/8:14,
    9*math.pi/8:13,
    10*math.pi/8:12,
    11*math.pi/8:11,
    12*math.pi/8:10,
    13*math.pi/8:9,
    14*math.pi/8:8,
    15*math.pi/8:7
}

PROJECTILE_ANGLE_MAPPING ={
    0*math.pi/8:6,
    1*math.pi/8:5,
    2*math.pi/8:4,
    3*math.pi/8:3,
    4*math.pi/8:2,
    5*math.pi/8:1,
    6*math.pi/8:0,
    7*math.pi/8:15,
    8*math.pi/8:14,
    9*math.pi/8:13,
    10*math.pi/8:12,
    11*math.pi/8:11,
    12*math.pi/8:10,
    13*math.pi/8:9,
    14*math.pi/8:8,
    15*math.pi/8:7
}

def MAP_ANGLE_INDEX(angle, angle_map):
    animation_index =0
    shortest_distance = 10 # big enoug so difference between two angle will never be that big

    for angle_key in angle_map.keys():
        current_distance = abs(angle - angle_key)
        if current_distance <= shortest_distance:
            shortest_distance = current_distance
            animation_index = angle_map.get(angle_key)

    return animation_index
 

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
pygame.display.set_caption("AOE2")


"""  DONT DELETE THIS SECTION !!!, WE MAY USE IT LATER 
GRASS= load_sprite("Sprites/grass.webp")
g =resize_sprite(GRASS, camera.img_scale*50)
g_w, g_h = g.get_size()

# Convert 2D grid coordinates to isometric coordinates
def convert_iso(x, y):
    iso_x = (y - x) * (TILE_SIZE_2ISO*50) + 6 * g_w//2
    iso_y = ((y + x)/2) * (TILE_SIZE_2ISO*50) + g_h//2
    return iso_x, iso_y

# Adjust region surface size to accommodate isometric layout
region_surface_width = 6 * g_w
region_surface_height = 6 * g_h
region_surface = pygame.Surface((region_surface_width, region_surface_height), pygame.SRCALPHA)

# Fill the region surface with GRASS tiles
for y in range(5):
    for x in range(5):
        iso_x, iso_y = convert_iso(x, y)
        # Adjust for center alignment on the region surface
        region_surface.blit(g, (iso_x - g_w // 2, iso_y - g_h // 2))
region_surface = resize_sprite(region_surface, 1/(camera.img_scale*50))
# Save the surface as an image
pygame.image.save(region_surface, "region.png")
"""
GRASS = load_sprite("Sprites/region.webp")

ARCHERYRANGE_ARRAY_3D= state_load_sprite_sheet("Sprites/Building/archeryrange")
BARRACKS_ARRAY_3D = state_load_sprite_sheet("Sprites/Building/barracks")
CAMP_ARRAY_3D = state_load_sprite_sheet("Sprites/Building/camp")
KEEP_ARRAY_3D = state_load_sprite_sheet("Sprites/Building/keep")
STABLE_ARRAY_3D = state_load_sprite_sheet("Sprites/Building/stable")
HOUSES_ARRAY_3D = state_load_sprite_sheet("Sprites/Building/house")
TOWNCENTER_ARRAY_3D = state_load_sprite_sheet("Sprites/Building/towncenter")
FARM_ARRAY_3D = state_load_sprite_sheet("Sprites/Building/farm")

GOLD_ARRAY_1D = load_single_sprites("Sprites/Resources/gold.webp",7)
TREES_ARRAY_1D = load_single_sprites("Sprites/Resources/trees.webp",42)



HORSEMAN_ARRAY_3D = state_load_sprite_sheet("Sprites/Unit/horseman")
ARCHER_ARRAY_3D = state_load_sprite_sheet("Sprites/Unit/archer")
SWORDMAN_ARRAY_3D = state_load_sprite_sheet("Sprites/Unit/swordman")
VILLAGER_ARRAY_3D = state_load_sprite_sheet("Sprites/Unit/villager")

ARROW_ARRAY_2D = load_sprite_sheet("Sprites/Projectile/arrow.webp",32, 11, skip_row = 2, limit_col = 1)

SPRITES = {
    'g': GRASS,
    'A': ARCHERYRANGE_ARRAY_3D,
    'B': BARRACKS_ARRAY_3D,
    'C': CAMP_ARRAY_3D,
    'K': KEEP_ARRAY_3D,
    'T': TOWNCENTER_ARRAY_3D,
    'F': FARM_ARRAY_3D,
    'G': GOLD_ARRAY_1D,
    'W': TREES_ARRAY_1D,
    'S': STABLE_ARRAY_3D,
    'H': HOUSES_ARRAY_3D,
    'h': HORSEMAN_ARRAY_3D,
    'a': ARCHER_ARRAY_3D,
    's': SWORDMAN_ARRAY_3D,
    'v': VILLAGER_ARRAY_3D,
    'na': ARROW_ARRAY_2D
}

UNIT_SATES = {
    "dying": UNIT_DYING
}
BUILDING_STATES = {
    "dying": BUILDING_DYING
}

STATES = {
    'A': BUILDING_STATES,
    'B': BUILDING_STATES,
    'C': BUILDING_STATES,
    'K': BUILDING_STATES,
    'T': BUILDING_STATES,
    'F': BUILDING_STATES,
    'S': BUILDING_STATES,
    'H': BUILDING_STATES,
    'h': UNIT_SATES,
    'a': UNIT_SATES,
    's': UNIT_SATES,
    'v': UNIT_SATES
}

WATER_MARK_SKIP = {
    "A":[(2,0,10), (2,0,15)],
    "B":[(2,0,20), (2,0,18)],
    "C":[(2,0,20), (2,0,17)],
    "H":[(2,0,7), (2,2,17)],
    "K":[(2,0,4), (2,0,16)],
    "S":[(2,0,20), (2,0,18)],
    "T":[(2,0,4), (2,0,16)]
}
META_SPRITES_CACHE ={}

def META_SPRITES_CACHE_HANDLE(zoom_level, list_keys, camera): # returns image to display

    global META_SPRITES_CACHE

    #print(f"zoom:{zoom_level}, keys:{list_keys}")
    current_dict = META_SPRITES_CACHE.get(zoom_level, None)

    if (current_dict == None):
        META_SPRITES_CACHE[zoom_level] = {}
        current_dict = META_SPRITES_CACHE.get(zoom_level, None)

    parallele_dict = SPRITES

    keys_len = len(list_keys)

    for key in range(keys_len):
        parallele_dict = parallele_dict.get(list_keys[key], None)
        tmp_dict = current_dict.get(list_keys[key], None)

        if (tmp_dict != None):
            current_dict = tmp_dict
            continue 
        
        if (key < keys_len - 1):
            current_dict[list_keys[key]] = {}
            current_dict = current_dict.get(list_keys[key], None)
        else:
            current_dict[list_keys[key]] = resize(parallele_dict, zoom_level * camera.img_scale)
            current_dict = current_dict.get(list_keys[key], None)
        
    return current_dict 
        
    
CURSOR_IMG = pygame.image.load("Sprites/cursor.png").convert_alpha()
MINIMAP_IMG = pygame.image.load("Sprites/minimap_cus.png").convert_alpha()
MINIMAP_IMG = adjust_sprite(MINIMAP_IMG, MINIMAP_WIDTH*(2 + 0.2), MINIMAP_HEIGHT/2 *(2 + 0.2))

#Resources
GOLD_ICON = pygame.image.load("Icons/Resources/Aoe2de_gold.png").convert_alpha()
WOOD_ICON = pygame.image.load("Icons/Resources/Aoe2de_wood.png").convert_alpha()
FOOD_ICON = pygame.image.load("Icons/Resources/Aoe2de_food.png").convert_alpha()

#Bulding
ARCHERY_RANGE_ICON = pygame.image.load("Icons/Building/Archery_range_aoe2DE.png").convert_alpha()
BARRACKS_ICON = pygame.image.load("Icons/Building/Barracks_aoe2DE.png").convert_alpha()
FARM_ICON = pygame.image.load("Icons/Building/FarmDE.png").convert_alpha()
HOUSE_ICON = pygame.image.load("Icons/Building/House_aoe2DE.png").convert_alpha()
KEEP_ICON = pygame.image.load("Icons/Building/Keep_icon_AoE2DE.png").convert_alpha()
CAMP_ICON = pygame.image.load("Icons/Building/Lumber_camp_aoe2de.png").convert_alpha()
STABLE_ICON = pygame.image.load("Icons/Building/Stable_aoe2DE.png").convert_alpha()
TOWNCENTRE_ICON = pygame.image.load("Icons/Building/Towncenter_aoe2DE.png").convert_alpha()

#Unit
ARCHER_ICON = pygame.image.load("Icons/Unit/Archer_aoe2DE.png").convert_alpha()
HORSEMAN_ICON = pygame.image.load("Icons/Unit/Knight_aoe2DE.png").convert_alpha()
SWORDSMAN_ICON = pygame.image.load("Icons/Unit/Longswordsman_aoe2DE.png").convert_alpha()
VILLAGER_ICON = pygame.image.load("Icons/Unit/MaleVillDE.png").convert_alpha()

ICONS = {
    "Gi":GOLD_ICON,
    "Wi":WOOD_ICON,
    "Mi":FOOD_ICON,
    "Ai":ARCHERY_RANGE_ICON,
    "Bi":BARRACKS_ICON,
    "Fi":FARM_ICON,
    "Hi":HOUSE_ICON,
    "Ki":KEEP_ICON,
    "Ci":CAMP_ICON,
    "Si":STABLE_ICON,
    "Ti":TOWNCENTRE_ICON,
    "ai":ARCHER_ICON,
    "hi":HORSEMAN_ICON,
    "si":SWORDSMAN_ICON,
    "vi":VILLAGER_ICON
}

ICON_WIDTH, ICON_HEIGHT =  3*TILE_SIZE_2ISO, 3*TILE_SIZE_2ISO

for key in ICONS:
    ICONS[key] = adjust_sprite(ICONS[key], ICON_WIDTH, ICON_HEIGHT)


SPRITES = SPRITES | ICONS