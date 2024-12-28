import pygame
from GLOBAL_VAR import *

class UserInterface:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)
        self.display_resources = False
        self.display_units = False
        self.display_builds = False

    def draw_resources(self, entity_matrix):
        player_1_data = {
            'Food': 500,  # Ressources alimentaires
            'Wood': 300,  # Ressources bois
            'Gold': 150,  # Ressources or
            'Units': {
                'Villagers': 10,  # Nombre de villageois
                'Soldiers': 5     # Nombre de soldats
            },
            'Builds': 3  # Nombre de bâtiments construits
        }

        player_2_data = {
            'Food': 450,  # Ressources alimentaires
            'Wood': 350,  # Ressources bois
            'Gold': 200,  # Ressources or
            'Units': {
                'Villagers': 8,   # Nombre de villageois
                'Soldiers': 7     # Nombre de soldats
            },
            'Builds': 4  # Nombre de bâtiments construits
        }
        # Position des joueurs
        player_1_pos = (10, 10)
        player_2_pos = (self.screen.get_width()//2, 10)

        # Y offsets distincts pour chaque joueur
        y_offset_player_1 = 0
        y_offset_player_2 = 0
        
        # Affichage des données des joueurs
        if self.display_resources:
            resources = f"Player 1 - Food: {player_1_data['Food']} | Wood: {player_1_data['Wood']} | Gold: {player_1_data['Gold']}"
            text = self.font.render(resources, True, WHITE_COLOR)
            self.screen.blit(text, (player_1_pos[0], player_1_pos[1] + y_offset_player_1))
            y_offset_player_1 += 20

        if self.display_units:
            units = f"Units - Villagers: {player_1_data['Units']['Villagers']} | Soldiers: {player_1_data['Units']['Soldiers']}"
            text = self.font.render(units, True, WHITE_COLOR)
            self.screen.blit(text, (player_1_pos[0], player_1_pos[1] + y_offset_player_1))
            y_offset_player_1 += 20

        if self.display_builds:
            builds = f"Builds: {player_1_data['Builds']}"
            text = self.font.render(builds, True, WHITE_COLOR)
            self.screen.blit(text, (player_1_pos[0], player_1_pos[1] + y_offset_player_1))
            y_offset_player_1 += 20

        # Affichage des données pour Player 2
        if self.display_resources:
            resources = f"Player 2 - Food: {player_2_data['Food']} | Wood: {player_2_data['Wood']} | Gold: {player_2_data['Gold']}"
            text = self.font.render(resources, True, WHITE_COLOR)
            self.screen.blit(text, (player_2_pos[0], player_2_pos[1] + y_offset_player_2))
            y_offset_player_2 += 20

        if self.display_units:
            units = f"Units - Villagers: {player_2_data['Units']['Villagers']} | Soldiers: {player_2_data['Units']['Soldiers']}"
            text = self.font.render(units, True, WHITE_COLOR)
            self.screen.blit(text, (player_2_pos[0], player_2_pos[1] + y_offset_player_2))
            y_offset_player_2 += 20

        if self.display_builds:
            builds = f"Builds: {player_2_data['Builds']}"
            text = self.font.render(builds, True, WHITE_COLOR)
            self.screen.blit(text, (player_2_pos[0], player_2_pos[1] + y_offset_player_2))
            y_offset_player_2 += 20

    def toggle_resources(self):
        self.display_resources = not self.display_resources

    def toggle_units(self):
        self.display_units = not self.display_units
    def toggle_builds(self):
        self.display_builds = not self.display_builds
    
    def toggle_all(self):
        self.display_resources = not self.display_resources
        self.display_units = not self.display_units
        self.display_builds = not self.display_builds