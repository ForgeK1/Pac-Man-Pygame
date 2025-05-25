'''
Description: The Game module serves to run the game through the pygame libraries, GameStateManager,
             and the dynamically updated scene instances
'''

#Imports pygame libraries and needed classes from their respective modules
import pygame #type: ignore
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

#A constant variable and a Clock object to keep track of the FPS
FPS = 60
clock = pygame.time.Clock()

'''
Sets up the game state manager to keep track of different scenes and running state during gameplay
    Note: Runs the Splash Scene when opening the game for the first time
'''
game_state_manager = GameStateManager('Main Menu Scene', True)

#Sets up scenes of the game
splash_scene = SplashScene(display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT)
main_menu_scene = MainMenuScene(display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT)
gameplay_scene = GameplayScene(display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT)

#A dictionary that matches keys with their respective scenes to help the game state manager switch between scenes of the game
list_of_states = {'Splash Scene':splash_scene, 'Main Menu Scene':main_menu_scene, 'Gameplay Scene':gameplay_scene}

#A game loop to run the game
while game_state_manager.get_running_state():
    #A for loop to catch all events done by the player or during gameplay and stores them in a queue to iterate through
    for event in pygame.event.get():       
        #Checks if the player quit the game
        if(event.type == pygame.QUIT):
            game_state_manager.set_running_state(False)
    
    '''
    Continuously runs the current scene the game state manager focuses on based on current player events
        Note: We pass in the event so that the run method can handle any events done by the player
              to perform specific tasks (Ex. clicking the play button in the Main Menu Scene)
    '''
    list_of_states[game_state_manager.get_scene_state()].run(event)

    #Constantly updates the display surface for any changes in runtime (sounds, blitting of images and text, etc.)
    pygame.display.update()
    
    #Delays the game loop so that all computers can run at 60 frames per second for every iteration of the game loop
    clock.tick(FPS)
    
#Un-initializes all pygame modules
pygame.quit()