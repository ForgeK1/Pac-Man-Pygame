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
        #Variables for the display surface and Game State Manager
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        '''
        Sets up the Main Menu Scene surface to continiously update and blit it onto the display surface
            NOTE: pygame.SRCALPHA must be included to access the alpha channel so that the program
                  can change the transparency of the surface object below during runtime
        '''
        self.main_menu_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)

        #Variables for the character & power pellet objects
        self.pac_man = PacMan(40, 40, 'Right', 300, 425, True, 100, self.main_menu_surface)
        self.blinky = Blinky(40, 40, 'Right', 180, 395, True, 100, self.main_menu_surface, self.game_state_manager)
        self.pinky = Pinky(40, 40, 'Right', 240, 395, True, 100, self.main_menu_surface, self.game_state_manager)
        self.inky = Inky(40, 40, 'Right', 180, 455, True, 100, self.main_menu_surface, self.game_state_manager)
        self.clyde = Clyde(40, 40, 'Right', 240, 455, True, 100, self.main_menu_surface, self.game_state_manager)

        #Variables for the interactable buttons
        self.play_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                  'black', 'black', 'black', 'Play', 'Fonts/Pixel/DePixelHalbfett.ttf', 22)
        self.credits_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                     'black', 'black', 'black', 'Credits', 'Fonts/Pixel/DePixelHalbfett.ttf', 22)

        #Variables to ensure the credits button has been pressed only once
        self.previous_button_event = None
        self.credits_button_has_been_pressed = False

    #A method to run Main Menu Scene
    def run(self, event, debug_mode): 
        #Fills the background of the display surface
        self.display_surface.fill('black')
        
        #A method to set up the updated Main Menu Scene surface
        self.set_up_main_menu_surface()

        #Checks and handles player events for the Main Menu Scene
        self.event_handler(event)

        #Blits the Main Menu Scene surface onto the display surface
        self.display_surface.blit(self.main_menu_surface, (0, 0))

    #A method to setup and blit surface objects onto the Main Menu Scene
    def set_up_main_menu_surface(self):
        #Fills the background color of the Main Menu Scene
        self.main_menu_surface.fill('black')

        #Set up the background menu
        background_menu = pygame.image.load('Images/Main Menu Background.png')
        background_menu_rect = background_menu.get_rect()
        background_menu_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2)

        #Blits the background menu
        self.main_menu_surface.blit(background_menu, background_menu_rect)

        #Sets up the interactable play button
        self.set_up_buttons()  

        #Updates all character animation based on the character_animation_speed variable
        self.pac_man.animation_update()
        self.blinky.animation_update()
        self.pinky.animation_update()
        self.inky.animation_update()
        self.clyde.animation_update()
        
        #Blits all character images and rects onto the Gameplay Scene
        self.main_menu_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
        self.main_menu_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
        self.main_menu_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
        self.main_menu_surface.blit(self.inky.get_image(), self.inky.get_rect())
        self.main_menu_surface.blit(self.clyde.get_image(), self.clyde.get_rect())   
    
    #A method to set up the play and credits buttons
    def set_up_buttons(self):
        self.play_button.scale_button(170, 54, 22)
        self.play_button.get_image_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 200)
        self.play_button.get_text_rect().center= (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 201)
        
        self.main_menu_surface.blit(self.play_button.get_image(), self.play_button.get_image_rect())
        self.main_menu_surface.blit(self.play_button.get_text(), self.play_button.get_text_rect())

        self.credits_button.scale_button(170, 54, 22)
        self.credits_button.get_image_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 270)
        self.credits_button.get_text_rect().center= (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 272)
        
        self.main_menu_surface.blit(self.credits_button.get_image(), self.credits_button.get_image_rect())
        self.main_menu_surface.blit(self.credits_button.get_text(), self.credits_button.get_text_rect())
    
    #A method to check and handle player events for the Main Menu Scene
    def event_handler(self, event):
        '''
        A section to handle player events for interacting with the play & credits buttons
        '''

        #Ensures the credits button has been pressed only once
        self.validate_credits_button(event)
        
        #Default values for the following variables
        mouse_pos = (0, 0)
        mouse_click = False
        mouse_let_go = False
        
        '''
        Uses the event dictionary (ex. 'pos', 'buttons', 'touch', 'window') to grab mouse position 
        (checks if 'pos' exists in the dictionary before grabbing the value)
        '''
        if('pos' in event.dict):
            mouse_pos = event.dict.get('pos') #Returns a tuple

        #Uses the event type to check if the player has clicked or let go of the left mouse button
        if('button' in event.dict and                 #Checks if there is a button categrory in the dict
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
        If (1) the player clicked and let go of the play button and
           (2) the button hasn't been pressed before
        
        They will be directed to the Credits Scene
        '''
        if(self.credits_button.check_input(mouse_pos, mouse_click, mouse_let_go) and
           self.credits_button_has_been_pressed is False):
            self.game_state_manager.set_scene_state('Credits Scene')
        
        #Debug code to ensure that the function contains all the events done by the player 
            # print(event.dict)
            # print(mouse_pos)

    '''
    Why does this method exist?:
    - The event dictionary always returns the last thing the player did, unless they
        decide to put another input
    
    - I used this mechanic to make Pac-Man continiously move in one direction until
        the player clicked a different arrow key (which updated the event variable)

    - Solution: I created a function to make sure that the button is pressed only once
                and accounted for the event updating or staying the same
    '''
    def validate_credits_button(self, event):
        #Checks if the button has been already pressed
        if(self.credits_button_has_been_pressed is False):
            #If not, the event is copied and the button pressed has been recorded
            self.previous_button_event = event
            self.credits_button_has_been_pressed = True
        #Checks if the event is different (ex. moving the mouse to click the button again)
        else:
            #If so, the button pressed is False so that the user can switch scenes
            if(event != self.previous_button_event):
                self.credits_button_has_been_pressed = False