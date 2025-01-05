'''
Description: This class contains methods for animations and interactable events for the 
             Inky (Cyan) ghost object
'''

#Imports pygame libraries
import pygame

class Inky:
    #A constructor to initialize an instance of Inky
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (horizontal_scale, vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)

        #Variables to keep track of current frame, direction, movement coordinates, and scale of the ghost
        self.frame = 0
        self.direction = direction
        self.x_position = x_position
        self.y_position = y_position
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale

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

    #A method to return Inky's x_position
    def get_x_position(self):
        return self.x_position

    #A method to set a new x_position for Inky
    def set_x_position(self, new_x_position):
        self.x_position = new_x_position
    
    #A method to return Inky's y_position
    def get_y_position(self):
        return self.y_position

    #A method to set a new y_position for Inky
    def set_y_position(self, new_y_position):
        self.y_position = new_y_position
    
    #A method to return Inky's horizontal_scale
    def get_horizontal_scale(self):
        return self.horizontal_scale

    #A method to set a new horizontal_scale for Inky
    def set_horizontal_scale(self, new_horizontal_scale):
        self.horizontal_scale = new_horizontal_scale
    
    #A method to return Inky's vertical_scale
    def get_vertical_scale(self):
        return self.vertical_scale

    #A method to set a new vertical_scale for Inky
    def set_vertical_scale(self, new_vertical_scale):
        self.vertical_scale = new_vertical_scale

    '''
    A series of methods to set the current frame and movement position of the character 
    (Ex. RMF1 means Right Movement Frame 1)
    '''
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)

    def set_LMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Inky (Cyan)/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
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