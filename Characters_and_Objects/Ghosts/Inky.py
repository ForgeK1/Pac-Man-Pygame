'''
Description: This class contains methods for how Inky (Cyan) functions
'''

#Imports pygame libraries
import pygame
import math
from Characters_and_Objects.Ghosts.Ghost import Ghost

class Inky(Ghost):
    #A constructor to initialize an instance of Inky (Cyan)
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed, scene_surface, game_state_manager):
        #Initializes the ghost parent class variables
        super().__init__('Inky (Cyan)', 'Images/Ghosts/Inky (Cyan)/left_frame_1.png', 
                         horizontal_scale, vertical_scale, 
                         direction, 
                         x_position, y_position, 
                         movement, character_animation_speed, 
                         scene_surface, game_state_manager)
    
    #An inherited method to update Inky's Chase State movement
    def chase_state_movement_update(self, list_obstacles, pac_man_direction, list_ghosts_positions, target):
        #Debug code
            # print(self.name + " is in his Chase State")

        #Teleports Inky to the other side of the tunnel
        self.tunnel_edge_teleport()

        #When entering Chase state & dependent on the turn_around_condition, Inky turns around 180 degrees
        self.turn_around_action()
        
        '''
        Like Pinky, Inky starts out by having his target 4 points (60 pixels in this game according to Photoshop measurement) ahead of Pac-Man, 
        so based on Pac-Man's given direction, the target gets dynamically updated
            EXCEPTION: When Pac-Man is facing up, Inky's target is 4 point left and 4 points up
        '''

        target = [target[0], target[1]] #<-- Converts tuple to an array to change its values

        if pac_man_direction == 'Up':
            target[0] = target[0] - 60 #4 points left
            target[1] = target[1] - 60 #4 points up
        elif pac_man_direction == 'Left':
            target[0] = target[0] - 60
        elif pac_man_direction == 'Down':
            target[1] = target[1] + 60
        elif pac_man_direction == 'Right': 
            target[0] = target[0] + 60

        '''
        From here, the rotate method rotates the point on Blinky's current position 180 degrees from Inky's current target point. The new
        rotated point becomes Inky's final target point
        '''

        inky_position = (target[0], target[1])
        blinky_position = list_ghosts_positions[0]

        target = self.rotate(inky_position, blinky_position, 180)
        
        #Debug code
            # print(target)

        #Returns the direction Pinky should take to chase Pac-Man
        self.direction = self.direction_update(list_obstacles, (target[0], target[1])) #<-- Converts back to tuple

        #Debug code
            # print(self.direction)

        #Updates Pinky's movement based on the given direction
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
    A helper method for Inky's chase_movement_update
        NOTE: This method was copied from https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python, 
              I did not come up with this method but it helped complete Inky's movement pattern
    '''
    def rotate(self, origin, point, angle_degrees):
        origin_x, origin_y = origin
        point_x, point_y = point

        angle = math.radians(angle_degrees)

        result_x = origin_x + math.cos(angle) * (point_x - origin_x) - math.sin(angle) * (point_y - origin_y)
        result_y = origin_y + math.sin(angle) * (point_x - origin_x) + math.cos(angle) * (point_y - origin_y)

        #This if-else chain helps convert any floating point #s (such as 6.123233995736766e-17) to 0
        if abs(result_x) < 1e-10:
            result_x = 0.0
        if abs(result_y) < 1e-10:
            result_y = 0.0

        return (result_x, result_y)

    #An inherited method to update Inky's Scatter State movement
    def scatter_state_movement_update(self, list_obstacles):
        #Debug code
            # print(self.ghost_name + ' is in his Scatter State')

        #Teleports Inky to the other side of the tunnel
        self.tunnel_edge_teleport()

        '''
        Returns the direction Inky should take to be in a scatter loop
            ex) (479, 0) is top right of the display surface window
        '''
        self.direction = self.direction_update(list_obstacles, (479, 585))

        #Debug code
            # print(self.direction)

        #Updates Inky's movement based on the given direction
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
            self.display_ghost_target_on_map((439, 605))