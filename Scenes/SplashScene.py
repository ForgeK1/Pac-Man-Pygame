'''
Description: The SplashScene class showcases the splash screen of the game
'''

#Imports pygame libraries
import pygame

class SplashScene:
    #A Constructor to initialize an instance of Splash Screen class
    def __init__(self, display_surface, game_state_manager, window_width, window_height):
        #Sets up variables relating to the Display Surface
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height

        '''
        Sets up the the splash surface variable to blit onto the Display Surface
            Note: pygame.SRCALPHA must be included in order to access the alpha channel in order to change
                  the transparency of the surface object
        '''
        self.splash_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)

        #Sets up a variable to keep track of the transparency of the Splash Surface
        self.transparency = 0
    
    #A method to run the Splash Screen
    def run(self):
        #Sets up the Splash Surface
        self.set_up_splash_surface()
        
        #An if statement to dynamically change the transparency of the splash screen
        if self.transparency < 255:
            self.transparency += 1
            pygame.time.delay(80)

        #Sets the alpha of Splash Surface based on the current transparency value
        self.splash_surface.set_alpha(self.transparency)

        #Blits the fully finished Splash Surface onto the Display Surface
        self.display_surface.blit(self.splash_surface, (0,0))

        #Grabs all the keys pressed by the player
        keys = pygame.key.get_pressed()

        #Switches to the main menu screen for debugging purposes
        if(keys[pygame.K_m]):
            self.game_state_manager.set_state('Main Menu Screen')

    #A method to set up and blit the surface objects onto the Splash Surface
    def set_up_splash_surface(self):
        #Fills the background color of the Splash Surface
        self.splash_surface.fill('black')

        #Sets up color for the splash screen borders and text
        DARK_YELLOW = (241, 196, 15)

        #Sets up Splash Screen border -> Rectangle(surface, color, (top-left x, top-left y, width, height), border line width [has no fill if you define width])
        pygame.draw.rect(self.splash_surface, DARK_YELLOW, (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT), 4)

        #Sets up Pac-Man icon by creating surface image, getting rect of the image, and positioning the rect
        game_icon_image = pygame.image.load('Images/Splash Screen/pacman_icon.png')
        game_icon_image = pygame.transform.scale(game_icon_image, (300, 300))
        game_icon_rect = game_icon_image.get_rect()
        game_icon_rect.centerx = self.WINDOW_WIDTH / 2
        game_icon_rect.centery = self.WINDOW_HEIGHT / 2 + 100

        #Sets up Splash Screen text (title) by creating a render (surface object) of the text 
        pacmania_font = pygame.font.Font('Fonts/Pacmania/Pacmania-Normal.ttf', 96) #Loads the font
        
        splash_text = pacmania_font.render('SPLASH', True, DARK_YELLOW) #(*text*, *anti-aliasing boolean*, *color of text*, *background color of text* [optional])
        splash_text_rect = splash_text.get_rect()
        splash_text_rect.centerx = self.WINDOW_WIDTH / 2
        splash_text_rect.centery = 100

        screen_text = pacmania_font.render('SCREEN', True, DARK_YELLOW)
        screen_text_rect = screen_text.get_rect()
        screen_text_rect.centerx = self.WINDOW_WIDTH / 2
        screen_text_rect.centery = 200

        #Blits game icon and "Splash" and "Text" onto the display surface
        self.splash_surface.blit(game_icon_image, game_icon_rect)
        self.splash_surface.blit(splash_text, splash_text_rect)
        self.splash_surface.blit(screen_text, screen_text_rect)