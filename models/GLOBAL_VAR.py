import math
import random

INITIAL_ZOOM = 1
ZOOM_LEVELS = [1, 1.3, 1.6, 2, 2.3, 2.6, 3, 3.3]
TILE_SIZE_2ISO = 15
TILE_SIZE_2D = 40
ONE_SEC = 1000 # 1000 millisec
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800
MAP_CELLX = 120
MAP_CELLY = 120

#colors

BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
RED_COLOR = (255, 0, 0)
GREEN_COLOR = (0,255, 0)
BLUE_COLOR = (0, 0, 255)

TEAM_COLORS = {
    1: BLUE_COLOR,
    2: RED_COLOR,
    3:GREEN_COLOR
}
UNIT_IDLE = 0
UNIT_WALKING = 1
UNIT_ATTACKING = 2
UNIT_DYING = 3
UNIT_TASK = 4

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
from ImageProcessingDisplay.viewport import ViewPort
from ImageProcessingDisplay.camera import Camera

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

camera = Camera()
font = pygame.font.Font(None, 24)

GRASS= load_sprite("Sprites/grass.webp")

ARCHERYRANGE= load_sprite("Sprites/Building/archery_range.webp")
BARRACKS = load_sprite("Sprites/Building/barracks.webp")
CAMP = load_sprite("Sprites/Building/camp.webp")
KEEP = load_sprite("Sprites/Building/keep.webp")
TOWNCENTER = load_sprite("Sprites/Building/town_center_1.webp")
FARM = load_sprite("Sprites/Building/farm.webp")
GOLD_ARRAY_1D = load_single_sprites("Sprites/Resources/gold.webp",7)
TREES_ARRAY_1D = load_single_sprites("Sprites/Resources/trees.webp",42)
STABLE_ARRAY_1D = load_single_sprites("Sprites/Building/stable.webp", 27)
HOUSES_ARRAY_1D = load_single_sprites("Sprites/Building/houses.webp",3)
HORSEMAN_ARRAY_3D = state_load_sprite_sheet("Sprites/Unit/horseman")
ARCHER_ARRAY_3D = state_load_sprite_sheet("Sprites/Unit/archer")
SWORDMAN_ARRAY_3D = state_load_sprite_sheet("Sprites/Unit/swordman")
VILLAGER_ARRAY_3D = state_load_sprite_sheet("Sprites/Unit/villager")

ARROW_ARRAY_2D = load_sprite_sheet("Sprites/Projectile/arrow.webp",32, 11, skip_row = 2, limit_col = 1)

META_SPRITES = {
    'G': {zoom: resize(GRASS,camera.img_scale * zoom) for zoom in ZOOM_LEVELS},
    'A': {zoom: resize(ARCHERYRANGE,camera.img_scale * zoom) for zoom in ZOOM_LEVELS},
    'C': {zoom: resize(CAMP, camera.img_scale *zoom) for zoom in ZOOM_LEVELS},
    'K': {zoom: resize(KEEP, camera.img_scale *zoom) for zoom in ZOOM_LEVELS},
    'T': {zoom: resize(TOWNCENTER, camera.img_scale *zoom) for zoom in ZOOM_LEVELS},
    'F': {zoom: resize(FARM,camera.img_scale * zoom) for zoom in ZOOM_LEVELS},
    'g': {zoom: resize(GOLD_ARRAY_1D, camera.img_scale *zoom) for zoom in ZOOM_LEVELS},
    'w': {zoom: resize(TREES_ARRAY_1D,camera.img_scale * zoom) for zoom in ZOOM_LEVELS},
    'S': {zoom: resize(STABLE_ARRAY_1D,camera.img_scale * zoom) for zoom in ZOOM_LEVELS},
    'H': {zoom: resize(HOUSES_ARRAY_1D, camera.img_scale *zoom) for zoom in ZOOM_LEVELS},
    'h': {zoom: resize(HORSEMAN_ARRAY_3D, camera.img_scale *zoom) for zoom in ZOOM_LEVELS},
    'a': {zoom: resize(ARCHER_ARRAY_3D,camera.img_scale * zoom) for zoom in ZOOM_LEVELS},
    's': {zoom: resize(SWORDMAN_ARRAY_3D, camera.img_scale *zoom) for zoom in ZOOM_LEVELS},
    'v': {zoom: resize(VILLAGER_ARRAY_3D, camera.img_scale *zoom) for zoom in ZOOM_LEVELS},
    'p': {zoom: resize(ARROW_ARRAY_2D, camera.img_scale *zoom) for zoom in ZOOM_LEVELS}
}







CURSOR_IMG = pygame.image.load("Sprites/cursor.png").convert_alpha()