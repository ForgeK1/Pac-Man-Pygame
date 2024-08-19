#import pygame libraries
import pygame

#Initializes all pygame modules
pygame.init()

#Creates display surface and sets its caption
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 640 
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pac-Man! - Keyvan M. Kani pygame project')

#Creating surface object image and setting it as the game's icon
game_icon_image = pygame.image.load('Images/Player/pacman_icon.png')
pygame.display.set_icon(game_icon_image)

#Create game loop
running = True
while running:
    #
    '''
    Catches all game events done by the player or during gameplay through a queue and uses them
    in a for loop
    '''
    for event in pygame.event.get():
        #Checks if the player quit the game
        if(event.type == pygame.QUIT):
            running = False
        
        #Constantly updates the display surface for any changes in runtime (blitting of images and text)
        pygame.display.update()
    
#Un-initializes all pygame modules
pygame.quit()