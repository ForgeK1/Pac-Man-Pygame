'''
Description: The Credits Scene class displays who created the game, who owns the copyright, and what the project was about
'''

#Import pygame libraries
import pygame
from Functions.Button import Button

class CreditsScene:
    #A constructor to initialize an instance of a Credits Scene
    def __init__(self, display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT):
        #A constructor to initialize the display surface and Game State Manager
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        '''
        Sets up the Credits Scene surface to blit onto the display surface
            NOTE: pygame.SRCALPHA must be included to access the alpha channel so that the program
                          can change the transparency of the surface object below during runtime 
        '''
        self.credits_scene = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)

        #A back button variable for the player to return to the main menu
        self.back_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                  'black', 'black', 'black', 'Back', 'Fonts/Pixel/DePixelHalbfett.ttf', 12)

        #Variables to ensure the back button has been pressed only once
        self.previous_button_event = None
        self.back_button_has_been_pressed = False

    #A method to run the Credts Scene
    def run(self, event, debug_mode):
        #Fills up the background color of the display surface
        self.display_surface.fill('black')

        #A method to continiously update the Credits Scene surface
        self.set_up_credits_surface()

        #A method to check and handle player events for the Credits Scene
        self.event_handler(event)

        #Blits the Credits Scene surface onto the display surface
        self.display_surface.blit(self.credits_scene, (0, 0))

    #A method to set up and blit the surface objects onto the Splash Scene
    def set_up_credits_surface(self):
        #Fills up the background color of the Credits Scene
        self.credits_scene.fill('black')

        #Sets up the background menu
        background_menu = pygame.image.load('Images/Main Menu Background.png')
        background_menu_rect = background_menu.get_rect()
        background_menu_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2)

        #Blits the background menu
        self.credits_scene.blit(background_menu, background_menu_rect)

        #Sets up the GitHub profile picture of pygame's author (which is me :D)
        author_image = pygame.image.load('Images/other/GitHub pfp.png')
        author_image = pygame.transform.scale(author_image, (100, 100))
        author_image_rect = author_image.get_rect()
        author_image_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 80)

        #Blits the profile image onto the Credits Scene surface
        self.credits_scene.blit(author_image, author_image_rect)

        #Sets up an interactable back button
        self.set_up_back_button()

    #A method to set up the back button
    def set_up_back_button(self):
        #Sets up the button
        self.back_button.scale_button(95, 37, 16)
        self.back_button.get_image_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 280)
        self.back_button.get_text_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 282)

        #Blits the button's image & text onto the Credits Scene
        self.credits_scene.blit(self.back_button.get_image(), self.back_button.get_image_rect())
        self.credits_scene.blit(self.back_button.get_text(), self.back_button.get_text_rect())

    #A method to check and handle player events for the Main Menu Scene
    def event_handler(self, event):
        '''
        A section to handle player events for interacting with the play & credits buttons
        '''

        #Ensures the back button has been pressed only once
        self.validate_back_button(event)
        
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

        '''
        If (1) the player clicked and let go of the play button and
           (2) the button hasn't been pressed before
        
        They will be directed to the Main Menu Scene
        '''
        if(self.back_button.check_input(mouse_pos, mouse_click, mouse_let_go) and
           self.back_button_has_been_pressed is False):
            self.game_state_manager.set_scene_state('Main Menu Scene')

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
    def validate_back_button(self, event):
        #Checks if the button has been already pressed
        if(self.back_button_has_been_pressed is False):
            #If not, the event is copied and the button pressed has been recorded
            self.previous_button_event = event
            self.back_button_has_been_pressed = True
        #Checks if the event is different (ex. moving the mouse to click the button again)
        else:
            #If so, the button pressed is False so that the user can switch scenes
            if(event != self.previous_button_event):
                self.back_button_has_been_pressed = False