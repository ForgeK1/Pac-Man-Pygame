'''
Description: The SplashScene class showcases the splash screen of the game
'''

#Imports pygame libraries
import pygame

class SplashScene:
    #A Constructor to initialize an instance of Splash Screen class
    def __init__(self, display_surface, game_state_manager, window_width, window_height):
        #Sets up variables relating to the display
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = window_width
        self.WINDOW_HEIGHT = window_height
    
    def run(self):
        #Sets up colors
        DARK_YELLOW = (241, 196, 15)
        
        #Fills the background color of the display surface
        self.display_surface.fill('black')

        #Sets up Splash Screen border -> Rectangle(surface, color, (top-left x, top-left y, width, height), border line width [has no fill if you define width])
        pygame.draw.rect(self.display_surface, DARK_YELLOW, (0, 0, self.WINDOW_WIDTH, self.WINDOW_HEIGHT), 4) 

        #Sets up Pac-Man icon by creating surface image, getting rect of the image, and positioning the rect
        game_icon_image = pygame.image.load('Images/Splash Screen/pacman_icon.png')
        game_icon_image = pygame.transform.scale(game_icon_image, (300, 300))
        game_icon_rect = game_icon_image.get_rect()
        game_icon_rect.centerx = self.WINDOW_WIDTH / 2
        game_icon_rect.centery = self.WINDOW_HEIGHT / 2 + 100
        self.display_surface.blit(game_icon_image, game_icon_rect)

        #Sets up Splash Screen text (title) by creating a render (surface object) of the text 
        pacmania_font = pygame.font.Font('Fonts/Pacmania/Pacmania-Normal.ttf', 96) #Loads the font
        
        splash_text = pacmania_font.render('SPLASH', True, DARK_YELLOW) #(*text*, *anti-aliasing boolean*, *color of text*, *background color of text* [optional])
        splash_text_rect = splash_text.get_rect()
        splash_text_rect.centerx = self.WINDOW_WIDTH / 2
        splash_text_rect.centery = 100

        self.display_surface.blit(splash_text, splash_text_rect)

        screen_text = pacmania_font.render('SCREEN', True, DARK_YELLOW)
        screen_text_rect = screen_text.get_rect()
        screen_text_rect.centerx = self.WINDOW_WIDTH / 2
        screen_text_rect.centery = 200

        self.display_surface.blit(screen_text, screen_text_rect)