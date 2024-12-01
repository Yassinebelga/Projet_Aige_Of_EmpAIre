import pygame
import pygame.gfxdraw
import math
from GLOBAL_VAR import *
def resize_sprite(image, scale):
    width, height = image.get_size()
    return pygame.transform.smoothscale(image, (int(width * scale), int(height * scale)))

def load_sprite_sheet(sprite_sheet, num_row, num_col, scale,skip_row = 1, limit_col = 1):
    sheet_width, sheet_height = sprite_sheet.get_size()

    frame_width = sheet_width // num_col
    frame_height = sheet_height // num_row
    
    img_array = []
    
    for row in range(0,num_row,skip_row): #  to skip unwanted angles ( in aoe2 sprites are in 16 angles, but to simplify the complexite in memory, we will use 8 )
        angle_frames = []
        for col in range(int(num_col/limit_col)):
            x = col * frame_width
            y = row * frame_height

            frame_image = sprite_sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))
            frame_image = resize_sprite(frame_image, scale)

            angle_frames.append(frame_image)

        img_array.append(angle_frames)
    
    return img_array

def zoomlevels_load_sprite_sheet(path, num_row, num_col, camera, skip_row = 1, limit_col = 1): # for each zoom level return the 2d array of images
    print(f"[::] Loading images from {path}")
    sprite_sheet = pygame.image.load(path).convert_alpha()
    zoomlevels_3d_array = [load_sprite_sheet(sprite_sheet, num_row, num_col, (i + 1) * camera.img_scale, skip_row, limit_col) for i in range(camera.max_zoom)]
    print(f"[+] Success")
    return zoomlevels_3d_array


def state_zoomlevels_load_sprite_sheet(path, camera): # define for each state ( attacking, walking ...) the 3d of zoom levels of the 2d array of images

    state_zoomlevels_4d_array = []

    with open(path+"/size_each.txt", "r") as file: # get the size of array for each animation
        content = file.read()
    content = content.split("\n")
    image_range = int(content[0])
    content = content[1:len(content) - 1]   # in size_each there is info about how the state and sprites are organized
    for i in range(len(content)):
        content[i] = content[i].split(",")
        row = content[i][0]
        col = content[i][1] 
        content[i][0] = int(row)
        content[i][1] = int(col)

    for image_index in range(image_range):
        current_row, current_col = content[image_index]
        state_zoomlevels_4d_array.append(zoomlevels_load_sprite_sheet(path+"/img_"+str(image_index)+".webp",current_row,current_col,camera))


    return state_zoomlevels_4d_array # for animated entites


def load_single_sprites(image, col_num, scale=1):  
    image_width, image_height = image.get_width(), image.get_height()
    
    sprite_width = image_width // col_num
    sprite_height = image_height  # Assumes sprites are vertically aligned

    sprites = []
    
    for col in range(col_num):
        # Extract the sub-surface for each sprite
        rect = pygame.Rect(col * sprite_width, 0, sprite_width, sprite_height)
        sprite = image.subsurface(rect).copy()
        
        # Scale the sprite if needed
        sprite = resize_sprite(sprite, scale)
        sprites.append(sprite)

    return sprites

def zoomlevels_load_single_sprites(path, num_col, camera):
    print(f"[::] Loading images form {path}")
    sprite = pygame.image.load(path).convert_alpha()
    zoomlevels_2d_array = [load_single_sprites(sprite, num_col, (i + 1)*camera.img_scale) for i in range(camera.max_zoom)]
    print(f"[+] Success")

    return zoomlevels_2d_array

def zoomlevels_sprite(path, camera): # different scaled for each zoom level
    print(f"[::] Loading images from {path}")
    sprite = pygame.image.load(path).convert_alpha()
    zoomlevels_1d_array = [resize_sprite(sprite, (i + 1) * camera.img_scale) for i in range(camera.max_zoom)] 
    print(f"[+] Success")
    return zoomlevels_1d_array # for static entities

def display_image(image, x, y, screen, flags=0x00, team = 0, glow_radius = 3): # flags to display in the center or the top left
    im_width, im_height = image.get_size()

    # Calculate final position based on flags
    if flags == 0x04:
        final_x, final_y = x - im_width // 2, y - im_height // 2
    else:
        final_x, final_y = x, y
        
    
    # Blit the main image onto the screen
    screen.blit(image, (final_x, final_y))

def draw_rectangle_with_borders(screen, topleftx, toplefty, bottomrightx, bottomrighty, color=(255, 255, 255), border_thickness=1):
    width = abs(bottomrightx - topleftx)
    height = abs(bottomrighty - toplefty)
    topleftx = min(topleftx,bottomrightx)
    toplefty = min(toplefty, bottomrighty)
    # Create a rectangle object
    rect = pygame.Rect(topleftx, toplefty, width, height)
    # Draw the rectangle's border
    pygame.draw.rect(screen, color, rect, border_thickness)

def draw_percentage_bar(screen,camera, iso_x, iso_y, _current , _max, sq_size, color = (255, 0, 0)):

    factor = (camera.zoom + 1)*max(1,sq_size/1.5)
    topleftx = iso_x - factor*BARBOX_WIDTH//2
    toplefty = iso_y - BARBOX_HEIGHT//2

    percentage = _current/_max
    
    current_bar = pygame.Rect(topleftx, toplefty, factor*BARBOX_WIDTH * percentage, BARBOX_HEIGHT)
    max_bar = pygame.Rect(topleftx, toplefty, factor*BARBOX_WIDTH, BARBOX_HEIGHT)

    pygame.draw.rect(screen, color, current_bar)
    pygame.draw.rect(screen, (0, 0, 0), max_bar, 2)

