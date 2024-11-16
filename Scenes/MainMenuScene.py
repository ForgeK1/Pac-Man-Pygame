'''
Description: The MainMenuScene class serves to help the player to navigate the game
'''

#Imports pygame libraries
import pygame

class MainMenuScene:
    #A constructor to initialize an instance of Main Menu Scene
    def __init__(self, display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        '''
        Sets up the Main Menu Scene surface to continiously update and blit onto the display surface
            Note: pygame.SRCALPHA must be included to access the alpha channel so that the program
                  can change the transparency of the surface object below during runtime
        '''
        self.main_menu_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)
    
    #A method to run MainMenuScene
    def run(self):
        #Resets the display surface background to blit a dynamically updated Main Menu Scene surface
        self.display_surface.fill('blue')

        #A method to set up the Main Menu Surface
        self.set_up_main_menu_surface()

        #Blits the updated Main Menu Surface onto the display surface
        self.display_surface.blit(self.main_menu_surface, (0, 0))

        #Checks for player input
        self.player_input()
    
    #A method to check for player input
    def player_input(self):
        #Grabs all the keys pressed by the player
        keys = pygame.key.get_pressed()

        #Switches to the main menu scene for debugging purposes
        if(keys[pygame.K_s]):
            self.game_state_manager.set_state('Splash Scene')

    #A method to setup and blit surface objects onto the Main Menu Scene
    def set_up_main_menu_surface(self):
        #Fills the background color of the Main Menu Scene
        self.main_menu_surface.fill("orange")