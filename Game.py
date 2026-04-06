'''
Description: The Game class serves to run the game through the pygame libraries, GameStateManager,
             and dynamically update the scene instances
'''

#Imports pygame libraries and needed classes from their respective modules
import pygame
from GameStateManager import GameStateManager
from Scenes.SplashScene import SplashScene
from Scenes.MainMenuScene import MainMenuScene
from Scenes.GameplayScene import GameplayScene

#Initializes all pygame modules
pygame.init()

#Creates display surface using pygame's display module
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)

#Sets the game's icon and caption
game_icon_image = pygame.image.load('Images/Pac-Man/icon.png')
pygame.display.set_icon(game_icon_image)
pygame.display.set_caption('Pac-Man - Keyvan M. Kani Pygame Project')

#A constant variable and a Clock object to keep track of the frames per second (FPS)
FPS = 60
clock = pygame.time.Clock()

'''
Sets up the Game State Manager to keep track of different scenes and running state during gameplay
    NOTE: The Game State Manager the Splash Scene when opening the game for the first time
'''
game_state_manager = GameStateManager('Splash Scene', True)

#Sets up scenes of the game
splash_scene = SplashScene(display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT)
main_menu_scene = MainMenuScene(display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT)
gameplay_scene = GameplayScene(display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT)

#A dictionary that matches keys with their respective scenes to help the Game State Manager switch between scenes of the game
list_of_states = {'Splash Scene':splash_scene, 'Main Menu Scene':main_menu_scene, 'Gameplay Scene':gameplay_scene}

#A variable to check if the player wants to enter debugging mode (by clicking 'D' or 'd' in on their keyboard)
debug_mode = False

#A game loop to run the game
while game_state_manager.get_running_state():
    #A for loop to catch all events done by the player or during gameplay and stores them in a queue to iterate through
    for event in pygame.event.get():       
        #Checks if the player quit the game
        if(event.type == pygame.QUIT):
            game_state_manager.set_running_state(False)

        #Checks if the key 'D' or 'd' was clicked for debugging mode
        if(event.type == pygame.KEYUP):
            if(event.key == pygame.K_d):
                if(debug_mode):
                    debug_mode = False
                else:
                    debug_mode = True

    '''
    Continuously runs the current scene the Game State Manager focuses on based on current game and player events
        NOTE: We pass the event so that the run method can handle any events done by the player
              or to enter debugging mode
    '''
    list_of_states[game_state_manager.get_scene_state()].run(event, debug_mode)

    #Constantly updates the display surface for any changes in runtime (sounds, blitting of images and text, etc.)
    pygame.display.update()
    
    #Delays the game loop so that all machines/computers can run at 60 FPS for every iteration of the game loop
    dt = clock.tick(FPS)
    game_state_manager.set_clock_delta_time(dt)
    
#Un-initializes all pygame modules
pygame.quit()