'''
Description: This class contains methods for how Blinky (Red) ghost functions
'''

#Imports pygame libraries & needed classes for their respective modules
import pygame
from Characters_and_Objects.Ghosts.Ghost import Ghost

class Blinky(Ghost):
    #A constructor to initialize an instance of Blinky (Red)
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed, scene_surface, game_state_manager):
        #Initializes the ghost parent class variables
        super().__init__('Blinky (Red)', 'Images/Ghosts/Blinky (Red)/left_frame_1.png', 
                         horizontal_scale, vertical_scale, 
                         direction, 
                         x_position, y_position, 
                         movement, character_animation_speed,  
                         scene_surface, game_state_manager)
    
    #An inherited method to update Blinky's Chase State movement
    def chase_state_movement_update(self, list_obstacles, pac_man_direction, list_ghosts_positions, target):
        #Debug code
            # print(self.ghost_name + " is in his Chase State")

        #Teleports Blinky to the other side of the tunnel
        self.tunnel_edge_teleport()

        #When entering Chase state & dependent on the turn_around_condition, Blinky turns around 180 degrees
        self.turn_around_action()

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

        #Debug code
        if(self.debug_mode):
            self.display_ghost_target_on_map(target)
    
    #An inherited method to update Blinky's Scatter State movement
    def scatter_state_movement_update(self, list_obstacles):
        #Debug code
            # print(self.ghost_name + " is in his Scatter State")

        #Teleports Blinky to the other side of the tunnel
        self.tunnel_edge_teleport()

        '''
        Returns the direction Blinky should take to be in a scatter loop
            ex) (479, 0) is top right of the display surface window
        '''
        self.direction = self.direction_update(list_obstacles, (459, 0))

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

        #Debug code
        if(self.debug_mode):
            self.display_ghost_target_on_map((439, 10))