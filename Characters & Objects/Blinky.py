'''
Description: This class contains methods for animations and interactable events for the 
             Blinky (Red) ghost object
'''

#Imports pygame libraries
import pygame

class Blinky:
    #A constructor to initialize an instance of Blinky
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed):
        #Variables to keep track of the image and rect
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (horizontal_scale, vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)

        #Variables to keep track of the scale, direction, movement boolean, and frame of Blinky
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale
        self.direction = direction
        self.movement = movement
        self.frame = 0

        #Variables to control character animation speed
        self.character_animation_speed = character_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds

    #A method to return Blinky's image
    def get_image(self):
        return self.image

    #A method to set a new image for Blinky
    def set_image(self, new_image):
        self.image = new_image

    #A method to return the rect of Blinky's image
    def get_rect(self):
        return self.rect
    
    #A method to set a new rect for Blinky
    def set_rect(self, new_rect):
        self.rect = new_rect
    
    #A method to return Blinky's horizontal_scale
    def get_horizontal_scale(self):
        return self.horizontal_scale

    #A method to set a new horizontal_scale for Blinky
    def set_horizontal_scale(self, new_horizontal_scale):
        self.horizontal_scale = new_horizontal_scale
    
    #A method to return Blinky's vertical_scale
    def get_vertical_scale(self):
        return self.vertical_scale

    #A method to set a new vertical_scale for Blinky
    def set_vertical_scale(self, new_vertical_scale):
        self.vertical_scale = new_vertical_scale
    
    #A method to return Blinky's current direction
    def get_direction(self):
        return self.direction
    
    #A method to set a new direction for Blinky
    def set_direction(self, new_direction):
        self.direction = new_direction
    
    #A method to return a boolean for Blinky's movement
    def get_movement(self):
        return self.movement

    #A method to set a new boolean for Blinky's movement
    def set_movement(self, new_movement):
        self.movement = new_movement

    #A method to return Blinky's current frame
    def get_frame(self):
        return self.frame
    
    #A method to set a new frame for Blinky
    def set_frame(self, new_frame):
        self.frame = new_frame

    '''
    A series of methods to set the current frame of the character 
    (Ex. CF means circle frame and RMF1 means Right Movement Frame 1)
    '''
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    def set_LMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Blinky (Red)/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #A method to check what movement frame and direction the ghost is in
    def frame_update(self):
        match self.frame:
            case 0:
                if(self.direction == 'Right'):
                    self.set_RMF1()
                elif(self.direction == 'Left'):
                    self.set_LMF1()
                elif(self.direction == 'Down'):
                    self.set_DMF1()
                elif(self.direction == 'Up'):
                    self.set_UMF1()
                
                self.frame = 1

            case 1:
                if(self.direction == 'Right'):
                    self.set_RMF2()
                elif(self.direction == 'Left'):
                    self.set_LMF2()
                elif(self.direction == 'Down'):
                    self.set_DMF2()
                elif(self.direction == 'Up'):
                    self.set_UMF2()
                
                self.frame = 0
        
        #Debug code for checking frame change speed
            #print(self.get_frame())
        
    #A method to update the animation speed for Blinky
    def animation_update(self):
        #Gets the current time in miliseconds
        curr_time = pygame.time.get_ticks()
        
        #A variable to keep track of changing frame of characters
        change_frame = False

        '''
        Updates the animation frame of each character if enough time has passed
            Ex) 0 - 0 > 200     False
                100 - 0 > 200   False
                201 - 0 > 200   True  --> 
                201 - 201 > 200 False
                ...
                402 - 201 > 200 True -->
                402 - 402 > 200 
                ... and so on
        '''
        if curr_time - self.last_updated_time > self.character_animation_speed: 
            #Sets change frame to True 
            change_frame = True

            #Sets up a new time
            self.last_updated_time = curr_time
        
        #If True, then the program updates the frame of the character. If False, then the program uses the old frame in runtime
        if(change_frame and self.movement):
            self.frame_update()
        
    #A method for the player to control Blinky's movement position
    def movement_update(self, event, list_obstacles):
        #Empty for now
        return None