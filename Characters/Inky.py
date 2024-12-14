'''
Description: This class contains methods for animations and interactable events for the 
             Inky (Cyan) ghost object
'''

#Imports pygame libraries
import pygame

class Inky:
    #A constructor to initialize an instance of Inky
    def __init__(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

        '''
        Variables to keep track of current movement frame and direction of the ghost
            Ex) ghost_frame has 2 movement frames and pac_man_frame has 3 movement frames for 
                any direction of movement
        '''
        self.frame = 0
        self.direction = 'right'

    #A method to return Inky's image
    def get_image(self):
        return self.image

    #A method to set a new image for Inky
    def set_image(self, new_image):
        self.image = new_image

    #A method to return the rect of Inky's image
    def get_rect(self):
        return self.rect
    
    #A method to set a new rect for Inky
    def set_rect(self, new_rect):
        self.rect = new_rect
    
    #A method to return Inky's current frame
    def get_frame(self):
        return self.frame
    
    #A method to set a new frame for Inky
    def set_frame(self, new_frame):
        self.frame = new_frame
    
    #A method to return Inky's current direction
    def get_direction(self):
        return self.direction
    
    #A method to set a new direction for Inky
    def set_direction(self, new_direction):
        self.direction = new_direction  

    '''
    A series of methods to set the movement frame of the character (Ex. RMF1 means Right Movement Frame 1)
    '''
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

    def set_LMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
    #A method to check what movement frame and direction the ghost is in
    def update_frame(self):
        #0: The Ghost is in frame 1
        if(self.get_frame() < 1):
            self.set_RMF1()
            self.set_frame(1)
        #1: The Ghost is in frame 2
        else:
            self.set_RMF2()
            self.set_frame(0)
        
        #Debug code for checking frame change speed
            #print(self.get_frame())