class MainMenuScene:
    def __init__(self, display_surface, game_state_manager):
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
    
    def run(self):
        self.display_surface.fill('green')