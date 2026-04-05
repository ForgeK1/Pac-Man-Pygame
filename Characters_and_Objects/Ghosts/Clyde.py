'''
Description: This class contains methods for animations and interactable events for the 
             Clyde (Orange) ghost object
'''

#Imports pygame libraries
import pygame
import math
from Characters_and_Objects.Ghosts.Ghost import Ghost

class Clyde(Ghost):
    #A constructor to initialize an instance of Clyde
    def __init__(self, scene_surface, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed, level_counter, game_state_manager):
        #Initializes the Ghost parent class variables
        super().__init__(scene_surface,
                         'Clyde (Orange)', 'Images/Ghosts/Clyde (Orange)/left_frame_1.png', 
                         horizontal_scale, vertical_scale, 
                         direction, 
                         x_position, y_position, 
                         movement, character_animation_speed, 
                         level_counter, game_state_manager)
    
    #An inherited method to update Clyde's chase state movement
    def chase_state_movement_update(self, list_obstacles, pac_man_direction, list_ghosts_positions, target):
        #Debug code
            # print(self.ghost_name + " is in his chase state")

        #Teleports Clyde to the other side of the tunnel
        self.tunnel_edge_teleport()

        #When entering Chase state & dependent on the turn_around_condition, Clyde turns around 180 degrees
        self.turn_around_action()

        #Debug code
        if(self.debug_mode):
            pygame.draw.circle(self.scene_surface, 'Orange', target, 150, 2) #Shows whether Clyde is inside Pac-Man's circle based on the pac_man_detector method

        #Detects if Clyde is in Pac-Man's radius to chase him
        target = self.pac_man_detector(target)

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

        #Debug code
        if(self.debug_mode):
            self.display_ghost_target_on_map(target)

    '''
    A helper method to determine if Clyde's center point is in the circle of Pac-Man 
    
    Given the following formula: (x_2 - x_1)^2 + (y_2 - y_1)^2 <= radius^2 
       NOTE: Where (x_1, y_1) is Pac-Man's position and (x_2, y_2) is Clyde's position
    '''
    def pac_man_detector(self, target):
        #Debug code 

        #Calculates the difference between the two points
        x_value = math.pow((self.rect.centerx - target[0]), 2)
        y_value = math.pow((self.rect.centery - target[1]), 2)

        #Calculates the result
        inside_circle = x_value + y_value <= math.pow(150, 2) #For Clyde, the Pac-Man's radius will be 150 in this game

        '''
        If the value is less than or equal to r^2, then Clyde is inside the circle and will chase him.
        Else, Clyde's target would be the same as his Scatter state
        '''
        if(inside_circle):
            return target
        else:
            return (40, 605)
    
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
        self.direction = self.direction_update(list_obstacles, (40, 585))

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
        
        #Debug code
        if(self.debug_mode):
            self.display_ghost_target_on_map((40, 605))