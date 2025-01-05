'''
Description: The Main Menu Scene class serves to help the player to navigate the game
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

        '''
        Sets up the Main Menu Scene surface to continiously update and blit it onto the display surface
            Note: pygame.SRCALPHA must be included to access the alpha channel so that the program
                  can change the transparency of the surface object below during runtime
        '''
        self.main_menu_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)

        #Initializes the character objects
        self.blinky = Blinky(70, 70, "Right", 80, self.WINDOW_HEIGHT / 2 - 100)
        self.pinky = Pinky(70, 70, "Right", 180, self.WINDOW_HEIGHT / 2 - 100)
        self.inky = Inky(70, 70, "Right", 80,self.WINDOW_HEIGHT / 2)
        self.clyde = Clyde(70, 70, "Right", 180, self.WINDOW_HEIGHT / 2)
        self.pac_man = PacMan(70, 70, "Right", 320, self.WINDOW_HEIGHT / 2 - 50, True, 100)
        self.power_pellet_image = pygame.image.load('Images/Dots/power_pellet.png')

        #Initializes variables to control character animation (speed)
        self.character_animation_speed = 100 #In miliseconds
        self.last_updated_time = 0 #In miliseconds

        #Initializes the interactable buttons
        self.play_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                  'Play', "black", "black", "black", 'Fonts/Pixel/DePixelHalbfett.ttf', 24)
        self.quit_button = Button('Images/Button/non_highlighted.png', 'Images/Button/highlighted.png', 'Images/Button/pressed.png', 
                                  'Quit', "black", "black", "black", 'Fonts/Pixel/DePixelHalbfett.ttf', 24)
    
    #A method to run Main Menu Scene
    def run(self, event):        
        #Resets the display surface background to blit a dynamically updated Main Menu Scene surface
        self.display_surface.fill('black')

        #A method to set up the Main Menu Surface
        self.set_up_main_menu_surface()

        #Blits the updated Main Menu Surface onto the display surface
        self.display_surface.blit(self.main_menu_surface, (0, 0))

        #Checks and handles player events for the Main Menu Scene
        self.event_handler(event)

    #A method to setup and blit surface objects onto the Main Menu Scene
    def set_up_main_menu_surface(self):
        #Fills the background color of the Main Menu Scene
        #self.main_menu_surface.fill("black")

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

        #Updates all character animation based on the character_animation_speed variable
        self.pac_man.animation_update()
        self.character_animation_update()
        
        self.main_menu_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())

        #Sets up interactable buttons
        self.set_up_buttons()
    
    #A method to update the animation speed of all characters in the Main Menu Scene
    def character_animation_update(self):
        #Gets the current time in miliseconds
        curr_time = pygame.time.get_ticks()

        #A variable to keep track of changing frame of characters
        change_frame = False

        '''
        Updates the animation frame of each character if enough time has passed
            Ex) 0 - 0 > 200     False
                100 - 0 > 200   False
                201 - 0 > 200   True  --> 
                201 - 201 > 200 False
                ...
                402 - 201 > 200 True -->
                402 - 402 > 200 
                ... and so on
        '''
        if curr_time - self.last_updated_time > self.character_animation_speed:
            #Sets change frame to True 
            change_frame = True

            #Sets up a new time
            self.last_updated_time = curr_time
        
        #Updates character frames
        self.character_frame_update(change_frame)

    #A method to update the frame of all characters in the Main Menu Scene
    def character_frame_update(self, change_frame):
        #Updates frames and movement positions of each character
        if(change_frame):
            self.blinky.update_frame()
            self.pinky.update_frame()
            self.inky.update_frame()
            self.clyde.update_frame()

        #Sets up the Power Pellet image
        self.power_pellet_image = pygame.transform.scale(self.power_pellet_image, (40, 40))
        self.power_pellet_image_rect = self.power_pellet_image.get_rect()
        self.power_pellet_image_rect.center = (415, self.WINDOW_HEIGHT / 2 - 50)

        #Blits the images onto the main menu surface after the updates frames
        self.main_menu_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
        self.main_menu_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
        self.main_menu_surface.blit(self.inky.get_image(), self.inky.get_rect())
        self.main_menu_surface.blit(self.clyde.get_image(), self.clyde.get_rect())
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
    
    #A method to check and handle player events for the Main Menu Scene
    def event_handler(self, event):
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

        #Uses the event type to check if the player has clicked or let go of the *left* mouse button
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
        
        #After clicking and letting go of the play button, the player is directed to the Gameplay Scene
        if(self.play_button.check_input(mouse_pos, mouse_click, mouse_let_go)):
            #Stops playing and unloads the Pac-Man theme music from the mixer
            pygame.mixer_music.stop()
            pygame.mixer_music.unload()
            
            self.game_state_manager.set_scene_state('Gameplay Scene')

        #After clicking and letting go of the quit button, the program convert running to False to stop the game loop in the Game class
        if(self.quit_button.check_input(mouse_pos, mouse_click, mouse_let_go)):
            self.game_state_manager.set_running_state(False)
        
        #Debug code to ensure that the function contains all the events done by the player 
            #print(event.dict)
            #print(mouse_pos)