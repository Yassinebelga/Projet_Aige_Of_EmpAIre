Part of Yassine
class GlobalMenu:
    def __init__(self):
        # Attributs du menu
        self.in_menu = False  # Est-ce qu'on est dans le menu principal ?
        self.is_paused = False  # Est-ce que le jeu est en pause ?
        self.is_playing = False  # Est-ce que le joueur est en train de jouer ?
        self.show_pause_buttons = False  # A-t-on besoin des boutons de pause ?
        self.show_game_buttons = False  # A-t-on besoin des boutons de jeu ?

    def toggle_menu(self):
        """Permet de basculer l'état du menu."""
        self.in_menu = not self.in_menu
        # Si on entre dans le menu, on arrête le jeu et on désactive les boutons
        if self.in_menu:
            self.is_playing = False
            self.is_paused = False
            self.show_pause_buttons = False
            self.show_game_buttons = False

    def toggle_pause(self):
        """Met en pause ou reprend le jeu."""
        if not self.in_menu and self.is_playing:
            self.is_paused = not self.is_paused
            # Affiche ou cache les boutons de pause
            self.show_pause_buttons = self.is_paused

    def start_game(self):
        """Démarre le jeu."""
        if not self.in_menu:
            self.is_playing = True
            self.is_paused = False
            self.show_pause_buttons = False
            self.show_game_buttons = True  # Les boutons de jeu sont maintenant visibles

    def stop_game(self):
        """Arrête le jeu."""
        self.is_playing = False
        self.is_paused = False
        self.show_pause_buttons = False
        self.show_game_buttons = False
