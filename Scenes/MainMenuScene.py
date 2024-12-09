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
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        #Sets up character objects
        self.blinky = Blinky()
        self.pinky = Pinky()
        self.inky = Inky()
        self.clyde = Clyde()
        self.pac_man = PacMan()

        #Sets up interactable buttons
        #self.play_button = Button()

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

        button_image = pygame.image.load("Images/Button/Play_Button_Normal.png")
        button_image = pygame.transform.scale(button_image, (240, 80))
        button_image_rect = button_image.get_rect()
        button_image_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 100)

        self.main_menu_surface.blit(button_image, button_image_rect)

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

        #Switches to the main menu scene for debugging purposes
        if(keys[pygame.K_s]):
            self.game_state_manager.set_state('Splash Scene')

    #A method to setup and blit surface objects onto the Main Menu Scene
    def set_up_main_menu_surface(self):
        #Fills the background color of the Main Menu Scene
        self.main_menu_surface.fill("black")

        #Sets up the color for the scene borders and text
        DARK_YELLOW = (241, 196, 15)

        #Draws the Main Menu Scene border -> Rectangle(surface, color, (top-left x, top-left y, width, height), border line width [has no fill if you define width])
        pygame.draw.rect(self.main_menu_surface, DARK_YELLOW, (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT), 4)

        #Creates the title of the Main Menu Scene by creating a render (surface object) of the text through a custom font
        pacmania_font = pygame.font.Font('Fonts/Pacmania/Pacmania-Normal.ttf', 86) #Loads the font

        pac_man_text = pacmania_font.render('Pac-Man', True, DARK_YELLOW)
        pac_man_text_rect = pac_man_text.get_rect()
        pac_man_text_rect.centerx = self.WINDOW_WIDTH / 2
        pac_man_text_rect.centery = 100

        #Sets up the Blinky ghost object and updates it's movement frame in runtime
        self.update_frame_ghost(self.blinky)
        self.blinky.get_rect().center = (80, self.WINDOW_HEIGHT / 2 - 100)

        #Sets up the Pinky ghost object and updates it's movement frame in runtime
        self.update_frame_ghost(self.pinky)
        self.pinky.get_rect().center = (180, self.WINDOW_HEIGHT / 2 - 100)

        #Sets up the Inky ghost image and updates it's movement frame in runtime
        self.update_frame_ghost(self.inky)
        self.inky.get_rect().center = (80, self.WINDOW_HEIGHT / 2)

        #Sets up the Clyde ghost image and updates it's movement frame in runtime
        self.update_frame_ghost(self.clyde)
        self.clyde.get_rect().center = (180, self.WINDOW_HEIGHT / 2)

        #Sets up the Pac-Man image and updates it's movement frame in runtime
        self.update_frame_pac_man()
        self.pac_man.get_rect().center = (320, self.WINDOW_HEIGHT / 2 - 50)

        #Sets up the Power Pellet image
        power_pellet_image = pygame.image.load('Images/Dots/power_pellet.png')
        power_pellet_image = pygame.transform.scale(power_pellet_image, (40, 40))
        power_pellet_image_rect = power_pellet_image.get_rect()
        power_pellet_image_rect.center = (415, self.WINDOW_HEIGHT / 2 - 50)

        #Sets up the play button for the Main Menu Scene


        #Blits the text and images onto the main menu surface using their positioned rects
        self.main_menu_surface.blit(pac_man_text, pac_man_text_rect)
        self.main_menu_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
        self.main_menu_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
        self.main_menu_surface.blit(self.inky.get_image(), self.inky.get_rect())
        self.main_menu_surface.blit(self.clyde.get_image(), self.clyde.get_rect())
        self.main_menu_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
        self.main_menu_surface.blit(power_pellet_image, power_pellet_image_rect)

    #A method to check what movement frames the ghost is in
    def update_frame_ghost(self, ghost):
        #0: The Ghost is in frame 1
        if(ghost.get_frame() < 1):
            ghost.set_RMF1()
            ghost.set_frame(1)
        #1: The Ghost is in frame 2
        else:
            ghost.set_RMF2()
            ghost.set_frame(0)
        
        #Debug code for checking frame change speed
            #print(ghost.get_frame())
    
    #A method to check what movement frames Pac-Man is in
    def update_frame_pac_man(self):
        match self.pac_man.get_frame():
            case 0:
                self.pac_man.set_CF()
                self.pac_man.set_frame(1)
            case 1:
                self.pac_man.set_RMF1()
                self.pac_man.set_frame(2)
            case 2:
                self.pac_man.set_RMF2()
                self.pac_man.set_frame(0)
        
        #Debug code for checking frame change speed
            #print(self.pac_man.get_frame())