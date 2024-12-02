'''
Description: This class contains methods for animations and interactable events for the 
             Pac-Man object
'''

#Imports pygame libraries
import pygame

class PacMan:
    #A constructor to initialize an instance of Pac Man (which is a static image)
    def __init__(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

    #A method to return Pac-Man's image
    def get_image(self):
        return self.image

    #A method to set a new image for Pac-Man
    def set_image(self, new_image):
        self.image = new_image

    #A method to return the rect of Pac-Man's image
    def get_rect(self):
        return self.rect
    
    #A method to set a new rect for Pac-Man
    def set_rect(self, new_rect):
        self.rect = new_rect

    '''
    A series of methods to set the movement frame of the character (Ex. RMF1 means Right Movement Frame 1)
    '''
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

    def set_LMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()