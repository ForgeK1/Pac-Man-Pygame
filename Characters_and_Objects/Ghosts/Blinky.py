'''
Description: This class contains methods for animations and interactable events for the 
             Blinky (Red) ghost object
'''

#Imports pygame libraries & needed classes for their respective modules
import pygame
from Characters_and_Objects.Ghosts.Ghost import Ghost

class Blinky(Ghost):
    #A constructor to initialize an instance of Blinky
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed, level_counter, game_state_manager):
        #Initializes the Ghost parent class variables
        super().__init__('Blinky (Red)', 'Images/Ghosts/Blinky (Red)/left_frame_1.png', 
                         horizontal_scale, vertical_scale, 
                         direction, x_position, y_position, 
                         movement, character_animation_speed,
                         level_counter, game_state_manager)
    
    #An inherited method to update Blinky's chase state movement
    def chase_state_movement_update(self, list_obstacles, target):
        #Debug code
            # print(self.ghost_name + " is in his chase state")

        #Teleports Blinky to the other side of the tunnel
        self.tunnel_edge_teleport()

        #Returns the direction Blinky should take to chase Pac-Man
        self.direction = self.direction_update(list_obstacles, target)

        #Debug code
            # print(self.direction)

        #Updates Blinky's movement based on the given direction
        if self.direction == 'Up':
            self.rect.centery = self.rect.centery - 2
        elif self.direction == 'Left':
            self.rect.centerx = self.rect.centerx - 2
        elif self.direction == 'Down':
            self.rect.centery = self.rect.centery + 2
        elif self.direction == 'Right': 
            self.rect.centerx = self.rect.centerx + 2
    
    #An inherited method to update Blinky's scatter state movement
    def scatter_state_movement_update(self, list_obstacles):
        #Debug code
            # print(self.ghost_name + " is in his scatter state")

        #Teleports Blinky to the other side of the tunnel
        self.tunnel_edge_teleport()

        '''
        Returns the direction Blinky should take to be in a scatter loop
            Ex) (479, 0) is top right of the display surface window
        '''
        self.direction = self.direction_update(list_obstacles, (479, 0))

        #Debug code
            # print(self.direction)

        #Updates Blinky's movement based on the given direction
        if self.direction == 'Up':
            self.rect.centery = self.rect.centery - 2
        elif self.direction == 'Left':
            self.rect.centerx = self.rect.centerx - 2
        elif self.direction == 'Down':
            self.rect.centery = self.rect.centery + 2
        elif self.direction == 'Right': 
            self.rect.centerx = self.rect.centerx + 2