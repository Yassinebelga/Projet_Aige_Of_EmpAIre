import pygame

from ImageProcessingDisplay import UserInterface
from GLOBAL_VAR import *

class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("AIge Of Empaire II")
        self.clock = pygame.time.Clock()
        from Game import GameState
        self.state = GameState(self.screen)

    def run(self):
        running = True
        while running:
            SCREEN_WIDTH, SCREEN_HEIGHT = self.state.screen.get_width(), self.state.screen.get_height()
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if self.state.states == START:
                    if event.type == pygame.MOUSEBUTTONDOWN and self.state.menu.handle_click(event.pos):
                        # Mise à jour des paramètres du jeu en quittant le menu
                        self.state.set_map_type(self.state.menu.map_options[self.state.menu.selected_map_index])
                        self.state.set_difficulty_mode(self.state.menu.selected_mode_index)
                        self.state.set_display_mode(self.state.menu.display_mode)
                        self.state.start_game()
                        self.state.states = PLAY

            # Gestion des touches pressées pendant la partie
            keys = pygame.key.get_pressed()
            if not (self.state.states == START):
                # Zoom de la caméra
                if keys[pygame.K_KP_PLUS]:  # Touche + du pavé numérique
                    self.state.camera.adjust_zoom(pygame.time.get_ticks(), 0.1)
                elif keys[pygame.K_KP_MINUS]:  # Touche - du pavé numérique
                    self.state.camera.adjust_zoom(pygame.time.get_ticks(), -0.1)

                # Basculer le mode d'affichage
                if keys[pygame.K_t]:
                    self.state.toggle_display_mode()
                # Pause
                if keys[pygame.K_p]:
                    self.state.toggle_pause()
                # Mouvement de la caméra
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    scale = 2
                else:
                    scale = 1
                if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
                    self.state.camera.view_port.position.x -= 10 * scale
                if keys[pygame.K_LEFT] or keys[pygame.K_q] :
                    self.state.camera.view_port.position.x += 10 * scale
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.state.camera.view_port.position.y -= 10 * scale
                if keys[pygame.K_UP] or keys[pygame.K_z]:
                    self.state.camera.view_port.position.y += 10 * scale

            # Mettre à jour l'état du jeu
            if not (self.state.states == PAUSE):
                self.state.update()

            # Effacer l'écran avant de dessiner
            self.screen.fill((0, 0, 0))
            if self.state.states == START:
                self.state.menu.draw()
            else:
                self.state.map.display(self.clock, self.state.screen, self.state.camera, SCREEN_WIDTH, SCREEN_HEIGHT)

            # Rafraîchissement de l'affichage
            pygame.display.flip()
            self.clock.tick(500)

        pygame.quit()


if __name__ == "__main__":
    game = GameLoop()
    game.run()
