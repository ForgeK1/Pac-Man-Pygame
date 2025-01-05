'''
Description: This class contains methods for animations and interactable events for the 
             Pac-Man object
'''

#Imports pygame libraries
import pygame

class PacMan:
    #A constructor to initialize an instance of Pac Man
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (horizontal_scale, vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)

        #Variables to keep track of current frame, direction, movement coordinates, and scale of Pac-Man
        self.frame = 0
        self.direction = direction
        self.x_position = x_position
        self.y_position = y_position
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale
        
        #A variable to keep track if Pac-Man should move or not
        self.movement = movement

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
    
    #A method to return Pac-Man's x_position
    def get_x_position(self):
        return self.x_position

    #A method to set a new x_position for Pac-Man
    def set_x_position(self, new_x_position):
        self.x_position = new_x_position
    
    #A method to return Pac-Man's y_position
    def get_y_position(self):
        return self.y_position

    #A method to set a new y_position for Pac-Man
    def set_y_position(self, new_y_position):
        self.y_position = new_y_position

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
    
    #A method to return a boolean for Pac-Man's movement
    def get_movement(self):
        return self.movement

    #A method to set a new boolean for Pac-Man's movement
    def set_movement(self, new_movement):
        self.movement = new_movement

    '''
    A series of methods to set the current frame and movement position of the character 
    (Ex. CF means circle frame and RMF1 means Right Movement Frame 1)
    '''
    def set_CF(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/circle.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)

    def set_LMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
    
    #A method to check what movement frame and direction Pac-Man is in
    def frame_update(self):
        match self.get_frame():
            case 0:
                self.set_CF()

                self.set_frame(1)
            case 1:
                if(self.direction == 'Right'):
                    self.set_RMF1()
                elif(self.direction == 'Left'):
                    self.set_LMF1()
                elif(self.direction == 'Down'):
                    self.set_DMF1()
                elif(self.direction == 'Up'):
                    self.set_UMF1()
                
                self.set_frame(2)
            case 2:
                if(self.direction == 'Right'):
                    self.set_RMF2()
                elif(self.direction == 'Left'):
                    self.set_LMF2()
                elif(self.direction == 'Down'):
                    self.set_DMF2()
                elif(self.direction == 'Up'):
                    self.set_UMF2()
                
                self.set_frame(0)
        
        #Debug code for checking frame change speed
            #print(self.get_frame())
    
    #A method to update the animation speed for a specific character in the Gameplay Scene
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
        if(change_frame and self.get_movement()):
            self.frame_update()
    
    #A method for the player to control Pac-Man's movement in the Gameplay Scene
    def movement_update(self, event, list_obstacles):
        #Grabs the old direction of Pac-Man if the player didn't change directions
        new_direction = self.direction
        
        '''
        Grabs the new direction (what arrow key the player pressed). Note that, if the player 
        didn't press any arrow keys it uses the previous direction that Pac-Man is on
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
        
        #Creates a Pac-Man object to predict the future position the play wants to prgress in
        next_position = PacMan(self.get_horizontal_scale(), self.get_vertical_scale(), new_direction,
                               self.get_x_position(), self.get_y_position(), self.get_movement(), 
                               50)
        
        #A set of if else statements to update the future movement position for next_position
        if(new_direction == 'Right'):
            next_position.get_rect().centerx = next_position.get_x_position() + 2
        elif(new_direction == 'Left'):
            next_position.get_rect().centerx = next_position.get_x_position() - 2
        elif(new_direction == 'Down'):
            next_position.get_rect().centery = next_position.get_y_position() + 2
        elif(new_direction == 'Up'):
            next_position.get_rect().centery = next_position.get_y_position() - 2
        
        #Debug code to see the rect of next_position before checking collision
            #print(next_position.get_rect().center)
        
        '''
        If next_position's future direction & position is not colliding with any walls, then those new values 
        are set for current Pac-Man object
        '''
        if(next_position.get_rect().collidelist(list_obstacles[2]) == -1):            
            #self.movement = True
            self.set_direction(next_position.get_direction())
            self.set_x_position(next_position.get_rect().centerx)
            self.set_y_position(next_position.get_rect().centery)
        
        #Debug code to see the rect of Pac-Man after checking collision
            #print(self.get_rect().center)