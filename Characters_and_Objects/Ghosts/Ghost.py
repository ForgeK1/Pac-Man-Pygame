'''
Description: This hybrid-abstract class serves as a parent Ghost class for the four ghosts to derive from
'''

#Imports for the Ghost class to function
import pygame
from abc import ABC, abstractmethod

class Ghost(ABC):
    #A constructor to initialize an instance of the Ghost
    def __init__(self, ghost_name, starting_image_path, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed, level_counter):
        #Initializes a variable to assign the child ghost name (Blinky, Inky, Pinky, or Clyde)
        self.ghost_name = ghost_name

        #Initializes variables to keep track of the image and rect
        self.image = pygame.image.load(starting_image_path)
        self.image = pygame.transform.scale(self.image, (horizontal_scale, vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)

        #Initializes variables to keep track of the scale, direction, movement boolean, and frame of Ghost
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale
        self.direction = direction
        self.movement = movement
        self.frame = 0

        #Initializes variables to control character animation speed
        self.character_animation_speed = character_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds

        #Initializes a variable to keep track of current level from the Gameplay Scene
        self.level_counter = level_counter

        #Variables to check what state the ghost is in
        self.chase_state = True #Ghost chasing Pac-Man
        self.scatter_state = False #Ghost moving away from Pac-Man
        self.frightened_state_v1 = False #Blue skin 
        self.frightened_state_v2 = False #A pattern of repeating blue and white skin
        self.eaten_state = False #A pair of floating eyes

        #variables to help the ghost cycle between the chase and scatter state
        self.chase_and_scatter_cycle_phases = ["Scatter", "Chase", "Scatter", "Chase", "Scatter", "Chase", "Scatter", "Chase"]
        self.chase_and_scatter_cycle_phase_timers = self.set_up_ghost_chase_and_scatter_cycle_phases()
        self.chase_and_scatter_cycle_real_timer = None
        self.chase_and_scatter_cycle_curr_timer = None

    #A method to return Ghost's image
    def get_image(self):
        return self.image

    #A method to set a new image for Ghost
    def set_image(self, new_image):
        self.image = new_image

    #A method to return the rect of Ghost's image
    def get_rect(self):
        return self.rect
    
    #A method to set a new rect for Ghost
    def set_rect(self, new_rect):
        self.rect = new_rect
    
    #A method to return Ghost's horizontal_scale
    def get_horizontal_scale(self):
        return self.horizontal_scale

    #A method to set a new horizontal_scale for Ghost
    def set_horizontal_scale(self, new_horizontal_scale):
        self.horizontal_scale = new_horizontal_scale
    
    #A method to return Ghost's vertical_scale
    def get_vertical_scale(self):
        return self.vertical_scale

    #A method to set a new vertical_scale for Ghost
    def set_vertical_scale(self, new_vertical_scale):
        self.vertical_scale = new_vertical_scale
    
    #A method to return Ghost's current direction
    def get_direction(self):
        return self.direction
    
    #A method to set a new direction for Ghost
    def set_direction(self, new_direction):
        self.direction = new_direction
    
    #A method to return the boolean for Ghost's movement
    def get_movement(self):
        return self.movement

    #A method to set a new boolean for Ghost's movement
    def set_movement(self, new_movement):
        self.movement = new_movement

    #A method to return Ghost's current frame
    def get_frame(self):
        return self.frame
    
    #A method to set a new frame for Ghost
    def set_frame(self, new_frame):
        self.frame = new_frame

    #A method to return the boolean for Ghost's chase state
    def get_chase_state(self):
        return self.chase_state
    
    #A method to set a new boolean for Ghost's chase state
    def set_chase_state(self, new_chase_state):
        self.chase_state = new_chase_state

    #A method to return the boolean for Ghost's scatter state
    def get_scatter_state(self):
        return self.scatter_state
    
    #A method to set a new boolean for Ghost's scatter state
    def set_scatter_state(self, new_scatter_state):
        self.scatter_state = new_scatter_state
    
    #A method to return the boolean for Ghost's frightened state version #1
    def get_frightened_state_v1(self):
        return self.frightened_state_v1

    #A method to set a new boolean for Ghost's frightened state version #1
    def set_frightened_state_v1(self, new_frightened_state_v1):
        self.frightened_state_v1 = new_frightened_state_v1

    #A method to return the boolean for Ghost's frightened state version #2
    def get_frightened_state_v2(self):
        return self.frightened_state_v2

    #A method to set a new boolean for Ghost's frightened state version #2
    def set_frightened_state_v2(self, new_frightened_state_v2):
        self.frightened_state_v2 = new_frightened_state_v2
    
    #A method to return the boolean for Ghost's eaten state
    def get_eaten_state(self):
        return self.eaten_state

    #A method to set a new boolean for Ghost's eaten state
    def set_eaten_state(self, new_eaten_state):
        self.eaten_state = new_eaten_state
    
    '''
    A series of methods to set the current frame of the Ghost in their normal state
    '''

    #Right movement frame 1
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.ghost_name + '/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Right movement frame 2
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.ghost_name + '/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Left movement frame 1
    def set_LMF1(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.ghost_name + '/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Left movement frame 2
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.ghost_name + '/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up movement frame 1
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.ghost_name + '/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up movement frame 2
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.ghost_name + '/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down movement frame 1
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.ghost_name + '/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down movement frame 2
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.ghost_name + '/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    '''
    A series of methods to set the current frame of the Ghost in their frightened state
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
    A series of methods to set the current frame of the Ghost in their eaten state
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

    '''
    A method that updates the ghost phase during gameplay (this method is called in the GameplayScene class)
        Ex. Chase, Scatter, Frightened, Eaten states
    '''
    def update_ghost_phase(self):
        #Checks if the ghost is in an eaten state
        if(self.eaten_state):
            print('Ghost is in an eaten state')
        #Checks if the ghost is in a frightened state
        if(self.frightened_state_v1 or self.frightened_state_v2):
            print('Ghost is in a frightened state')
        #Else, the ghost cycles between the chase and scatter states
        else:
            #Grabs the time passed in game
            self.chase_and_scatter_cycle_real_timer = round(pygame.time.get_ticks() / 1000)

            '''
            If the current timer has not been defined, it is set to the same value as the real timer.
            This ensures that the time passed starts from a clean slate 
                Ex. real time - curr time = 0 seconds have passed
            '''
            if(self.chase_and_scatter_cycle_curr_timer is None):
                self.chase_and_scatter_cycle_curr_timer = self.chase_and_scatter_cycle_real_timer          

            num_seconds_passed = self.chase_and_scatter_cycle_real_timer - self.chase_and_scatter_cycle_curr_timer

            #Debug code
                #print(str(num_seconds_passed) + " seconds have passed")
            
            

        return None
    
    '''
    A method that sets the amount of time to cycle between the scatter and chase states
        Ex) Level 1 indicates
            cycle_phase_timers: [7 seconds, 20 seconds, 7 seconds, 20 seconds, 5 seconds, 20 seconds, 5 seconds, -1 (Chase state until the round ends)]
            cycle_phase_timers: ["Scatter", "Chase",    "Scatter", "Chase",    "Scatter", "Chase",    "Scatter", "Chase"]
    '''
    def set_up_ghost_chase_and_scatter_cycle_phases(self):
        if(self.level_counter == 1):
            cycle_phase_timers = [7, 20, 7, 20, 5, 20, -1]
        elif(2 <= self.level_counter or self.level_counter <= 4):
            #For the inner list: Red 17 sec / Pink 13 sec / Inky 14 sec / Clyde 14 sec
            cycle_phase_timers = [7, 20, 7, 20, 5, [17, 13, 14, 14], 0.01, -1]
        else: #Rounds 5 and up
            cycle_phase_timers = [5, 20, 5, 20, 5, [17, 17, 14, 14], 0.01, -1]
            
        return cycle_phase_timers

    #A method to check what movement frame and direction the ghost is in
    def frame_update(self):
        #Frightened state #1 (a blue version of the ghost)
        if(self.frightened_state_v1):
            #Debug code
                #print('The Ghost is in a frightened state #1')

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
                #print('The Ghost is in a frightened state #2')

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
                #print('The Ghost is in an eaten state')

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
                #print('The Ghost is in a normal state')

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
        
    #A method to update the animation speed for Ghost
    def animation_update(self):       
        #Gets the current time in miliseconds
        curr_time = pygame.time.get_ticks()
        
        #print("\nCurrent Time: " + str(curr_time) + "\nLast Updated Time: " + str(self.last_updated_time) + "\n")

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
    
    #A method to change the Ghost's state based on in-game events
    def state_handler(self, event):
        states = ["Chase", "Scatter", "Frightened", "Eaten"]

        current_state = states[0]

        ### Outline ###
        #Include a method that updates the phase_timer based on the current level of the game

        #If the ghost is in Scatter or Chase state, use resepective movement methods

        #If the ghost is in Frightened or Eaten state, use respective movementr methods

        return None

    #A method to update Ghost's movement based on his chase state
    def chase_state_movement_update(self, list_obstacles):
        return None
    
    #A method to update Ghost's movement based on his scatter state
    def scatter_state_movement_update(self, list_obstacles):
        return None

    #A method to update Ghost's movement based on his frightened state
    def frightened_state_movement_update(self, list_obstacles):
        return None

    #A method to update Ghost's movement based on his eaten state
    def eaten_state_movement_update(self, list_obstacles):
        return None