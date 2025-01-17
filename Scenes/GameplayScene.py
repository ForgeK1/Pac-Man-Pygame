'''
Description: The GameplayScene class helps run the levels of the game. For every level the player passes,
             the high score continues to increase and the ghosts will become more difficult
'''

#Imports pygame and other libraries
import pygame
import os
from Characters.PacMan import PacMan
from Characters.Blinky import Blinky
from Characters.Pinky import Pinky
from Characters.Inky import Inky
from Characters.Clyde import Clyde
import csv

class GameplayScene:
    #A constructor to initialize an instance of Gameplay Scene
    def __init__(self, display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT, start):
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

        #Initializes the list of pellets for the game map
        self.list_power_pellets = self.load_power_pellets()
        self.list_pellets = self.load_pellets()

        #Initializes the character objects
        self.pac_man = PacMan(30, 30, 'Left', self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 138, True, 50)
        self.blinky = Blinky(30, 30, "Left", self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 68, True, 100)
        self.pinky = Pinky(30, 30, "Down", self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 20, True, 100)
        self.inky = Inky(30, 30, "Up", self.WINDOW_WIDTH / 2 - 33, self.WINDOW_HEIGHT / 2 - 20, True, 100)
        self.clyde = Clyde(30, 30, "Up", self.WINDOW_WIDTH / 2 + 33, self.WINDOW_HEIGHT / 2 - 20, True, 100)

        #Initializes pygame mixer channels for utilizing music or sound effects
        self.pac_man_channel = pygame.mixer.Channel(0)
        self.ghost_channel = pygame.mixer.Channel(1)

        #Initializes music and sound effects
        self.pac_man_pellet_sound = pygame.mixer.Sound('Audio/Sound Effects/Waka (Cut Version).wav')
        self.pac_man_power_pellet_sound = pygame.mixer.Sound('Audio/Sound Effects/Power-Up.wav')
        self.ghost_siren_v1_sound = pygame.mixer.Sound('Audio/Sound Effects/Ghost Siren V1.wav')
        self.ghost_siren_v2_sound = pygame.mixer.Sound('Audio/Sound Effects/Ghost Siren V2.wav')

        #Initializes a variable to check if the player is starting a new round in the Gameplay Scene for the very first time
        self.start = start

    #A method to run the Gameplay Scene
    def run(self, event):
        #An if statement to check if the player is seeing the Gameplay Scene for the first time
        if(self.start):
            self.start_round()
        else:
            #Fills the background of the display surface
            self.display_surface.fill('black')
            
            #A method to check and handle player events for the Gameplay Scene
            self.event_handler(event)

            #A method to set up the updated Gameplay Scene surface
            self.set_up_gameplay_surface()

            #Blits the Gameplay Scene surface onto the display surface
            self.display_surface.blit(self.gameplay_surface, (0, 0))
    
    #A method to setup and blit surface objects onto the Gameplay Scene
    def set_up_gameplay_surface(self):        
        #Resets the Gameplay Scene background
        self.gameplay_surface.fill('black')
        
        #Updates all character animation based on the character_animation_speed variable
        self.pac_man.animation_update()
        self.blinky.animation_update()
        self.pinky.animation_update()
        self.inky.animation_update()
        self.clyde.animation_update()

        #Blits all character images and rects onto the Gameplay Scene
        self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
        self.gameplay_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
        self.gameplay_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
        self.gameplay_surface.blit(self.inky.get_image(), self.inky.get_rect())
        self.gameplay_surface.blit(self.clyde.get_image(), self.clyde.get_rect())
    
        #Sets up the obstacles on the Gameplay Scene
        for i in range(len(self.list_obstacles[0])): 
            self.gameplay_surface.blit(self.list_obstacles[1][i], self.list_obstacles[2][i])

        #Sets up the power pellets on the Gameplay Scene
        for i in range(len(self.list_power_pellets[0])):
            if(self.list_power_pellets[1][i]):
                self.gameplay_surface.blit(self.list_power_pellets[2], self.list_power_pellets[3][i])            
        
        #Sets up the pellets on the Gameplay Scene
        for i in range(len(self.list_pellets[0])):
            if(self.list_pellets[1][i]):
                self.gameplay_surface.blit(self.list_pellets[2], self.list_pellets[3][i])
    
    #A method to load obstacles' coordinates, images, and rects to store each respectivly in their lists
    def load_obstacles(self):
        '''
        First parameter:  [X, Y] coordinates of the image
        Second parameter: Surface object of the image
        Third parameter:  Rect of the image
        '''
        list_obstacles = ([], [], [])

        #A for loop to iterate through all image files in the obstacles folder
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

            '''
            A section to grab the image and rect of the file
            '''
            image = pygame.image.load('Images/Obstacles/' + filename)
            image_rect = image.get_rect()
            image_rect.topleft = (coordinates[0], coordinates[1])

            #Stores image in the second list and the rect in the third list
            list_obstacles[1].append(image)
            list_obstacles[2].append(image_rect)

        return list_obstacles
    
    #A method to load power pellets' coordinates, hidden boolean, images, and rects to store each respectivly in their lists
    def load_power_pellets(self):
        power_pellet_image = pygame.transform.scale(pygame.image.load('Images/Pellets/power_pellet.png'), (16, 16))
        
        '''
        First parameter:  [X, Y] coordinates of the image
        Second parameter: Boolean of whether the pellet should be hidden or shown on the map
        Third parameter:  Surface object of the image
        Fourth parameter: Rect of the image
        '''
        list_power_pellets = ([], [], power_pellet_image, [])

        #Opens the Power Pellets CSV file 
        with open('Images/Pellets/power_pellets_coordinates.csv') as fileObject:
            #next() is used so that we skip the header row. Ex) ['X', 'Y', 'Hidden']
            next(fileObject)
            
            #Creates a reader object by passing in the file
            reader = csv.reader(fileObject)

            #A for loop to iterate through each row
            for row in reader:
                '''
                A section to grab and record the coordinates in the first list
                '''
                coordinates = [int(row[0]), int(row[1])]
                list_power_pellets[0].append(coordinates)

                '''
                A section to grab and record the boolean in the second list
                '''
                list_power_pellets[1].append(row[2])

                '''
                A section to grab and record the updated rect position in the fourth list
                    Note: Since all power pellets share the same image, then the third parameter is not a list
                '''
                power_pellet_image_rect = power_pellet_image.get_rect()
                power_pellet_image_rect.topleft = coordinates
                list_power_pellets[3].append(power_pellet_image_rect)

                #Debug code
                    #print(row)
            
            return list_power_pellets
        
    #A method to load pellets' coordinates, hidden boolean, images, and rects to store each respectivly in their lists
    def load_pellets(self):
        pellet_image = pygame.transform.scale(pygame.image.load('Images/Pellets/pellet.png'), (4, 4)) 

        '''
        First parameter:  [X, Y] coordinates of the image
        Second parameter: Boolean of whether the pellet should be hidden or shown on the map
        Third parameter:  Surface object of the image
        Fourth parameter: Rect of the image
        '''
        list_pellets = ([], [], pellet_image, [])
            
        with open('Images/Pellets/pellets_coordinates.csv') as fileObject:
            next(fileObject)
            reader = csv.reader(fileObject)

            for row in reader:
                coordinates = [int(row[0]), int(row[1])]
                list_pellets[0].append(coordinates)

                list_pellets[1].append(row[2])

                pellet_image_rect = pellet_image.get_rect()
                pellet_image_rect.topleft = coordinates
                list_pellets[3].append(pellet_image_rect)
        
        return list_pellets

    #A method to showcase the start of the round to the player
    def start_round(self):
        #Checks if the Pac-Man start theme is still playing. If the theme ends, then the Pac-Man & the ghosts start moving
        if(pygame.mixer_music.get_busy() is False):
            self.start = False
            pygame.mixer_music.unload()
        
        #Resets the Gameplay Scene background
        self.gameplay_surface.fill('black')
        
        #Sets up the obstacles on the Gameplay Scene
        for i in range(len(self.list_obstacles[0])): 
            self.gameplay_surface.blit(self.list_obstacles[1][i], self.list_obstacles[2][i])
        
        #Sets up the power pellets on the Gameplay Scene
        for i in range(len(self.list_power_pellets[0])):
            if(self.list_power_pellets[1][i]):
                self.gameplay_surface.blit(self.list_power_pellets[2], self.list_power_pellets[3][i])
        
        #Sets up the pellets on the Gameplay Scene
        for i in range(len(self.list_pellets[0])):
            if(self.list_pellets[1][i]):
                self.gameplay_surface.blit(self.list_pellets[2], self.list_pellets[3][i])
        
        '''
        A section to dynamically showcase text based on the number of seconds left in the Pac-Man start theme
        '''

        pixel_font = pygame.font.Font('Fonts/Pixel/DePixelHalbfett.ttf', 18)

        #Displays the "READY!" text throughout the entire theme
        ready_text = pixel_font.render('READY!', True, 'Yellow')
        ready_text_rect = ready_text.get_rect()
        ready_text_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 35)

        self.gameplay_surface.blit(ready_text, ready_text_rect)

        #Displays the "PLAYER ONE" text up to 3 seconds of the theme
        if(pygame.mixer_music.get_pos() / 1000 >= 0.01 and pygame.mixer_music.get_pos() / 1000 <= 2.5):
            player_one_text = pixel_font.render('PLAYER ONE', True, 'Cyan')
            player_one_text_rect = player_one_text.get_rect()
            player_one_text_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 68)

            self.gameplay_surface.blit(player_one_text, player_one_text_rect)
        #Else, the program displays the characters and their positions before the theme ends
        else:
            self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
            self.gameplay_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
            self.gameplay_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
            self.gameplay_surface.blit(self.inky.get_image(), self.inky.get_rect())
            self.gameplay_surface.blit(self.clyde.get_image(), self.clyde.get_rect())

        #Blits the Gameplay Scene surface onto the display surface
        self.display_surface.blit(self.gameplay_surface, (0, 0))

    #A method to check and handle events for the Gameplay Scene
    def event_handler(self, event):
        '''
        A section to handle player events for Pac-Man
        '''

        #A method to update Pac-Man's movement
        self.pac_man.movement_update(event, self.list_obstacles)

        #A method to allow Pac-Man to eat pellets
        self.pac_man.eat_pellets(self.list_pellets, self.list_power_pellets, 
                                 self.pac_man_channel, self.ghost_channel,
                                 self.pac_man_pellet_sound, self.pac_man_power_pellet_sound)
        
        #Checks if Pac-Man ate a power pellet. If so, then the ghosts will scatter instead of chasing Pac-Man
        if(self.ghost_channel.get_busy() is False):
            self.ghost_channel.play(self.ghost_siren_v1_sound)