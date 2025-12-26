#Import pygame
import pygame

#Initialize all pygame modules
pygame.init()

#Create a display surface that will be visible on your game window and sets its caption
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
pygame.display.set_caption("Pygame Syntax Practice")

#Create a surface object image and set it as the game's icon
game_icon_image = pygame.image.load('Images/Pac-Man/icon.png')
pygame.display.set_icon(game_icon_image)

#Create a framerate variable and a Clock object to keep track of the FPS
FPS = 120
clock = pygame.time.Clock()

#Create a game loop
running = True
while running:
    #Create a for loop that will catch all events done by the player or during gameplay and stores them in a queue to iterate through
    for event in pygame.event.get():
        #Check if the player quit the game
        if event.type == pygame.QUIT:
            running = False
    
    #Add a line of code that will constantly update the display surface (using pygame's display module) to detect any changes in runtime (sounds, blitting of images and text, etc.)
    pygame.display.update()

    #Add a line of code to tick the clock after each loop
    clock.tick(FPS)

#Un-initialize all pygame modules
pygame.quit()