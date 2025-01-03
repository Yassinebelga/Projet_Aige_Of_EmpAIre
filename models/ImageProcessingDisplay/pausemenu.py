import pygame
from GLOBAL_VAR import *

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, 36)

        # Button dimensions
        self.button_width = 200
        self.button_height = 50

        # Initialize button positions (updated dynamically)
        self.buttons = {}
        self._update_buttons()

    def _update_buttons(self):
        """Recalculate button positions based on screen size."""
        screen_width, screen_height = self.screen.get_size()
        center_x = screen_width // 2
        center_y = screen_height // 2

        self.buttons = {
            'save': pygame.Rect(center_x - self.button_width // 2, center_y - 60, self.button_width, self.button_height),
            'quit': pygame.Rect(center_x - self.button_width // 2, center_y, self.button_width, self.button_height),
            'resume': pygame.Rect(center_x - self.button_width // 2, center_y + 60, self.button_width, self.button_height)
        }

    def draw(self):
        """Draw the pause menu overlay and buttons."""
        # Update button positions in case of screen resize
        self._update_buttons()

        # Draw semi-transparent overlay
        overlay = pygame.Surface(self.screen.get_size())
        overlay.set_alpha(220)  # Transparency level (0-255)
        overlay.fill((0, 0, 0))  # Black background
        self.screen.blit(overlay, (0, 0))

        # Draw pause menu title
        title_text = self.font.render("Pause Menu", True, WHITE_COLOR)
        title_rect = title_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 - 120))
        self.screen.blit(title_text, title_rect)

        # Draw buttons
        for button_text, button_rect in self.buttons.items():
            pygame.draw.rect(self.screen, (50, 50, 50), button_rect)  # Button background
            text = self.font.render(button_text.capitalize(), True, WHITE_COLOR)
            text_rect = text.get_rect(center=button_rect.center)
            self.screen.blit(text, text_rect)

    def handle_click(self, pos, game_state):
        """Handle button clicks based on mouse position."""
        if self.buttons['save'].collidepoint(pos):
            #game_state.save_manager.save_game()
            print("Game Saved!")  # Replace with actual save logic
        elif self.buttons['quit'].collidepoint(pos):
            pygame.quit()
            exit()
        elif self.buttons['resume'].collidepoint(pos):
            game_state.toggle_pause()
