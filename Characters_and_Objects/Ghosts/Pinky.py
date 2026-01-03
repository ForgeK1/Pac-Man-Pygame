'''
Description: This class contains methods for animations and interactable events for the 
             Pinky (Pink) ghost object
'''

#Imports pygame libraries
import pygame
from Characters_and_Objects.Ghosts.Ghost import Ghost

class Pinky(Ghost):
    #A constructor to initialize an instance of Pinky
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed,level_counter):
        #Initializes the Ghost parent class variables
        super().__init__('Pinky (Pink)', 'Images/Ghosts/Pinky (Pink)/left_frame_1.png', 
                         horizontal_scale, vertical_scale, 
                         direction, x_position, y_position, 
                         movement, character_animation_speed,
                         level_counter)