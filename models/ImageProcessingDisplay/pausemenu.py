import pygame
from GLOBAL_VAR import *

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

        # Button positions and dimensions
        self.buttons = {
            'save': pygame.Rect(self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 - 50, 100, 30),
            'quit': pygame.Rect(self.screen.get_width() // 2 - 50, self.screen.get_height() // 2, 100, 30),
            'resume': pygame.Rect(self.screen.get_width() // 2 - 50, self.screen.get_height() // 2 + 50, 100, 30)
        }

    def draw(self):
        # Draw semi-transparent overlay
        overlay = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        overlay.set_alpha(150)  # Set transparency level (0-255)
        overlay.fill((0, 0, 0))  # Black background
        self.screen.blit(overlay, (0, 0))

        # Draw pause menu title
        pause_text = self.font.render("Pause Menu", True, WHITE)
        self.screen.blit(pause_text, (self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 - 100))

        # Draw buttons
        for button_text, button_rect in self.buttons.items():
            pygame.draw.rect(self.screen, (50, 50, 50), button_rect)  # Draw button
            text = self.font.render(button_text.capitalize(), True, WHITE)
            self.screen.blit(text, (button_rect.x + 10, button_rect.y + 5))

    def handle_click(self, event, game_state):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.buttons['save'].collidepoint(mouse_pos):
                print("Game Saved!")  # Replace with actual save logic
            elif self.buttons['quit'].collidepoint(mouse_pos):
                pygame.quit()
                exit()
            elif self.buttons['resume'].collidepoint(mouse_pos):
                game_state.toggle_pause()