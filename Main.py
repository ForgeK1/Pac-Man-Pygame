#Imports pygame libraries
import pygame
import sys

#Initializes all pygame modules
pygame.init()

#Creates display surface and sets its caption
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pac-Man! - Keyvan M. Kani Pygame project')

#Creates surface object image and setting it as the game's icon
game_icon_image = pygame.image.load('Images/Player/pacman_icon.png')
pygame.display.set_icon(game_icon_image)

#A game loop to run the game
running = True
while running:
    #A for loop to catch all events done by the player or during gameplay and stores them in a queue to iterate through
    for event in pygame.event.get():
        #Checks if the player quit the game
        if(event.type == pygame.QUIT):
            running = False
        
        #Constantly updates the display surface for any changes in runtime (sounds, blitting of images and text, etc.)
        pygame.display.update()
    
#Un-initializes all pygame modules
pygame.quit()