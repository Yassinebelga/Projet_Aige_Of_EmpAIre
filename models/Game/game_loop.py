import pygame
from game.game_state import GameState
from game.user_interface import UserInterface

class GameLoop:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Strategy Game")
        self.clock = pygame.time.Clock()
        self.state = GameState()
        self.ui = UserInterface(self.screen)
        self.in_menu = True  # Commence dans le menu principal

    def run(self):
        running = True
        while running:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if self.in_menu:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                        self.state.toggle_pause()
                    elif event.type == pygame.MOUSEBUTTONDOWN and self.ui.handle_click(event.pos):
                        # Mise à jour des paramètres du jeu en quittant le menu
                        self.state.set_map_type(self.ui.map_options[self.ui.selected_map_index])
                        self.state.set_difficulty_mode(self.ui.selected_mode_index)
                        self.state.set_display_mode(self.ui.display_mode)
                        self.state.start_game()
                        self.in_menu = False

            # Gestion des touches pressées pendant la partie
            keys = pygame.key.get_pressed()
            if not self.in_menu:
                # Zoom de la caméra
                if keys[pygame.K_KP_PLUS]:  # Touche + du pavé numérique
                    self.state.zoom_in()
                elif keys[pygame.K_KP_MINUS]:  # Touche - du pavé numérique
                    self.state.zoom_out()

                # Basculer le mode d'affichage
                if keys[pygame.K_t]:
                    self.state.toggle_display_mode()
                # Pause
                if keys[pygame.K_p]:
                    self.state.toggle_pause()
                # Mouvement de la caméra
                camera_dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] or keys[pygame.K_d] - keys[pygame.K_q]
                camera_dy = keys[pygame.K_DOWN] - keys[pygame.K_UP] or keys[pygame.K_s] - keys[pygame.K_z]
                if camera_dx or camera_dy:
                    self.state.move_camera(camera_dx, camera_dy, self.screen)

            # Mettre à jour l'état du jeu
            if not self.state.is_paused:
                self.state.update()

            # Effacer l'écran avant de dessiner
            self.screen.fill((0, 0, 0))
            if self.in_menu:
                self.ui.draw()
            else:
                self.state.draw(self.screen)

            # Rafraîchissement de l'affichage
            pygame.display.flip()
            self.clock.tick(500)

        pygame.quit()


if __name__ == "__main__":
    game = GameLoop()
    game.run()
