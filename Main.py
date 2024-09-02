'''
Description: The Main module serves to run the game through the pygame libraries, GameStateManager,
             and the dynamically updated scene instances
'''

#Imports pygame libraries and needed classes from their respective modules
import pygame
from GameStateManager import GameStateManager
from Scenes.SplashScene import SplashScene
from Scenes.MainMenuScene import MainMenuScene
from Scenes.GameplayScene import GameplayScene

#Initializes all pygame modules
pygame.init()

#Creates display surface and sets the game's caption
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pac-Man - Keyvan M. Kani Pygame Project')

#Creates surface object image and setting it as the game's icon
game_icon_image = pygame.image.load('Images/Player/pacman_icon.png')
pygame.display.set_icon(game_icon_image)

#A constant variable and a Clock object to keep track of the FPS
FPS = 60
clock = pygame.time.Clock()

'''
Sets up the game state manager to keep track of different scenes during gameplay through
keeping track of states through keys 
'''
game_state_manager = GameStateManager('Splash Screen')

#Sets up scenes of the game
splash_scene = SplashScene(display_surface, game_state_manager)
main_menu_scene = MainMenuScene(display_surface, game_state_manager)
gameplay_scene = GameplayScene(display_surface, game_state_manager)

#A dictionary that matches keys with their respective scenes to help the game state manager switch between screens of the game
list_of_states = {'Splash Screen':splash_scene, 'Main Menu Screen':main_menu_scene, 'Gameplay Screen':gameplay_scene}

#Runs the scene for the game which is the Splash Screen
list_of_states[game_state_manager.get_state()].run()

#A game loop to run the game
running = True
while running:
    #A for loop to catch all events done by the player or during gameplay and stores them in a queue to iterate through
    for event in pygame.event.get():
        #Checks if the player quit the game
        if(event.type == pygame.QUIT):
            running = False
        
        #Constantly updates the display surface for any changes in runtime (sounds, blitting of images and text, etc.)
        pygame.display.update()

        #Delays the game loop so that all computers can run at 60 frames per second for every iteration of the game loop
        clock.tick(FPS)
    
#Un-initializes all pygame modules
pygame.quit()