'''
Description: This hybrid-abstract class serves as a parent Ghost class for the four ghosts to derive from
'''

#Imports for the Ghost class to function
import pygame
import random
import math
from abc import ABC, abstractmethod

class Ghost(ABC):
    #A constructor to initialize an instance of the Ghost
    def __init__(self, scene_surface, name, starting_image_path, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed, level_counter, game_state_manager):
        #Initializes the current surface the ghosts are being blitted on (Ex. Gameplay Scene --> gameplay_surface)
        self.scene_surface = scene_surface
        
        #Initializes a variable to assign the child ghost name (Blinky, Inky, Pinky, or Clyde)
        self.name = name

        #Initializes variables to keep track of the image and rect
        self.image = pygame.image.load(starting_image_path)
        self.image = pygame.transform.scale(self.image, (horizontal_scale, vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)

        #Initializes variables to keep track of the scale, direction, movement boolean, frame of the ghost, and how many steps to take per frame (based on their current state)
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale
        self.direction = direction
        self.movement = movement
        self.frame = 0
        self.stand_by_state_steps_per_frame = 0
        self.frightened_state_steps_per_frame = 0
        self.eaten_state_steps_per_frame = 0

        #Initializes variables to control character animation speed
        self.character_animation_speed = character_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds

        #Initializes a variable to keep track of current level from the Gameplay Scene
        self.level_counter = level_counter

        #Initializes the game state manager
        self.game_state_manager = game_state_manager

        #Variables to check what state the ghost is in
        self.stand_by_state = True #Ghost waiting in the gate until Pac-Man eats enough dots
        self.chase_state = False #Ghost chasing Pac-Man
        self.scatter_state = False #Ghost moving away from Pac-Man
        self.frightened_state_v1 = False #Blue skin 
        self.frightened_state_v2 = False #A pattern of repeating blue and white skin
        self.eaten_state = False #A pair of floating eyes

        #Variables to indicate that the ghost turns around 180 degrees once they go into their Frightened state or Chase state
        self.turn_around = False
        self.turn_around_occured_once = False

        #Variables to help the ghost cycle between the chase and scatter state
        self.chase_and_scatter_cycle_phases = ["Scatter", "Chase", "Scatter", "Chase", "Scatter", "Chase", "Scatter", "Chase"]
        self.chase_and_scatter_cycle_phase_timers = self.set_up_ghost_chase_and_scatter_cycle_phase_timers()

        self.chase_and_scatter_cycle_real_timer = 0
        self.chase_and_scatter_cycle_curr_timer = None

        #Initializes a variable timer to dynamically change ghost frightened state frame after Pac-Man eats a power pellet
        self.ghost_scatter_timer = 0

        #Initializes a variable to help the Ghost exit the gate region once their stand by state ends
        self.stand_by_state_exit_condition = False

    #A method to return Ghost's name
    def get_name(self):
        return self.name

    #A method to set a new name for Ghost
    def set_name(self, new_name):
        self.name = new_name

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
    
    #A method to return the boolean for Ghost's stand by state
    def get_stand_by_state(self):
        return self.stand_by_state
    
    #A method to set a new boolean for Ghost's stand by state
    def set_stand_by_state(self, new_stand_by_state):
        self.stand_by_state = new_stand_by_state

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

    #A method to get the boolean for the ghost's turn_around_occured_once condition
    def get_turn_around_occured_once(self):
        return self.turn_around_occured_once
    
    #A method to set a new boolean for the ghost's turn_around_occured_once condition
    def set_turn_around_occured_once(self, new_turn_around_occured_once):
        self.turn_around_occured_once = new_turn_around_occured_once

    #A method to return the ghost scatter timer
    def get_ghost_scatter_timer(self):
        return self.ghost_scatter_timer
    
    #A method to set the ghost scatter timer
    def set_ghost_scatter_timer(self, new_ghost_scatter_timer):
        self.ghost_scatter_timer = new_ghost_scatter_timer
    
    #A method to return the boolean for Ghost's exit condition when their stand by state ends
    def get_stand_by_state_exit_condition(self):
        return self.stand_by_state_exit_condition
    
    #A method to set the boolean for Ghost's exit condition when their stand by state ends
    def set_stand_by_state_exit_condition(self, new_stand_by_state_exit_condition):
        self.stand_by_state_exit_condition = new_stand_by_state_exit_condition

    '''
    A series of methods to set the current frame of the Ghost in their normal state
    '''

    #Right movement frame 1
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.name + '/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Right movement frame 2
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.name + '/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Left movement frame 1
    def set_LMF1(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.name + '/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Left movement frame 2
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.name + '/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up movement frame 1
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.name + '/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up movement frame 2
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.name + '/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down movement frame 1
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.name + '/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down movement frame 2
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Ghosts/' + self.name + '/down_frame_2.png')
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
    A method to reset the chase and scatter cycle for the Ghost 
        Ex) At the end of a round, the timers for all ghosts need to be reset to transition
            to the next level or to the Main Menu Scene
    '''
    def reset_chase_and_scatter_cycle(self):
        self.chase_and_scatter_cycle_phases = ["Scatter", "Chase", "Scatter", "Chase", "Scatter", "Chase", "Scatter", "Chase"]
        self.chase_and_scatter_cycle_phase_timers = self.set_up_ghost_chase_and_scatter_cycle_phase_timers()
        self.chase_and_scatter_cycle_real_timer = 0
        self.chase_and_scatter_cycle_curr_timer = 0

    #A method to check what movement frame and direction the ghost is in
    def frame_update(self):
        #Frightened state #1 (a blue version of the ghost)
        if(self.frightened_state_v1):
            #Debug code
                # if(self.name == 'Inky (Cyan)'):
                #     print('The Ghost is in a frightened state #1')

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
                # if(self.name == 'Inky (Cyan)'):
                #     print('The Ghost is in a frightened state #2')

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

            '''
            To ensure that the normal state is not handed a frame greater than 1 (when coming out of
            the frightened or eaten state), the frame is reset to 0
            '''
            if(self.frame > 1):
                self.frame = 0

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

            # if(self.name == 'Blinky (Red)'):
            #     print(self.ghost_scatter_timer)

    '''
    A method that updates the Ghost's behavior based on the current state they're in during gameplay
        Ex. Stand By, Chase, Scatter, Frightened, and Eaten states
    '''
    def state_handler(self, dots_eaten, siren_channel, ghost_return_channel, ghost_return, power_pellet_channel):
        #Debug code
            # if(self.name == 'Pinky (Pink)'):
            #     print("\nStand by state: " + str(self.stand_by_state) + 
            #             "\nEaten state: " + str(self.eaten_state) + 
            #             "\nFrightend state: " + str(self.frightened_state_v1 or self.frightened_state_v2) +
            #             "\nChase state: " + str(self.chase_state) + 
            #             "\nScatter state: " + str(self.scatter_state) + '\n')
    
        '''
        Checks if the Ghost is in a stand by state (where the ghost is waiting for Pac-Man to eat enough dots 
        before leaving the gate at the start of the round)
        '''
        if(self.stand_by_state):
            #Debug code
                # print('The ghost is in a stand by state')

            #Inky leaves after Pac-Man eats 30 dots 
            if(self.name == "Inky (Cyan)" and dots_eaten >= 30 and self.rect.centery == 302): 
                self.stand_by_state_exit_condition = True

            #Clyde leaves after Pac-Man eats 60 dots 
            if(self.name == "Clyde (Orange)" and dots_eaten >= 60 and self.rect.centery == 302):
                self.stand_by_state_exit_condition = True
            
            #Debug code
                # print('Center y: ' + str(self.rect.centery) + 
                #       '\nDots Eaten: ' + str(dots_eaten) + '\n')

            '''
            Deactivates the ghost's stand by state once the ghost passes the front gate
            '''

            gate_entrance = (240, 252)

            if(gate_entrance[0] > self.rect.centerx):
                range_x = self.rect.centerx / gate_entrance[0]
            else:
                range_x = gate_entrance[0] / self.rect.centerx
            
            if(gate_entrance[1] > self.rect.centery):
                range_y = self.rect.centery / gate_entrance[1]
            else: 
                range_y = gate_entrance[1] / self.rect.centery

            #Debug code
                # print('\nrange_x: ' + str(range_x))
                # print('\nrange_y: ' + str(range_y))

            if range_x > 0.95 and range_y > 0.99: 
                self.stand_by_state = False

                if(self.frightened_state_v1 is False and self.frightened_state_v2 is False):
                    self.chase_state = True
            
        #Checks if the ghost is in an eaten state
        if(self.eaten_state):
            #Debug code
                # print('The ghost is in an eaten state')

            '''
            Plays the ghost return sound effect until the ghost respawns at the gate
            '''

            power_pellet_channel.set_volume(0)
            siren_channel.set_volume(0)

            if ghost_return_channel.get_busy() is False:
                ghost_return_channel.play(ghost_return)

            '''
            Deactivates the ghost's eaten state once the ghost respawns inside of the gate region
            '''

            respawn_coordinates = (240, 310)

            if(respawn_coordinates[0] > self.rect.centerx):
                range_x = self.rect.centerx / respawn_coordinates[0]
            else:
                range_x = respawn_coordinates[0] / self.rect.centerx
            
            if(respawn_coordinates[1] > self.rect.centery):
                range_y = self.rect.centery / respawn_coordinates[1]
            else: 
                range_y = respawn_coordinates[1] / self.rect.centery

            #Debug code
                # print('\nrange_x: ' + str(range_x))
                # print('\nrange_y: ' + str(range_y))

            if range_x > 0.95 and range_y > 0.95:
                ghost_return_channel.stop()
                power_pellet_channel.set_volume(1)
                siren_channel.set_volume(1)

                self.eaten_state = False

                self.direction = 'Up'

                #This statement resets the condition for the ghost to turn around again when transitioning to their Chase state
                self.turn_around_occured_once = False
                
        #Checks if the ghost is in a frightened state
        if(self.frightened_state_v1 or self.frightened_state_v2):
            #Debug code
                # if(self.name == "Clyde (Orange)"):
                #     print('The ghost is in a frightened state')

            #Enables the condition for the ghost to turn around 180 degrees once they go into their Frightened state
            self.turn_around_condition()
            
            #Increments the timer based on how long the power pellet lasts
            self.ghost_scatter_timer += 1

            #An if-else statement to switch from the frightened v1 to the v2 frame cycle
            if(power_pellet_channel.get_busy()):
                if(self.ghost_scatter_timer <= 300):
                    #Debug code
                        #print('before 300\n')

                    self.frightened_state_v1 = True
                    self.frightened_state_v2 = False
                else:
                    #Debug code
                        #print('after 300\n')

                    self.frightened_state_v1 = False
                    self.frightened_state_v2 = True
            #Once the power pellet wears off, the ghosts are resetted to their normal state and Pac-Man is no longer chasing the ghosts
            else:          
                self.frightened_state_v1 = False
                self.frightened_state_v2 = False

                self.frame = 0
                self.ghost_scatter_timer = 0

                #This statement resets the condition for the ghost to turn around again when transitioning to their Chase state
                self.turn_around_occured_once = False

        #Else, the ghost cycles between the chase and scatter states
        if(self.stand_by_state is False and (self.frightened_state_v1 is False and self.frightened_state_v2 is False) and self.eaten_state is False):
            #Debug code
                # print('The ghost is in a chase and scatter state cycle')

            '''
            Delta time (the amount of real world time that passed since the previous frame)
                --> clock.tick(60) returns milliseconds since the last tick
            ''' 
            dt = self.game_state_manager.get_clock_delta_time() / 1000.0

            '''
            Advances the ghost phase timer by real elapsed time (frame-rate independent).
            This ensures scatter/chase timing stays accurate regardless of FPS or lag
            '''
            self.chase_and_scatter_cycle_real_timer += dt

            #Debug code
                # print(dt)
                # print(round(self.chase_and_scatter_cycle_real_timer))

            '''
            If the current timer has not been defined, it is set to the same value as the real timer.
            This ensures that the time passed starts from a clean slate 
                Ex. real time - curr time = 0 seconds have passed
            '''
            if(self.chase_and_scatter_cycle_curr_timer is None):
                self.chase_and_scatter_cycle_curr_timer = self.chase_and_scatter_cycle_real_timer          

            num_seconds_passed = self.chase_and_scatter_cycle_real_timer - self.chase_and_scatter_cycle_curr_timer

            '''
            Checks if there is only one phase left in chase_and_scatter_cycle_phases
                Ex) After 1 minute and 24 seconds have passed for level 1, all ghosts will be in the Chase state 
                    until the round ends
            '''
            if len(self.chase_and_scatter_cycle_phases) == 1:
                self.chase_state = True
                self.scatter_state = False

                #Debug code
                    #print("\n000000000000000000000000000This if statement is running000000000000000000000000000")
            #If there is more than one phase left, the ghosts will cycle between chase and scatter states
            else:
                #If the number of seconds passed hasn't reached the timer, the ghost will stay in the state at the beginning of the phase timers list
                if num_seconds_passed < self.chase_and_scatter_cycle_phase_timers[0]:
                    if self.chase_and_scatter_cycle_phases[0] == "Chase":
                        self.chase_state = True
                        self.scatter_state = False

                        #Enables the condition for the ghost to turn around 180 degrees once they go into their Chase state
                        self.turn_around_condition()
                    else:
                        self.chase_state = False
                        self.scatter_state = True
                else:
                    #As soon as the number of seconds passes the phase timer, the phase string and phase timer gets popped out of their lists
                    self.chase_and_scatter_cycle_phases.pop(0)
                    self.chase_and_scatter_cycle_phase_timers.pop(0)

                    #Then the current timer gets reset
                    self.chase_and_scatter_cycle_curr_timer = self.chase_and_scatter_cycle_real_timer
            
            #Debug code
                # if(self.name == "Blinky (Red)"):
                #     #print("\n********************************This ********************************")
                #     print("\n" + self.name + " " + str(self.chase_and_scatter_cycle_phase_timers))
                #     print("Chase State: " + str(self.chase_state))
                #     print("Scatter State: " + str(self.scatter_state))
                #     print("Number of seconds passed: " + str(round(num_seconds_passed)) + "\n")

    '''
    A method that sets the amount of time to cycle between the scatter and chase states
        Ex) Level 1 indicates
            cycle_phase_timers: [7 seconds, 20 seconds, 7 seconds, 20 seconds, 5 seconds, 20 seconds, 5 seconds, -1 (Chase state until the round ends)]
            cycle_phase_timers: ["Scatter", "Chase",    "Scatter", "Chase",    "Scatter", "Chase",    "Scatter", "Chase"]
    '''
    def set_up_ghost_chase_and_scatter_cycle_phase_timers(self):
        #Sets the timers to None if the ghost objects are created in the Main Menu Scene
        if(self.level_counter is None):
            return None
        
        elif(self.level_counter == 1):
            cycle_phase_timers = [7, 20, 7, 20, 5, 20, -1]

        elif(2 <= self.level_counter and self.level_counter <= 4):
            #For the 6th timer: Red 17 sec / Pink 13 sec / Inky 14 sec / Clyde 14 sec
            if(self.name == "Blinky (Red)"):
                cycle_phase_timers = [7, 20, 7, 20, 5, 17, 0.01, -1]
            elif(self.name == "Pinky (Pink)"):
                cycle_phase_timers = [7, 20, 7, 20, 5, 13, 0.01, -1]
            elif(self.name == "Inky (Cyan)"):
                cycle_phase_timers = [7, 20, 7, 20, 5, 14, 0.01, -1]
            elif(self.name == "Clyde (Orange)"):
                cycle_phase_timers = [7, 20, 7, 20, 5, 14, 0.01, -1]

        #Rounds 5 and up
        elif(5 <= self.level_counter): 
            if(self.name == "Blinky (Red)"):
                cycle_phase_timers = [5, 20, 5, 20, 5, 17, 0.01, -1]
            elif(self.name == "Pinky (Pink)"):
                cycle_phase_timers = [5, 20, 5, 20, 5, 17, 0.01, -1]
            elif(self.name == "Inky (Cyan)"):
                cycle_phase_timers = [5, 20, 5, 20, 5, 14, 0.01, -1]
            elif(self.name == "Clyde (Orange)"):
                cycle_phase_timers = [5, 20, 5, 20, 5, 14, 0.01, -1]

        return cycle_phase_timers
    
    '''
    A method to help the Ghost decide the direction they should take based on the Pac-Man's location (target) defined in movement_update
        1) Defines all possible paths the Ghost can take
        2) Uses the target to calculate the distance of each path
        3) Choose the path closest to the target
            Note: If two paths are the same distance, then the priority order is ⬆️ ⬅️ ⬇️ ➡️
    '''
    def direction_update(self, list_obstacles, target):
        directions = {
            'Up': None,
            'Left': None,
            'Down': None,
            'Right': None
        }

        #Prevents the Ghost from being able to turn around
        if self.direction == 'Up':
            directions.pop('Down')
        elif(self.direction == 'Left'):
            directions.pop('Right')
        elif(self.direction == 'Down'):
            directions.pop('Up')
        elif(self.direction == 'Right'):
            directions.pop('Left')

        # if(self.name == 'Pinky (Pink)'):
        #     print('\n' + str(directions))

        #Cycles through the dictionary to assign each key a rect value that determines the future position of each direction
        for key in directions:
            #Copies the rect of the Ghost
            rect_copy = pygame.Rect.copy(self.rect)

            if key == 'Up':
                rect_copy.centery = self.rect.centery - 2
            elif key == 'Left':
                rect_copy.centerx = self.rect.centerx - 2
            elif key == 'Down':
                rect_copy.centery = self.rect.centery + 2
            elif key == 'Right': 
                rect_copy.centerx = self.rect.centerx + 2

            directions[key] = rect_copy
        
        #Cycles through each new position to see which directions are a viable path
        for key in list(directions):
            #Debug code
                #print(str(key) + ": " + str(directions[key].collidelist(list_obstacles[2]) != -1))

            #Checks if the ghost's current direction is to exit the pink gate from the inside
            if(key == 'Up' and self.exiting_pink_gate(directions[key])):
                return 'Up'
            
            #Checks if the ghost's current direction is to enter the pink gate from the outside
            if(key in ['Left', 'Down', 'Right'] and self.entering_pink_gate(directions[key])):
                return 'Down'

            #Checks if the ghost's current direction is colliding with a wall. If so, the direction is removed from the list
            if(directions[key].collidelist(list_obstacles[2]) != -1):
                directions.pop(key)
        
        #Debug code
        # if(self.name == 'Pinky (Pink)'):
        #     print(str(directions) + '\n')

        '''
        Checks if the Ghost is in a frightened state. If so, the Ghost will move in a random direction
            Note: The program is checking if the Ghost's stand_by_state is False so that the Ghost can 
                  exit the gate region once Pac-Man eats enough dots
        '''
        if ((self.frightened_state_v1 or self.frightened_state_v2) and self.stand_by_state is False):
            random_direction = random.randint(0, len(directions) - 1)
            
            return list(directions.keys())[random_direction]
        
        #Else, the Ghost follows the direction closest to the target
        else:
            '''
            Calculates the distance between each rect and the target, then replaces the rect value to 
            a distance value for each respective direction

            Distance formula: d = √(x_2 - X_1)^2 + (y_2 - Y_1)^2
            
            Ex) Possible paths: {'Left': <rect(223, 237, 30, 30)>, 'Right': <rect(227, 237, 30, 30)>} 
                Target:         (368, 458)

                Result: {'Left': 243.6, 'Right': 241.5} <-- Right is the best direction to take
            '''
            for key in directions:
                rect = directions[key]

                difference_x = math.pow(target[0] - rect.centerx, 2) 
                difference_y = math.pow(target[1] - rect.centery, 2)

                distance = math.sqrt(difference_x + difference_y)

                directions[key] = distance

            '''
            Selects the direction whose associated value (distance) is the smallest. The expression `key=directions.get` 
            tells `min()` to compare dictionary entries using their values (distances) instead of their keys (direction names). 
            If distances are equal, dictionary insertion order (Up → Left → Down → Right) is used as a deterministic tie-breaker
            '''
            best_direction = min(directions, key=directions.get)

        return best_direction
    
    '''
    A method that checks the following condition:
        (1) Everytime the ghost switches to their chase state, they turn around 180 degrees
        (2) Helps the chase_state_movement_update & frightened_state_movement_update methods to have the ghost turn around only once
            Ex) Blinky turns around only once when transitioning into his Chase state or Frightened state
    '''
    def turn_around_condition(self):
        #Debug code
            # if(self.name == 'Blinky (Red)'):
            #     print('turn_around: ' + str(self.turn_around) + 
            #         '\nturn_around_occured_once: ' + str(self.turn_around_occured_once) + '\n')

        if(self.turn_around is False and self.turn_around_occured_once is False):
            self.turn_around = True

    #A method that helps the ghost turns around 180 degrees based on the turn_around_condition method
    def turn_around_action(self):
        '''
        This section prevents the ghost from turning around when they are inside the gate region
        '''

        gate_region = (240, 302)

        if(gate_region[0] > self.rect.centerx):
            range_x = self.rect.centerx / gate_region[0]
        else:
            range_x = gate_region[0] / self.rect.centerx
        
        if(gate_region[1] > self.rect.centery):
            range_y = self.rect.centery / gate_region[1]
        else: 
            range_y = gate_region[1] / self.rect.centery

        #Debug code
            # if(self.name == 'Blinky (Red)'):
            #     print('\nrange_x: ' + str(range_x))
            #     print('\nrange_y: ' + str(range_y))

        if range_x > 0.80 and range_y > 0.80:
            return

        '''
        This section helps the ghost turn around
        '''

        if(self.turn_around):
            if self.direction == 'Up':
                self.direction = 'Down'
            elif self.direction == 'Left':
                self.direction = 'Right'
            elif self.direction == 'Down':
                self.direction = 'Up'
            elif self.direction == 'Right': 
                self.direction = 'Left'
            
            #The ghost can only turn around once
            self.turn_around = False
            self.turn_around_occured_once = True

            #Debug code
                # if(self.name == 'Blinky (Red)'):
                #     print('turn_around: ' + str(self.turn_around) + 
                #         '\nturn_around_occured_once: ' + str(self.turn_around_occured_once) + '\n')

    #A method to allow a ghost to exit the pink gate at the start of the game or after they respawn
    def exiting_pink_gate(self, rect_copy):
        #Checks if the ghost is in their chase or scatter state
        if(self.chase_state or self.scatter_state or self.stand_by_state):
            '''
            This section helps the Ghost change direction to 'Up' when they are at the middle point of the gate. 
            Examples include:
                1) At the start of the round, Pinky needs to leave the gate
                2) Inky's & Clyde's Stand By state just ended and they need to leave the gate
                3) After Pac-Man respawns, all ghosts are still in their Chase state and their target is  
                   pointing in a direction that will make them collide with a wall inside the gate
                        Ex. Inky is facing to the right, and if he doesn't turn up, then he will colide to the 
                            far right wall of the gate region
            '''

            if(rect_copy.centerx > 240):
                range_x = 240 / rect_copy.centerx
            else:
                range_x = rect_copy.centerx / 240
            
            if(rect_copy.centery > 302):
                range_y = 302 / rect_copy.centery
            else: 
                range_y = rect_copy.centery / 302

            #If the range between the ghost and the gate meets this requirement, the ghost is allowed to pass through
            if(range_x >= 1.0 and range_y > 0.95):
                return True

            '''
            This section helps the Ghost to pass/phase through directly the pink gate wall 
            '''

            if(rect_copy.centerx > 240):
                range_x = 240 / rect_copy.centerx
            else:
                range_x = rect_copy.centerx / 240
            
            if(rect_copy.centery > 272):
                range_y = 272 / rect_copy.centery
            else: 
                range_y = rect_copy.centery / 272

            #If the range between the ghost and the gate meets this requirement, the ghost is allowed to pass through
            if(range_x > 0.95 and range_y > 0.93):
                return True
            
        #Debug code
            # if(self.name == 'Pinky (Pink)'):
                # print('range_x: ' + str(range_x))
                # print('\nrange_y: ' + str(range_y) + '\n')

                # print(range_x > 0.90 and range_y > 0.90)
    
    #A method to allow a ghost to enter the pink gate in their eaten state so that they can respawn
    def entering_pink_gate(self, rect_copy):
        #Checks if the ghost is in their eaten state
        if(self.eaten_state):
            if(rect_copy.centerx > 240):
                range_x = 240 / rect_copy.centerx
            else:
                range_x = rect_copy.centerx / 240
            
            if(rect_copy.centery > 272):
                range_y = 272 / rect_copy.centery
            else: 
                range_y = rect_copy.centery / 272
            
            #If the range between the ghost and the gate meets this requirement, the ghost is allowed to pass through
            if(range_x > 0.99 and range_y > 0.93):
                return True

        #Debug code
            # if(self.name == 'Pinky (Pink)'):
            #     print('range_x: ' + str(range_x))
            #     print('\nrange_y: ' + str(range_y) + '\n')

            #     print(range_x > 0.90 and range_y > 0.90)
        
    '''
    A method to cycle through the Ghost's movement based on their current state
        Note: Unlike the state_handler method, this method must be an if-else chain so that the ghost does not take
              on multiple movement updates. In contrast, the state_handler is designed to have a ghost behave 
              in intertwining states (Ex. Inky can both be in a stand_by and frightened state)
    '''
    def movement_update(self, list_obstacles, pac_man_direction, list_ghosts_positions, target):
        if(self.stand_by_state):
            self.stand_by_state_movement_update(list_obstacles)
        elif(self.chase_state):
            self.chase_state_movement_update(list_obstacles, pac_man_direction, list_ghosts_positions, target)
        elif(self.scatter_state):
            self.scatter_state_movement_update(list_obstacles)
        elif(self.frightened_state_v1 or self.frightened_state_v2):
            self.frightened_state_movement_update(list_obstacles)
        elif(self.eaten_state):
            self.eaten_state_movement_update(list_obstacles)
    
    #A method to update the Ghost's movement based on their stand by state
    def stand_by_state_movement_update(self, list_obstacles):        
        #An if statement helps the ghost move out of the gate region once Pac-Man eats enough dots
        if(self.stand_by_state_exit_condition):            
            #Gets the direction Inky should take to be at the front of the gate
            self.direction = self.direction_update(list_obstacles, (240, 252))

            #Debug code
                # print(self.direction)

            if self.direction == 'Up':
                self.rect.centery = self.rect.centery - 2
            elif self.direction == 'Left':
                self.rect.centerx = self.rect.centerx - 2
            elif self.direction == 'Down':
                self.rect.centery = self.rect.centery + 2
            elif self.direction == 'Right': 
                self.rect.centerx = self.rect.centerx + 2

            #Debug code
            self.display_ghost_target_on_map((240, 252))
        
        #An else statement to help the ghost move up and down repeatadly (essentially standing by until Pac-Man eats a certain number of dots)
        else:
            if(self.rect.centery == 294 and self.direction == 'Up'):
                self.direction = 'Down'
            elif(self.rect.centery == 310 and self.direction == 'Down'):
                self.direction = 'Up'

            if(self.direction == 'Down'):
                self.rect.centery = self.rect.centery + 1
            elif(self.direction == 'Up'):
                self.rect.centery = self.rect.centery - 1
    
    #An abstract method to update Ghost's movement based on their chase state
    def chase_state_movement_update(self):
        return None
    
    #An abstract method to update the Ghost's movement based on their scatter state
    def scatter_state_movement_update(self):
        return None

    #A method to update the Ghost's frightened state movement
    def frightened_state_movement_update(self, list_obstacles):
        #Debug code
            # print(self.name + " is in his frightened state")

        #Teleports Ghost to the other side of the tunnel
        self.tunnel_edge_teleport()

        #When entering Frightened state & dependent on the turn_around_condition, the ghost turns around 180 degrees
        self.turn_around_action()

        '''
        Returns the direction the Ghost should take to be in a scatter loop
            Ex) (240, 302) will be the target for all ghosts, but they will be forced to take random directions
        '''
        self.direction = self.direction_update(list_obstacles, (0, 0))

        #Debug code
            # print(self.direction)
        
        '''
        Move counter helps the Ghost move half of his speed when in a frightened state
        '''
        self.frightened_state_steps_per_frame += 1

        if self.frightened_state_steps_per_frame >= 2:
            #Updates the Ghost's movement based on the given direction
            if self.direction == 'Up':
                self.rect.centery = self.rect.centery - 2
            elif self.direction == 'Left':
                self.rect.centerx = self.rect.centerx - 2
            elif self.direction == 'Down':
                self.rect.centery = self.rect.centery + 2
            elif self.direction == 'Right': 
                self.rect.centerx = self.rect.centerx + 2
            
            self.frightened_state_steps_per_frame = 0

        #Debug code
        self.display_ghost_target_on_map((240, 302))
    
    #A method to update the Ghost's eaten state movement
    def eaten_state_movement_update(self, list_obstacles):
        #print(self.name + " is in his eaten state")

        #Teleports Ghost to the other side of the tunnel
        self.tunnel_edge_teleport()

        #Returns the direction the Ghost should take to get back to the ghost gate so that they can respawn
        self.direction = self.direction_update(list_obstacles, (240, 303))

        #Updates the Ghost's movement based on the given direction
        if self.direction == 'Up':
            self.rect.centery = self.rect.centery - 2
        elif self.direction == 'Left':
            self.rect.centerx = self.rect.centerx - 2
        elif self.direction == 'Down':
            self.rect.centery = self.rect.centery + 2
        elif self.direction == 'Right': 
            self.rect.centerx = self.rect.centerx + 2

        '''
        Because direction_update only checked if the first step was valid, the program needs to check if the 
        following step is also valid for the same direction
            Note: Movement is twice as fast for the eaten state compared to the other states
        '''
        if(self.eaten_state_steps_per_frame == 0):
            collision = pygame.Rect.copy(self.rect)

            if self.direction == 'Up':
                collision.centery = self.rect.centery - 2
            elif self.direction == 'Left':
                collision.centerx = self.rect.centerx - 2
            elif self.direction == 'Down':
                collision.centery = self.rect.centery + 2
            elif self.direction == 'Right': 
                collision.centerx = self.rect.centerx + 2
            
            #Debug code
                # print(collision)
            
            if(collision.collidelist(list_obstacles[2]) == -1):
                self.rect = collision

            self.eaten_state_steps_per_frame = 1
        else:
            self.eaten_state_steps_per_frame = 0

        #Debug code
        self.display_ghost_target_on_map((240, 303))
        
        #Debug code
            # print(self.steps_per_frame)
    
    #A method to help the Ghost travel through the tunnel edge at the left or right side of the game map
    def tunnel_edge_teleport(self):
        if(self.rect.centerx == -2 and self.rect.centery == 304):
            self.rect.center = (482, 304)
            self.direction = 'Left'            
        elif(self.rect.centerx == 482 and self.rect.centery == 304):
            self.rect.center = (-2, 304)
            self.direction = 'Right'

    #A debug method to visually display the ghost's current target on the surface they are currently on
    def display_ghost_target_on_map(self, target):
        #Creates font 
        pixel_font = pygame.font.Font('Fonts/Pixel/DePixelHalbfett.ttf', 12)

        if(self.name == 'Blinky (Red)'):
            text_color = 'Red'
        elif(self.name == 'Pinky (Pink)'):
            text_color = 'Pink'
        elif(self.name == 'Inky (Cyan)'):
            text_color = 'Cyan'
        elif(self.name == 'Clyde (Orange)'):
            text_color = 'Orange'

        #Sets up target text
        x_text = pixel_font.render('X', True, text_color)
        target_text = pixel_font.render('[TARGET]', True, text_color)

        #Gets the rect of the text
        x_text_rect = x_text.get_rect()
        target_text_rect = target_text.get_rect()

        #Applies the position the text should be blitted on
        x_text_rect.center = (target[0], target[1])
        target_text_rect.center = (target[0], target[1] + 20)

        #Blits the text on the current surface
        self.scene_surface.blit(x_text, x_text_rect)
        self.scene_surface.blit(target_text, target_text_rect)