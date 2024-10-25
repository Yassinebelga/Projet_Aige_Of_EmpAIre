from models.map import Map
import pygame
from pygame.locals import *



pygame.init()

fenetre = pygame.display.set_mode((640, 480))

# instancion d'un objet Clock pour utiliser le temps dans nos divers contraintes
clock = pygame.time.Clock()

# création d'un tableau pour stocké le temps de chaque évènement
event_times = []
FPS = 60 # initlisation du nombre de FPS/de tick de Clock par seconde
previous_time = pygame.time.get_ticks()

continuer = True
while continuer :
    current_time = pygame.time.get_ticks()
    delta_time = (current_time-previous_time) / 10000.0 # initalisation d'un temps delta qui va gérer des évènements spécifiques comme la vitesse de déplacement des unités ou la vitesse de construction des bâtiments 
    previous_time = current_time
    for event in pygame.event.get():
        event_time = pygame.time.get_ticks()
        event_times.append(event_time) 
        if event.type == QUIT:
            continuer = False


    # Mise à jour du jeux 

    clock.tick(FPS) # limite du nombre de tick par second à FPS = 60 par seconde, donc le jeux va être mis à jour (déplcaement des unités, découverte et affichage de la carte, découverte et affichage des batiments) 60 fois par seconde

    # pygame.display.update()

pygame.quit()
def main():
    pass
