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

        #Sets up the Blinky ghost image by creating a surface image, getting the rect of it, and then positioning the image
        blinky_image = pygame.image.load('Images/Ghosts/Blinky (Red)/right_frame_1.png')
        blinky_image = pygame.transform.scale(blinky_image, (70, 70))
        blinky_image_rect = blinky_image.get_rect()
        blinky_image_rect.center = (80, self.WINDOW_HEIGHT / 2 - 100)

        #Sets up the Pinky ghost image
        pinky_image = pygame.image.load('Images/Ghosts/Pinky (Pink)/right_frame_1.png')
        pinky_image = pygame.transform.scale(pinky_image, (70, 70))
        pinky_image_rect = pinky_image.get_rect()
        pinky_image_rect.center = (180, self.WINDOW_HEIGHT / 2 - 100)

        #Sets up the Inky ghost image
        inky_image = pygame.image.load('Images/Ghosts/Inky (Cyan)/right_frame_1.png')
        inky_image = pygame.transform.scale(inky_image, (70, 70))
        inky_image_rect = inky_image.get_rect()
        inky_image_rect.center = (80, self.WINDOW_HEIGHT / 2)

        #Sets up the Clyde ghost image
        clyde_image = pygame.image.load('Images/Ghosts/Clyde (Orange)/right_frame_1.png')
        clyde_image = pygame.transform.scale(clyde_image, (70, 70))
        clyde_image_rect = clyde_image.get_rect()
        clyde_image_rect.center = (180, self.WINDOW_HEIGHT / 2)

        #Sets up the Pac-Man image
        pac_man_image = pygame.image.load('Images/Pac Man/Movement/right_frame_1.png')
        pac_man_image = pygame.transform.scale(pac_man_image, (70, 70))
        pac_man_image_rect = pac_man_image.get_rect()
        pac_man_image_rect.center = (320, self.WINDOW_HEIGHT / 2 - 50)

        #Sets up the Power Pellet image
        power_pellet_image = pygame.image.load('Images/Dots/power_pellet.png')
        power_pellet_image = pygame.transform.scale(power_pellet_image, (40, 40))
        power_pellet_image_rect = power_pellet_image.get_rect()
        power_pellet_image_rect.center = (415, self.WINDOW_HEIGHT / 2 - 50)

        #Blits the text and images onto the main menu surface using their positioned rects
        self.main_menu_surface.blit(pac_man_text, pac_man_text_rect)
        self.main_menu_surface.blit(blinky_image, blinky_image_rect)
        self.main_menu_surface.blit(pinky_image, pinky_image_rect)
        self.main_menu_surface.blit(inky_image, inky_image_rect)
        self.main_menu_surface.blit(clyde_image, clyde_image_rect)
        self.main_menu_surface.blit(pac_man_image, pac_man_image_rect)
        self.main_menu_surface.blit(power_pellet_image, power_pellet_image_rect)