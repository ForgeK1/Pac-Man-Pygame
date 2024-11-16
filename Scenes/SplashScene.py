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
            pygame.time.delay(3000)

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

        #Sets up Splash Scene border -> Rectangle(surface, color, (top-left x, top-left y, width, height), border line width [has no fill if you define width])
        pygame.draw.rect(self.splash_surface, DARK_YELLOW, (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT), 4)

        #Sets up Pac-Man icon by creating surface image, getting rect of the image, and positioning the rect
        game_icon_image = pygame.image.load('Images/Splash Scene/pacman_icon.png')
        game_icon_image = pygame.transform.scale(game_icon_image, (300, 300))
        game_icon_rect = game_icon_image.get_rect()
        game_icon_rect.centerx = self.WINDOW_WIDTH / 2
        game_icon_rect.centery = self.WINDOW_HEIGHT / 2 + 100

        #Sets up Splash Scene text (title) by creating a render (surface object) of the text 
        pacmania_font = pygame.font.Font('Fonts/Pacmania/Pacmania-Normal.ttf', 96) #Loads the font
        
        splash_text = pacmania_font.render('SPLASH', True, DARK_YELLOW) #(*text*, *anti-aliasing boolean*, *color of text*, *background color of text* [optional])
        splash_text_rect = splash_text.get_rect()
        splash_text_rect.centerx = self.WINDOW_WIDTH / 2
        splash_text_rect.centery = 100

        scene_text = pacmania_font.render('SCREEN', True, DARK_YELLOW)
        scene_text_rect = scene_text.get_rect()
        scene_text_rect.centerx = self.WINDOW_WIDTH / 2
        scene_text_rect.centery = 200

        #Blits game icon and "Splash" and "Text" onto the display surface
        self.splash_surface.blit(game_icon_image, game_icon_rect)
        self.splash_surface.blit(splash_text, splash_text_rect)
        self.splash_surface.blit(scene_text, scene_text_rect)