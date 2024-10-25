from models.map import Map
import pygame
from pygame.locals import *



pygame.init()

fenetre = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()


continuer = True
while continuer :
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    current_time = pygame.time.get_ticks()

    # pygame.display.update()

pygame.quit()
def main():
    pass
