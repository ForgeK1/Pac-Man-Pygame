'''
Description: The MainMenuScene class serves to help the player to navigate the game
'''

#Imports pygame libraries
import pygame

class MainMenuScene:
    def __init__(self, display_surface, game_state_manager):
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
    
    def run(self):
        self.display_surface.fill('green')

        #Grabs all possible keys pressed by the player
        keys = pygame.key.get_pressed()

        #Switches to the splash screen for debugging purposes
        if(keys[pygame.K_s]):
            self.game_state_manager.set_state('Splash Screen')