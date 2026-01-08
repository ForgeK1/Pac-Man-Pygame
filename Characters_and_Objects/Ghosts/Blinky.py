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