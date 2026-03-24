'''
Description: This class contains methods for animations and interactable events for the 
             Clyde (Orange) ghost object
'''

#Imports pygame libraries
import pygame
from Characters_and_Objects.Ghosts.Ghost import Ghost

class Clyde(Ghost):
    #A constructor to initialize an instance of Clyde
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed, level_counter, game_state_manager):
        #Initializes the Ghost parent class variables
        super().__init__('Clyde (Orange)', 'Images/Ghosts/Clyde (Orange)/left_frame_1.png', 
                         horizontal_scale, vertical_scale, 
                         direction, x_position, y_position, 
                         movement, character_animation_speed,
                         level_counter, game_state_manager)
    
    #An inherited method to update Clyde's chase state movement
    def chase_state_movement_update(self, list_obstacles, pac_man_direction, target):
        #Debug code
            # print(self.ghost_name + " is in his chase state")

        #Teleports Clyde to the other side of the tunnel
        self.tunnel_edge_teleport()

        #When entering chase state & dependent on the turn_around_condition, Clyde turns around 180 degrees
        self.chase_state_turn_around_action()

        #Returns the direction Clyde should take to chase Pac-Man
        self.direction = self.direction_update(list_obstacles, target)

        #Debug code
            # print(self.direction)

        #Updates Clyde's movement based on the given direction
        if self.direction == 'Up':
            self.rect.centery = self.rect.centery - 2
        elif self.direction == 'Left':
            self.rect.centerx = self.rect.centerx - 2
        elif self.direction == 'Down':
            self.rect.centery = self.rect.centery + 2
        elif self.direction == 'Right': 
            self.rect.centerx = self.rect.centerx + 2
    
    #An inherited method to update Clyde's scatter state movement
    def scatter_state_movement_update(self, list_obstacles):
        #Debug code
            # print(self.ghost_name + " is in his scatter state")

        #Teleports Clyde to the other side of the tunnel
        self.tunnel_edge_teleport()

        '''
        Returns the direction Clyde should take to be in a scatter loop
            Ex) (479, 0) is top right of the display surface window
        '''
        self.direction = self.direction_update(list_obstacles, (0, 585))

        #Debug code
            # print(self.direction)

        #Updates Clyde's movement based on the given direction
        if self.direction == 'Up':
            self.rect.centery = self.rect.centery - 2
        elif self.direction == 'Left':
            self.rect.centerx = self.rect.centerx - 2
        elif self.direction == 'Down':
            self.rect.centery = self.rect.centery + 2
        elif self.direction == 'Right': 
            self.rect.centerx = self.rect.centerx + 2