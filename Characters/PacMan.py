'''
Description: This class contains methods for animations and interactable events for the 
             Pac-Man object
'''

#Imports pygame libraries
import pygame

class PacMan:
    #A constructor to initialize an instance of Pac Man
    def __init__(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()

        '''
        Variables to keep track of current movement frame and direction of Pac-Man
            Ex) ghost_frame has 2 movement frames and pac_man_frame has 3 movement frames for 
                any direction of movement
        '''
        self.frame = 0
        self.direction = 'right'

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

    #A method to return Pac-Man's current frame
    def get_frame(self):
        return self.frame
    
    #A method to set a new frame for Pac-Man
    def set_frame(self, new_frame):
        self.frame = new_frame
    
    #A method to return Pac-Man's current direction
    def get_direction(self):
        return self.direction
    
    #A method to set a new direction for Pac-Man
    def set_direction(self, new_direction):
        self.direction = new_direction

    '''
    A series of methods to set the movement frame of the character (Ex. RMF1 means Right Movement Frame 1 and CF means circle frame)
    '''
    def set_CF(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/circle.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
    
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
    
    #A method to check what movement frame and direction Pac-Man is in
    def update_frame(self):
        match self.get_frame(): 
            case 0:
                self.set_CF()
                self.set_frame(1)
            case 1:
                self.set_RMF1()
                self.set_frame(2)
            case 2:
                self.set_RMF2()
                self.set_frame(0)
        
        #Debug code for checking frame change speed
            #print(self.get_frame())