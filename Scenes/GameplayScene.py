'''
Description: The GameplayScene class helps run the levels of the game. For every level the player passes,
             the high score continues to increase and the ghosts will become more difficult
'''

#Imports pygame libraries
import pygame

class GameplayScene:
    def __init__(self, display_surface, game_state_manager):
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager

    def run(self):
        self.display_surface.fill('blue')