'''
Description: This class contains methods for animations and interactable events for the 
             Pinky (Pink) ghost object
'''

#Imports pygame libraries
import pygame
from Characters_and_Objects.Ghosts.Ghost import Ghost

class Pinky(Ghost):
    #A constructor to initialize an instance of Pinky
    def __init__(self, scene_surface, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed,level_counter, game_state_manager):
        #Initializes the Ghost parent class variables
        super().__init__(scene_surface,
                         'Pinky (Pink)', 'Images/Ghosts/Pinky (Pink)/left_frame_1.png', 
                         horizontal_scale, vertical_scale, 
                         direction, 
                         x_position, y_position, 
                         movement, character_animation_speed, 
                         level_counter, game_state_manager)
        
    #An inherited method to update Pinky's chase state movement
    def chase_state_movement_update(self, list_obstacles, pac_man_direction, list_ghosts_positions, target):
        #Debug code
            # print(self.name + " is in his chase state")

        #Teleports Pinky to the other side of the tunnel
        self.tunnel_edge_teleport()

        #When entering Chase state & dependent on the turn_around_condition, Pinky turns around 180 degrees
        self.turn_around_action()
        
        '''
        Pinky's target is always 4 points (60 pixels in this game according to Photoshop measurement) ahead of Pac-Man, so based on Pac-Man's given
        direction, the target gets dynamically updated
            EXCEPTION: When Pac-Man is facing up, Pinky's target is 4 point left and 4 points up
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
        self.display_ghost_target_on_map(target)
    
    #An inherited method to update Pinky's scatter state movement
    def scatter_state_movement_update(self, list_obstacles):
        #Debug code
            # print(self.ghost_name + " is in his scatter state")

        #Teleports Pinky to the other side of the tunnel
        self.tunnel_edge_teleport()

        '''
        Returns the direction Pinky should take to be in a scatter loop
            Ex) (479, 0) is top right of the display surface window
        '''
        self.direction = self.direction_update(list_obstacles, (40, 10))

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
        self.display_ghost_target_on_map((40, 10))