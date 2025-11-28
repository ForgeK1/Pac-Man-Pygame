'''
Description: This class contains methods for animations and interactable events for the 
             Pinky (Pink) ghost object
'''

#Imports pygame libraries
import pygame

class Pinky:
    #A constructor to initialize an instance of Pinky
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed):
        #Variables to keep track of the image and rect
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (horizontal_scale, vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)

        #Variables to keep track of the scale, direction, movement boolean, and frame of Pinky
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale
        self.direction = direction
        self.movement = movement
        self.frame = 0

        #Variables to check what state the ghost is in
        self.chase_state = True #Ghost chasing Pac-Man
        self.scatter_state = False #Ghost moving away from Pac-Man
        self.frightened_state_v1 = False #Blue skin 
        self.frightened_state_v2 = False #A pattern of repeating blue and white skin
        self.eaten_state = False #A pair of floating eyes

        #Variables to control character animation speed
        self.character_animation_speed = character_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds

    #A method to return Pinky's image
    def get_image(self):
        return self.image

    #A method to set a new image for Pinky
    def set_image(self, new_image):
        self.image = new_image

    #A method to return the rect of Pinky's image
    def get_rect(self):
        return self.rect
    
    #A method to set a new rect for Pinky
    def set_rect(self, new_rect):
        self.rect = new_rect
    
    #A method to return Pinky's horizontal_scale
    def get_horizontal_scale(self):
        return self.horizontal_scale

    #A method to set a new horizontal_scale for Pinky
    def set_horizontal_scale(self, new_horizontal_scale):
        self.horizontal_scale = new_horizontal_scale
    
    #A method to return Pinky's vertical_scale
    def get_vertical_scale(self):
        return self.vertical_scale

    #A method to set a new vertical_scale for Pinky
    def set_vertical_scale(self, new_vertical_scale):
        self.vertical_scale = new_vertical_scale
    
    #A method to return Pinky's current direction
    def get_direction(self):
        return self.direction
    
    #A method to set a new direction for Pinky
    def set_direction(self, new_direction):
        self.direction = new_direction
    
    #A method to return the boolean for Pinky's movement
    def get_movement(self):
        return self.movement

    #A method to set a new boolean for Pinky's movement
    def set_movement(self, new_movement):
        self.movement = new_movement

    #A method to return Pinky's current frame
    def get_frame(self):
        return self.frame
    
    #A method to set a new frame for Pinky
    def set_frame(self, new_frame):
        self.frame = new_frame

    #A method to return the boolean for Pinky's chase state
    def get_chase_state(self):
        return self.chase_state
    
    #A method to set a new boolean for Pinky's chase state
    def set_chase_state(self, new_chase_state):
        self.chase_state = new_chase_state

    #A method to return the boolean for Pinky's scatter state
    def get_scatter_state(self):
        return self.scatter_state
    
    #A method to set a new boolean for Pinky's scatter state
    def set_scatter_state(self, new_scatter_state):
        self.scatter_state = new_scatter_state
    
    #A method to return the boolean for Pinky's frightened state version #1
    def get_frightened_state_v1(self):
        return self.frightened_state_v1

    #A method to set a new boolean for Pinky's frightened state version #1
    def set_frightened_state_v1(self, new_frightened_state_v1):
        self.frightened_state_v1 = new_frightened_state_v1

    #A method to return the boolean for Pinky's frightened state version #2
    def get_frightened_state_v2(self):
        return self.frightened_state_v2

    #A method to set a new boolean for Pinky's frightened state version #2
    def set_frightened_state_v2(self, new_frightened_state_v2):
        self.frightened_state_v2 = new_frightened_state_v2
    
    #A method to return the boolean for Pinky's eaten state
    def get_eaten_state(self):
        return self.eaten_state

    #A method to set a new boolean for Pinky's eaten state
    def set_eaten_state(self, new_eaten_state):
        self.eaten_state = new_eaten_state

    '''
    A series of methods to set the current frame of the character in their normal state
    '''

    #Right movement frame 1
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Right movement frame 2
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Left movement frame 1
    def set_LMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Left movement frame 2
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up movement frame 1
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up movement frame 2
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down movement frame 1
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down movement frame 2
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Pinky (Pink)/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    '''
    A series of methods to set the current frame of the character in their frightened state
    '''

    #Blue movement frame 1
    def set_BMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Frightened State/blue_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Blue movement frame 2
    def set_BMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Frightened State/blue_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #White movement frame 1
    def set_WMF1(self):
        self.image = pygame.image.load('Images/Ghosts/Frightened State/white_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #White movement frame 2
    def set_WMF2(self):
        self.image = pygame.image.load('Images/Ghosts/Frightened State/white_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    '''
    A series of methods to set the current frame of the character in their eaten state
    '''

    #Right eaten movement frame
    def set_REMF(self):
        self.image = pygame.image.load('Images/Ghosts/Eaten State/right.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Left eaten movement frame
    def set_LEMF(self):
        self.image = pygame.image.load('Images/Ghosts/Eaten State/left.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up eaten movement frame
    def set_UEMF(self):
        self.image = pygame.image.load('Images/Ghosts/Eaten State/up.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down eaten movement frame
    def set_DEMF(self):
        self.image = pygame.image.load('Images/Ghosts/Eaten State/down.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #A method to check what movement frame and direction the ghost is in
    def frame_update(self):
        #Frightened state #1 (a blue version of the ghost)
        if(self.frightened_state_v1):
            #Debug code
                #print('Pinky is in a frightened state #1')

            match self.frame:
                case 0:
                    self.set_BMF1()                    
                    self.frame = 1

                case 1:
                    self.set_BMF2()                    
                    self.frame = 0

            #Debug code for checking frame change speed
                #print(self.get_frame())
        #Frightened state #2 (a pattern of repeating blue and white version of the ghost)
        elif(self.frightened_state_v2):
            #Debug code
                #print('Pinky is in a frightened state #2')

            match self.frame:
                case 0:
                    self.set_WMF1()
                    self.frame = 1

                case 1:
                    self.set_BMF1()
                    self.frame = 2

                case 2:
                    self.set_BMF2()
                    self.frame = 3

                case 3:
                    self.set_WMF2()
                    self.frame = 4
                
                case 4:
                    self.set_BMF1()
                    self.frame = 5

                case 5:
                    self.set_BMF2()
                    self.frame = 0
        #A state where the ghost is a pair of floating eyes
        elif(self.eaten_state):
            #Debug code
                #print('Pinky is in an eaten state')

            if(self.direction == 'Right'):
                self.set_REMF()
            elif(self.direction == 'Left'):
                self.set_LEMF()
            elif(self.direction == 'Down'):
                self.set_DEMF()
            elif(self.direction == 'Up'):
                self.set_UEMF()
        #Normal state
        else:
            #Debug code
                #print('Pinky is in a normal state')

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
        
    #A method to update the animation speed for Pinky
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
        
    #A method to change the Pinky's state based on in-game events
    def state_handler(self, event, list_obstacles):
        return None

    #A method to update Pinky's movement based on his chase state
    def chase_state_movement_update(self):
        return None
    
    #A method to update Pinky's movement based on his scatter state
    def scatter_state_movement_update(self):
        return None

    #A method to update Pinky's movement based on his frightened state
    def frightened_state_movement_update(self):
        return None

    #A method to update Pinky's movement based on his eaten state
    def eaten_state_movement_update(self):
        return None