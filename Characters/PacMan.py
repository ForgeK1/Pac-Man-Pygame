'''
Description: This class contains methods for animations and interactable events for the 
             Pac-Man object
'''

#Imports pygame libraries
import pygame

class PacMan:
    #A constructor to initialize an instance of Pac-Man
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed):
        #Variables to keep track the image and rect
        self.image = pygame.image.load('Images/Pac-Man/Movement/circle.png')
        self.image = pygame.transform.scale(self.image, (horizontal_scale, vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)

        #Variables to keep track of the scale, direction, movement boolean, and frame of Pac-Man
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale
        self.direction = direction
        self.movement = movement
        self.frame = 0

        #Variables to control character animation speed
        self.character_animation_speed = character_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds

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
    
    #A method to return Pac-Man's horizontal_scale
    def get_horizontal_scale(self):
        return self.horizontal_scale

    #A method to set a new horizontal_scale for Pac-Man
    def set_horizontal_scale(self, new_horizontal_scale):
        self.horizontal_scale = new_horizontal_scale
    
    #A method to return Pac-Man's vertical_scale
    def get_vertical_scale(self):
        return self.vertical_scale

    #A method to set a new vertical_scale for Pac-Man
    def set_vertical_scale(self, new_vertical_scale):
        self.vertical_scale = new_vertical_scale
    
    #A method to return Pac-Man's current direction
    def get_direction(self):
        return self.direction
    
    #A method to set a new direction for Pac-Man
    def set_direction(self, new_direction):
        self.direction = new_direction
    
    #A method to return a boolean for Pac-Man's movement
    def get_movement(self):
        return self.movement

    #A method to set a new boolean for Pac-Man's movement
    def set_movement(self, new_movement):
        self.movement = new_movement

    #A method to return Pac-Man's current frame
    def get_frame(self):
        return self.frame
    
    #A method to set a new frame for Pac-Man
    def set_frame(self, new_frame):
        self.frame = new_frame

    '''
    A series of methods to set the current frame of the character 
    (Ex. CF means circle frame and RMF1 means Right Movement Frame 1)
    '''
    def set_CF(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/circle.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    def set_LMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #A method to check what frame Pac-Man is in
    def frame_update(self):
        match self.frame:
            case 0:
                self.set_CF()

                self.frame = 1
            case 1:
                if(self.direction == 'Right'):
                    self.set_RMF1()
                elif(self.direction == 'Left'):
                    self.set_LMF1()
                elif(self.direction == 'Down'):
                    self.set_DMF1()
                elif(self.direction == 'Up'):
                    self.set_UMF1()
                
                self.frame = 2
            case 2:
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
    
    #A method to update the animation speed for Pac-Man
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
    
    #A method for the player to control Pac-Man's movement position
    def movement_update(self, event, list_obstacles):
        #Creates direction variables for Pac-Man's new and ongoing (old) directions
        new_direction = self.direction
        old_direction = self.direction
        
        '''
        Applies a value to new direction if the player pressed any arrow keys 
            Note: If the player didn't press any arrow keys, new & old direction 
                  will have same value
        '''
        if('key' in event.dict):
            direction_key = event.dict.get('key')

            if(direction_key == 1073741903):
                new_direction = 'Right'

            elif(direction_key == 1073741904):
                new_direction = 'Left'

            elif(direction_key == 1073741905):
                new_direction = 'Down'

            elif(direction_key == 1073741906):
                new_direction = 'Up'
        
        #Creates two rect objects to predict the future position the player wants to progress in
        new_direction_rect = pygame.Rect.copy(self.rect)
        old_direction_rect = pygame.Rect.copy(self.rect)
        
        #A set of if else statements to update the future position for Pac-Man's new direction
        if(new_direction == 'Right'):
            new_direction_rect.centerx = new_direction_rect.centerx + 2
        elif(new_direction == 'Left'):
            new_direction_rect.centerx = new_direction_rect.centerx - 2
        elif(new_direction == 'Down'):
            new_direction_rect.centery = new_direction_rect.centery + 2
        elif(new_direction == 'Up'):
            new_direction_rect.centery = new_direction_rect.centery - 2
        
        #A set of if else statements to update the future position for Pac-Man's old direction
        if(old_direction == 'Right'):
            old_direction_rect.centerx = old_direction_rect.centerx + 2
        elif(old_direction == 'Left'):
            old_direction_rect.centerx = old_direction_rect.centerx - 2
        elif(old_direction == 'Down'):
            old_direction_rect.centery = old_direction_rect.centery + 2
        elif(old_direction == 'Up'):
            old_direction_rect.centery = old_direction_rect.centery - 2
        
        '''
        If Pac-Man's new direction and position do not result in a collision with any walls,  
        the new values are applied to the current Pac-Man object. Otherwise, the original direction 
        is checked under the same conditions. If neither condition allows movement, Pac-Man remains stationary
        '''
        if(new_direction_rect.collidelist(list_obstacles[2]) == -1):            
            self.direction = new_direction
            self.rect.center = (new_direction_rect.centerx, new_direction_rect.centery)
            self.movement = True
        elif(old_direction_rect.collidelist(list_obstacles[2]) == -1):
            self.rect.center = (old_direction_rect.centerx, old_direction_rect.centery)
            self.movement = True
        else:
            self.movement = False