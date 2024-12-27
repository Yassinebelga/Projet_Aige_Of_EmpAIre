import pygame

from ImageProcessingDisplay import UserInterface
from GLOBAL_VAR import *
from Game.game_state import *

def generate_html_file():
    with open("Game/test_html_2.html", "r") as template_file:
        html_content = template_file.read()
    
    buildings_positions = [(1, 2), (3, 4)]
    building_list_html = ""
    for i, position in enumerate(buildings_positions, start=1):  # Utiliser enumerate pour avoir un index
        building_list_html += f"""<li class="building">Building {i} : {position}</li>"""

    unit_list_html = ""
    for i in range(1,3):
        unit_list_html += f'<li class="unit">Villager {i} : {i}, {i+1}</li>'
    # unit_list_html = ""
    # for unit in units:
    #     unit_list_html+=f'<li class="unit" > {unit.get_x()}, {unit.get_y()}'
    
    # Replace the placeholder in the template with the actual building list
    html_content = html_content.replace("{{BUILDINGS}}", building_list_html)
    html_content = html_content.replace("{{UNITS}}", unit_list_html)

    # Write the modified HTML content to a new file
    with open("game_map.html", "w") as output_file:
        output_file.write(html_content)

class GameLoop:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_caption("Age Of Empaire II")

        pygame.mouse.set_visible(False)

        self.font = pygame.font.Font(None, 24)

        self.clock = pygame.time.Clock()

        
        self.state = GameState(self.screen)

    def run(self):
        
        horse = Archer(5, 5, PVector2(0, 0), 1) # debugging
        target_pos = PVector2(0,0)
        self.state.map.add_entity(horse)

        running = True
        while running:
            move_flags = 0

            mouse_x, mouse_y = pygame.mouse.get_pos()

            current_time = pygame.time.get_ticks()
            
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
                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.state.mouse_held = True
                        
                        x, y = self.state.camera.convert_from_isometric_2d(mouse_x, mouse_y)

                        target_pos.x = x
                        target_pos.y = y
                        horse.change_state(UNIT_WALKING)
                        
                        print(f"screen( width:{SCREEN_WIDTH}, {SCREEN_HEIGHT}), mouse( x:{mouse_x}, y:{mouse_y})")
                    elif event.type == pygame.MOUSEBUTTONUP:
                        self.state.mouse_held = False

            if (self.state.mouse_held):
                self.state.map.minimap.update_camera(self.state.camera, mouse_x, mouse_y)

            # Gestion des touches pressées pendant la partie
            keys = pygame.key.get_pressed()
            if not (self.state.states == START):
                # Zoom de la caméra
                if keys[pygame.K_KP_PLUS] or keys[pygame.K_k]:  # Touche + du pavé numérique
                    self.state.camera.adjust_zoom(pygame.time.get_ticks(), 0.1, SCREEN_WIDTH, SCREEN_HEIGHT)
                elif keys[pygame.K_KP_MINUS] or keys[pygame.K_j]:  # Touche - du pavé numérique
                    self.state.camera.adjust_zoom(pygame.time.get_ticks(), -0.1, SCREEN_WIDTH, SCREEN_HEIGHT)

                # Basculer le mode d'affichage
                if keys[pygame.K_t]:
                    self.state.toggle_display_mode(self)
                # Pause
                if keys[pygame.K_p]:
                    self.state.toggle_pause()
                    generate_html_file()
                # Mouvement de la caméra
                if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                    scale = 2
                else:
                    scale = 1
                if keys[pygame.K_RIGHT] or keys[pygame.K_d] :
                    move_flags |= 0b0010
                if keys[pygame.K_LEFT] or keys[pygame.K_q] :
                    move_flags |= 0b0001
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    move_flags |= 0b0100
                if keys[pygame.K_UP] or keys[pygame.K_z]:
                    move_flags |= 0b1000
                if keys[pygame.K_f]:
                    self.state.toggle_fullscreen(self)

                if keys:
                    self.state.camera.move_flags = move_flags
                    self.state.terminal_camera.move_flags = move_flags
                    self.state.terminal_camera.move(current_time)
                    self.state.camera.move(current_time, 5*scale)
            # Mettre à jour l'état du jeu
            if not (self.state.states == PAUSE):
                self.state.update()

            # Effacer l'écran avant de dessiner
            
            if self.state.states == START:
                self.state.menu.draw()
                screen.blit(CURSOR_IMG,(mouse_x, mouse_y))
            else:
                if (self.state.display_mode == ISO2D): # everything in the iso2d 
                    self.screen.fill((0, 0, 0))

                    self.state.map.display(current_time, self.state.screen, self.state.camera, SCREEN_WIDTH, SCREEN_HEIGHT)

                    fps = int(self.clock.get_fps())
                    fps_text = self.font.render(f"FPS: {fps}", True, (255, 255, 255))
                    screen.blit(fps_text, (10, 10))

                    screen.blit(CURSOR_IMG,(mouse_x, mouse_y))
                    # Rafraîchissement de l'affichage
                   
                elif (self.state.display_mode == TERMINAL):
                    self.state.map.terminal_display(current_time, self.state.terminal_camera)

                horse.try_to_move(current_time, target_pos)
            
            pygame.display.flip()
            self.clock.tick(FPS)
            
        pygame.quit()


if __name__ == "__main__":
    game = GameLoop()
    game.run()
