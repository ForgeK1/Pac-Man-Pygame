'''
Description: The MainMenuScene class serves to help the player to navigate the game
'''

#Imports pygame libraries and needed classes from their respective modules
import pygame
from Characters.PacMan import PacMan
from Characters.Blinky import Blinky
from Characters.Pinky import Pinky
from Characters.Inky import Inky
from Characters.Clyde import Clyde
from Functions.Button import Button

class MainMenuScene:
    #A constructor to initialize an instance of Main Menu Scene
    def __init__(self, display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT):
        #Initializes the display surface and game state manager
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        #Initializes the character objects
        self.blinky = Blinky()
        self.pinky = Pinky()
        self.inky = Inky()
        self.clyde = Clyde()
        self.pac_man = PacMan()
        self.power_pellet_image = pygame.image.load('Images/Dots/power_pellet.png')

        #Initializes the interactable buttons
        self.play_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                  'Play', "black", "black", "black", 'Fonts/Pixel/DePixelHalbfett.ttf', 24)
        self.quit_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                  'Quit', "black", "black", "black", 'Fonts/Pixel/DePixelHalbfett.ttf', 24)

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

        #Delayes the game by 100 miliseconds so that the animations do not update too fast
        pygame.time.delay(100)
    
    #A method to check for player input
    def player_input(self):
        #Grabs all the keys pressed by the player
        keys = pygame.key.get_pressed()

        #Switches to the Main Menu Scene for debugging purposes
        if(keys[pygame.K_s]):
            self.game_state_manager.set_state('Splash Scene')

    #A method to setup and blit surface objects onto the Main Menu Scene
    def set_up_main_menu_surface(self):
        #Fills the background color of the Main Menu Scene
        self.main_menu_surface.fill("black")

        #Sets up the color for the scene borders and text
        DARK_YELLOW = (241, 196, 15)

        #Creates the title of the Main Menu Scene by creating a render (surface object) of the text through a custom font
        pacmania_font = pygame.font.Font('Fonts/Pacmania/Pacmania-Normal.ttf', 86) #Loads the font

        pac_man_text = pacmania_font.render('Pac-Man', True, DARK_YELLOW)
        pac_man_text_rect = pac_man_text.get_rect()
        pac_man_text_rect.centerx = self.WINDOW_WIDTH / 2
        pac_man_text_rect.centery = 100

        #Blits the text onto the main menu surface using text's positioned rect
        self.main_menu_surface.blit(pac_man_text, pac_man_text_rect)

        #Sets up the characters for the background
        self.set_up_characters()

        #Sets up interactable buttons
        self.set_up_buttons()

    #A method to set up the characters and pellet for Main Menu Scene background
    def set_up_characters(self):
        #Sets up the Blinky ghost object and updates it's movement frame in runtime
        self.blinky.update_frame()
        self.blinky.get_rect().center = (80, self.WINDOW_HEIGHT / 2 - 100)

        #Sets up the Pinky ghost object and updates it's movement frame in runtime
        self.pinky.update_frame()
        self.pinky.get_rect().center = (180, self.WINDOW_HEIGHT / 2 - 100)

        #Sets up the Inky ghost image and updates it's movement frame in runtime
        self.inky.update_frame()
        self.inky.get_rect().center = (80, self.WINDOW_HEIGHT / 2)

        #Sets up the Clyde ghost image and updates it's movement frame in runtime
        self.clyde.update_frame()
        self.clyde.get_rect().center = (180, self.WINDOW_HEIGHT / 2)

        #Sets up the Pac-Man image and updates it's movement frame in runtime
        self.pac_man.update_frame()
        self.pac_man.get_rect().center = (320, self.WINDOW_HEIGHT / 2 - 50)

        #Sets up the Power Pellet image
        self.power_pellet_image = pygame.transform.scale(self.power_pellet_image, (40, 40))
        self.power_pellet_image_rect = self.power_pellet_image.get_rect()
        self.power_pellet_image_rect.center = (415, self.WINDOW_HEIGHT / 2 - 50)

        #Blits the images onto the main menu surface using their positioned rects
        self.main_menu_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
        self.main_menu_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
        self.main_menu_surface.blit(self.inky.get_image(), self.inky.get_rect())
        self.main_menu_surface.blit(self.clyde.get_image(), self.clyde.get_rect())
        self.main_menu_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
        self.main_menu_surface.blit(self.power_pellet_image, self.power_pellet_image_rect)
    
    #A method to set up interactable buttons
    def set_up_buttons(self):
        self.play_button.scale_button(260, 74, 30)
        self.play_button.get_image_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 120)
        self.play_button.get_text_rect().center= (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 120)
        
        self.main_menu_surface.blit(self.play_button.get_image(), self.play_button.get_image_rect())
        self.main_menu_surface.blit(self.play_button.get_text(), self.play_button.get_text_rect())

        self.quit_button.scale_button(260, 74, 30)
        self.quit_button.get_image_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 220)
        self.quit_button.get_text_rect().center= (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 220)
        
        self.main_menu_surface.blit(self.quit_button.get_image(), self.quit_button.get_image_rect())
        self.main_menu_surface.blit(self.quit_button.get_text(), self.quit_button.get_text_rect())