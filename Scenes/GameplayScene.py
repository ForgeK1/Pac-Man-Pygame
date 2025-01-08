'''
Description: The GameplayScene class helps run the levels of the game. For every level the player passes,
             the high score continues to increase and the ghosts will become more difficult
'''

#Imports pygame and other libraries
import pygame
import os
from Characters.PacMan import PacMan

class GameplayScene:
    #A constructor to initialize an instance of Gameplay Scene
    def __init__(self, display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT):
        #Initializes the display surface and game state manager
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        '''
        Sets up the Gameplay Scene surface to continiously update and blit it onto the display surface
            Note: pygame.SRCALPHA must be included to access the alpha channel so that the program
                  can change the transparency of the surface object below during runtime
        '''
        self.gameplay_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)

        #Initializes the list of obstacles for the game map
        self.list_obstacles = self.load_obstacles()

        #Initializes the character objects
        self.pac_man = PacMan(30, 30, 'Right', self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 138, True, 50)

    #A method to run the Gameplay Scene
    def run(self, event):
        #Resets the display surface background to blit a dynamically updated Gameplay Scene surface
        self.display_surface.fill('black')

        #A method to check and handle player events for the Gameplay Scene
        self.event_handler(event)

        #A method to set up the Gameplay Scene surface
        self.set_up_gameplay_surface()

        #Blits the updated Gameplay Surface onto the display surface
        self.display_surface.blit(self.gameplay_surface, (0, 0))
    
    #A method to setup and blit surface objects onto the Gameplay Scene
    def set_up_gameplay_surface(self):
        #Resets the Gameplay Scene surface background
        self.gameplay_surface.fill('black')
        
        #Sets up the obstacles on the Gameplay Scene
        for i in range(len(self.list_obstacles[0])): 
            self.gameplay_surface.blit(self.list_obstacles[1][i], self.list_obstacles[2][i])
        
        #Updates animation speed and frame of the characters
        self.pac_man.animation_update()

        #Blits the character's image and rect onto the main menu surface
        self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
    
    #A method to load obstacles into images and rects, and store then in a list
    def load_obstacles(self):
        '''
        First parameter:  [X, Y] coordinates of the image
        Second parameter: Surface object of the image
        Third parameter:  Rect of the image
        '''
        list_obstacles = ([], [], [])

        #A for loop to iterate through all files in the obstacles folder
        for filename in os.listdir('Images/Obstacles'):
            '''
            A section to grab the top left X & Y coordinate of each file as an array 
                Note: The coordinates for the file are stored in the file name
            '''
            coordinates = filename
            coordinates = coordinates.removeprefix('(')
            coordinates = coordinates.removesuffix(').png')
            coordinates = coordinates.split(',')
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            
            #Appends the coordinates in the first list
            list_obstacles[0].append(coordinates)

            #A section to grab the image and rect
            image = pygame.image.load('Images/Obstacles/' + filename)
            image_rect = image.get_rect()
            image_rect.topleft = (coordinates[0], coordinates[1])

            #Stores image in the second list and the rect in the third list
            list_obstacles[1].append(image)
            list_obstacles[2].append(image_rect)

        return list_obstacles

    #A method to check and handle player events for the Gameplay Scene
    def event_handler(self, event):
        '''
        A section to handle player events for Pac-Man
        '''

        #A method to update Pac-Man's movement
        self.pac_man.movement_update(event, self.list_obstacles)