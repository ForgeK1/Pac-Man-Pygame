'''
Description: The Game class serves to run the game through the pygame libraries, GameStateManager,
             and dynamically update the scene instances
'''

#Imports pygame libraries and needed classes from their respective modules
import pygame
import asyncio
from GameStateManager import GameStateManager
from Scenes.SplashScene import SplashScene
from Scenes.MainMenuScene import MainMenuScene
from Scenes.GameplayScene import GameplayScene

class Game():
    def __init__(self):
        #Initializes all pygame modules
        pygame.init()

        #Creates display surface using pygame's display module
        self.WINDOW_WIDTH = 480
        self.WINDOW_HEIGHT = 640 
        self.display_surface = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)

        #Sets the game's icon and caption
        self.game_icon_image = pygame.image.load('Images/Pac-Man/icon.png')
        pygame.display.set_icon(self.game_icon_image)
        pygame.display.set_caption('Pac-Man - Keyvan M. Kani Pygame Project')

        #A constant variable and a Clock object to keep track of the frames per second (FPS)
        self.FPS = 60
        self.clock = pygame.time.Clock()

        '''
        Sets up the Game State Manager to keep track of different scenes and running state during gameplay
            NOTE: The Game State Manager the Splash Scene when opening the game for the first time
        '''
        self.game_state_manager = GameStateManager('Splash Scene', True)

        #Sets up scenes of the game
        self.splash_scene = SplashScene(self.display_surface, self.game_state_manager, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.main_menu_scene = MainMenuScene(self.display_surface, self.game_state_manager, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)
        self.gameplay_scene = GameplayScene(self.display_surface, self.game_state_manager, self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        #A dictionary that matches keys with their respective scenes to help the Game State Manager switch between scenes of the game
        self.list_of_states = {'Splash Scene':self.splash_scene, 'Main Menu Scene':self.main_menu_scene, 'Gameplay Scene':self.gameplay_scene}

        #A variable to check if the player wants to enter debugging mode (by clicking 'D' or 'd' in on their keyboard)
        self.debug_mode = False

    async def run(self):
        #A game loop to run the game
        while self.game_state_manager.get_running_state():
            #A for loop to catch all events done by the player or during gameplay and stores them in a queue to iterate through
            for event in pygame.event.get():     
                #Checks if the player quit the game  
                if(event.type == pygame.QUIT):
                    self.game_state_manager.set_running_state(False)

                #Checks if the key 'D' or 'd' was clicked for debugging mode
                if(event.type == pygame.KEYUP):
                    if(event.key == pygame.K_d):
                        if(self.debug_mode):
                            self.debug_mode = False
                        else:
                            self.debug_mode = True

            '''
            Continuously runs the current scene the Game State Manager focuses on based on current game and player events
                NOTE: We pass the event so that the run method can handle any events done by the player
                    or to enter debugging mode
            '''
            self.list_of_states[self.game_state_manager.get_scene_state()].run(event, self.debug_mode)

            #Constantly updates the display surface for any changes in runtime (sounds, blitting of images and text, etc.)
            pygame.display.flip()
            
            #Delays the game loop so that all machines/computers can run at 60 FPS for every iteration of the game loop
            dt = self.clock.tick(self.FPS)
            self.game_state_manager.set_clock_delta_time(dt)

            # #This must include this statement for the main loop. Keep the argument at 0
            await asyncio.sleep(0)
            
        #Un-initializes all pygame modules
        pygame.quit()
        
if __name__ == '__main__':
    game = Game()
    asyncio.run(game.run())