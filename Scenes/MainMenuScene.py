'''
Description: The Main Menu Scene class serves to help the player to navigate the menu of the game
'''

#Imports pygame libraries and needed classes from their respective modules
import pygame
from Characters_and_Objects.PacMan import PacMan
from Characters_and_Objects.Ghosts.Blinky import Blinky
from Characters_and_Objects.Ghosts.Pinky import Pinky
from Characters_and_Objects.Ghosts.Inky import Inky
from Characters_and_Objects.Ghosts.Clyde import Clyde
from Functions.Button import Button

class MainMenuScene:
    #A constructor to initialize an instance of Main Menu Scene
    def __init__(self, display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT):        
        #Initializes the display surface and game state manager
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        '''
        Sets up the Main Menu Scene surface to continiously update and blit it onto the display surface
            Note: pygame.SRCALPHA must be included to access the alpha channel so that the program
                  can change the transparency of the surface object below during runtime
        '''
        self.main_menu_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)

        #Initializes the character objects
        self.pac_man = PacMan(70, 70, "Right", 320, self.WINDOW_HEIGHT / 2 - 50, True, 100)
        self.blinky = Blinky(70, 70, "Right", 80, self.WINDOW_HEIGHT / 2 - 100, True, 100, 0)
        self.pinky = Pinky(70, 70, "Right", 180, self.WINDOW_HEIGHT / 2 - 100, True, 100, 0)
        self.inky = Inky(70, 70, "Right", 80, self.WINDOW_HEIGHT / 2, True, 100, 0)
        self.clyde = Clyde(70, 70, "Right", 180, self.WINDOW_HEIGHT / 2, True, 100, 0)
        self.power_pellet_image = pygame.image.load('Images/Dots/power_pellet.png')

        #Initializes the interactable buttons
        self.play_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                  'Play', "black", "black", "black", 'Fonts/Pixel/DePixelHalbfett.ttf', 24)
        self.quit_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                  'Quit', "black", "black", "black", 'Fonts/Pixel/DePixelHalbfett.ttf', 24)
    
    #A method to run Main Menu Scene
    def run(self, event): 
        #Fills the background of the display surface
        self.display_surface.fill('black')
        
        #Checks and handles player events for the Main Menu Scene
        self.event_handler(event)
        
        #A method to set up the updated Main Menu Scene surface
        self.set_up_main_menu_surface()

        #Blits the Main Menu Scene surface onto the display surface
        self.display_surface.blit(self.main_menu_surface, (0, 0))

    #A method to setup and blit surface objects onto the Main Menu Scene
    def set_up_main_menu_surface(self):
        #Fills the background color of the Main Menu Scene
        self.main_menu_surface.fill('black')

        #Sets up the color for the scene borders and text
        DARK_YELLOW = (241, 196, 15)

        #Loads a custom font to use for the Main Menu Scene title
        pacmania_font = pygame.font.Font('Fonts/Pacmania/Pacmania-Normal.ttf', 86)

        #Sets up the screen title by creating a render (surface object) of the text through the custom font
        pac_man_text = pacmania_font.render('Pac-Man', True, DARK_YELLOW)
        pac_man_text_rect = pac_man_text.get_rect()
        pac_man_text_rect.centerx = self.WINDOW_WIDTH / 2
        pac_man_text_rect.centery = 100

        #Blits the text onto the main menu surface using text's positioned rect
        self.main_menu_surface.blit(pac_man_text, pac_man_text_rect)

        #Updates all character animation based on the character_animation_speed variable
        self.pac_man.animation_update()
        self.blinky.animation_update()
        self.pinky.animation_update()
        self.inky.animation_update()
        self.clyde.animation_update()

        #Sets up the Power Pellet image
        self.power_pellet_image = pygame.transform.scale(self.power_pellet_image, (40, 40))
        self.power_pellet_image_rect = self.power_pellet_image.get_rect()
        self.power_pellet_image_rect.center = (415, self.WINDOW_HEIGHT / 2 - 50)
        
        #Blits all character images and rects onto the Gameplay Scene
        self.main_menu_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
        self.main_menu_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
        self.main_menu_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
        self.main_menu_surface.blit(self.inky.get_image(), self.inky.get_rect())
        self.main_menu_surface.blit(self.clyde.get_image(), self.clyde.get_rect())
        self.main_menu_surface.blit(self.power_pellet_image, self.power_pellet_image_rect)

        #Sets up interactable buttons
        self.set_up_buttons()        
    
    #A method to set up the play and quit buttons
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
    
    #A method to check and handle player events for the Main Menu Scene
    def event_handler(self, event):
        '''
        A section to handle player events for interacting with the play & quit buttons
        '''
        
        #Default values for the following variables
        mouse_pos = (0, 0)
        mouse_click = False
        mouse_let_go = False
        
        '''
        Uses the event dictionary (Ex. 'pos', 'buttons', 'touch', 'window') to grab mouse position 
        (checks if 'pos' exists in the dictionary before grabbing the value)
        '''
        if('pos' in event.dict):
            mouse_pos = event.dict.get('pos') #Returns a tuple

        #Uses the event type to check if the player has clicked or let go of the left mouse button
        if('button' in event.dict and                 #Checks if there is a button categrory in dict
            event.type == pygame.MOUSEBUTTONDOWN and  #Checks if we're clicking down on a mouse button  
            event.dict.get('button') == 1):           #Checks if its the left mouse that were clicking
            mouse_click = True
            mouse_let_go = False
        elif('button' in event.dict and                 
             event.type == pygame.MOUSEBUTTONUP and   
             event.dict.get('button') == 1):           
             mouse_click = False
             mouse_let_go = True
        
        #If the player clicked and let go of the play button, then they will be directed to the Gameplay Scene
        if(self.play_button.check_input(mouse_pos, mouse_click, mouse_let_go)):
            #Stops playing and unloads the Pac-Man Theme Remix for the Main Menu Scene from the music_mixer
            pygame.mixer_music.stop()
            pygame.mixer_music.unload()

            #Loads and plays the Pac-Man Start Theme when switching to the Gameplay Scene
            pygame.mixer_music.load('Audio/Music/Pac-Man Start Theme.wav')
            pygame.mixer_music.play()
            
            self.game_state_manager.set_scene_state('Gameplay Scene')

        '''
        If the player clicked and let go of the quit button, the program will convert the running boolean to 
        False to stop the game loop in the Game class
        '''
        if(self.quit_button.check_input(mouse_pos, mouse_click, mouse_let_go)):
            self.game_state_manager.set_running_state(False)
        
        #Debug code to ensure that the function contains all the events done by the player 
            #print(event.dict)
            #print(mouse_pos)