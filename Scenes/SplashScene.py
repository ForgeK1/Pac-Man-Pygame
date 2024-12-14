'''
Description: A class to create and showcase the splash scene of the game
'''

#Imports pygame libraries
import pygame

class SplashScene:
    #A constructor to initialize an instance of Splash Scene
    def __init__(self, display_surface, game_state_manager, window_width, window_height):
        #Initializes variables relating to the sisplay surface and game state manager
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height

        '''
        Sets up the the Splash Scene surface to continiously update and blit onto the display surface
            Note: pygame.SRCALPHA must be included to access the alpha channel so that the program
                  can change the transparency of the surface object below during runtime
        '''
        self.splash_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)

        #Initializes up variables to keep track of the transparency of the Splash Surface
        self.transparency = 0
        self.fully_transparent = False
    
    #A method to run the Splash Scene
    def run(self):
        #Resets the display surface background to blit a dynamically updated Main Menu Scene surface
        self.display_surface.fill('black')
        
        #A method to set up the Splash Scene
        self.set_up_splash_surface()

        '''
        An if statement to check if the transparency has reached 250 to pause the splash scene (momentarily stops
        changing the transparency of the Splash Surface)
        '''
        if self.transparency == 250:
            self.fully_transparent = True
            pygame.time.delay(5000)

            #Debug code
                #print(str(self.transparency) + " First if statement ran \n")
        
        #An if-else statement to dynamically change the value of the transparency variable for the Splash Surface
        if self.fully_transparent == False:
            self.transparency += 10
            pygame.time.delay(50)

            #Debug code
                #print(str(self.transparency) + " Second if statement ran \n")
        elif(self.fully_transparent and self.transparency > 0):
            self.transparency -= 10
            pygame.time.delay(50)

            #Debug code
                #print(str(self.transparency) + " Third if statement ran \n")
            
        #Sets the alpha of Splash Surface based on the current transparency value during each function call
        self.splash_surface.set_alpha(self.transparency)

        #Continiously blits the Splash Surface onto the display surface
        self.display_surface.blit(self.splash_surface, (0, 0))

        '''
        An if statement that uses the game state manager to re-direct the player to the 
        main menu scene after the splash scene dissapears
            Note: Although the value of transparency is 0 in the beginning, the game 
                  doesn't switch scenes because the variable gets incremented before
                  reaching this if statement
        '''
        if self.transparency == 0:
            self.game_state_manager.set_state('Main Menu Scene')

    #A method to set up and blit the surface objects onto the Splash Surface
    def set_up_splash_surface(self):
        #Fills the background color of the Splash Surface
        self.splash_surface.fill('black')
        
        #Sets up color for the splash scene borders and text
        DARK_YELLOW = (241, 196, 15)

        #Draws the Splash Scene border -> Rectangle(surface, color, (top-left x, top-left y, width, height), border line width [has no fill if you define width])
        #pygame.draw.rect(self.splash_surface, DARK_YELLOW, (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT), 4)

        #Sets up the Splash Scene title by creating a surface image, getting the rect of it, and then positioning the image
        title_image = pygame.image.load('Images/Other/title.png')
        title_image = pygame.transform.scale(title_image, (402, 97))
        title_image_rect = title_image.get_rect()
        title_image_rect.center = (self.WINDOW_WIDTH / 2, 100)

        #Sets up the background image for Splash Scene
        background_image = pygame.image.load('Images/Other/background.png')
        background_image = pygame.transform.scale(background_image, (451, 346))
        background_image_rect = background_image.get_rect()
        background_image_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 20)

        '''
        Creates the title and rights reserved texts of the Main Menu Scene by creating a render (surface object) 
        of the text through a custom font
        '''
        pixel_font = pygame.font.Font('Fonts/Pixel/DePixelHalbfett.ttf', 12)

        author_text = pixel_font.render('A Python Pygame Project By Keyvan M. Kani', True, DARK_YELLOW)
        author_text_rect = author_text.get_rect()
        author_text_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 220)

        rights_reserved_text = pixel_font.render('All Rights Reserved To Bandai Namco Entertainment', True, DARK_YELLOW)
        rights_reserved_text_rect = rights_reserved_text.get_rect()
        rights_reserved_text_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 250)
        
        #Blits the text and images onto the splash surface using their positioned rects
        self.splash_surface.blit(title_image, title_image_rect)
        self.splash_surface.blit(background_image, background_image_rect)
        self.splash_surface.blit(author_text, author_text_rect)
        self.splash_surface.blit(rights_reserved_text, rights_reserved_text_rect)