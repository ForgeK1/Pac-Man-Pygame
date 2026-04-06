'''
Description: This class contains methods for how Pac-Man functions
'''

#Imports pygame libraries
import pygame
import math

class PacMan:
    #A constructor to initialize an instance of Pac-Man
    def __init__(self, horizontal_scale, vertical_scale, direction, x_position, y_position, movement, character_animation_speed, scene_surface):        
        #Variables to keep track the image and rect
        self.image = pygame.image.load('Images/Pac-Man/Movement/circle.png')
        self.image = pygame.transform.scale(self.image, (horizontal_scale, vertical_scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x_position, y_position)

        #Variables to that create a lower hitbox detection for Pac-Man to eat pellets eating pellets
        self.minimized_image = pygame.transform.scale(self.image, (25, 25))
        self.minimized_rect = self.minimized_image.get_rect()
        self.minimized_rect.center = self.rect.center

        #Variables to keep track of the scale, direction, movement boolean, and frame of Pac-Man
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale
        self.direction = direction
        self.movement = movement
        self.frame = 0

        #Variables to keep track of Pac-Man's list of lives, if he gained an extra life (when reaching 10,000 points), # of dots earen, high score, current score, score streak (the number of ghosts eaten in a row)
        self.list_of_lives = 3
        self.gained_extra_life = False
        self.dots_eaten = 0
        self.high_score = 0
        self.score = 0
        self.score_streak = 0

        #Variables to check if Pac-Man ate all pellets, is caught by a ghost, or ate a ghost while they were in a Frightened State
        self.ate_all_pellets = False
        self.is_caught = False
        self.ate_a_ghost = [None, False]

        #Variables to control character animation speed
        self.character_animation_speed = character_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds

        #Variables to create a timer for playing Pac-Man's death animation
        self.death_animation = False
        self.death_animation_timer = 0

        #A variable to point to the current surface Pac-Man is being blitted on (ex. Gameplay Scene --> gameplay_surface)
        self.scene_surface = scene_surface

    #A method to return Pac-Man's image
    def get_image(self):
        return self.image

    #A method to set a new image for Pac-Man
    def set_image(self, new_image):
        self.image = new_image

    #A method to return Pac-Man's image rect
    def get_rect(self):
        return self.rect
    
    #A method to set a new rect for Pac-Man
    def set_rect(self, new_rect):
        self.rect = new_rect
    
    #A method to return Pac-Man's minimized image
    def get_minimized_image(self):
        return self.minimized_image

    #A method to set a new minimized image for Pac-Man
    def set_minimized_image(self, new_minimized_image):
        self.minimized_image = new_minimized_image

    #A method to return the minimized rect of Pac-Man's image
    def get_minimized_rect(self):
        return self.minimized_rect
    
    #A method to set a new minimized rect for Pac-Man
    def set_minimized_rect(self, new_minimized_rect):
        self.minimized_rect = new_minimized_rect
    
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
    
    #A method to return Pac-Man's direction
    def get_direction(self):
        return self.direction
    
    #A method to set a new direction for Pac-Man
    def set_direction(self, new_direction):
        self.direction = new_direction
    
    #A method to return Pac-Man's movement boolean
    def get_movement(self):
        return self.movement

    #A method to set a new movement boolean for Pac-Man
    def set_movement(self, new_movement):
        self.movement = new_movement

    #A method to return Pac-Man's frame
    def get_frame(self):
        return self.frame
    
    #A method to set a new frame for Pac-Man
    def set_frame(self, new_frame):
        self.frame = new_frame

    #A method to return Pac-Man's list of lives
    def get_list_of_lives(self):
        return self.list_of_lives

    #A method to set a new list_of_lives for Pac-Man
    def set_list_of_lives(self, new_list_of_lives):
        self.list_of_lives = new_list_of_lives

    #A method to return Pac-Man's gained_extra_life boolean
    def get_gained_extra_life(self):
        return self.gained_extra_life

    #A method to set a new gained_extra_life boolean Pac-Man
    def set_gained_extra_life(self, new_gained_extra_life):
        self.gained_extra_life = new_gained_extra_life

    #A method to return Pac-Man's number of dots_eaten (in a single level)
    def get_dots_eaten(self):
        return self.dots_eaten

    #A method to set a new number of dots_eaten (in a single level) for Pac-Man
    def set_dots_eaten(self, new_number_dots_eaten):
        self.dots_eaten = new_number_dots_eaten
    
    #A method to return Pac-Man's high_score
    def get_high_score(self):
        return self.high_score
    
    #A method to set a new high_score for Pac-Man
    def set_high_score(self, new_high_score):
        self.high_score = new_high_score

    #A method to return Pac-Man's score
    def get_score(self):
        return self.score
    
    #A method to set a new score for Pac-Man
    def set_score(self, new_score):
        self.score = new_score

    #A method to return Pac-Man's score_streak
    def get_score_streak(self):
        return self.score_streak
    
    #A method to set new score_streak for Pac-Man
    def set_score_streak(self, new_score_streak):
        self.score_streak = new_score_streak
    
    #A method to return Pac-Man's ate_all_pellets boolean
    def get_ate_all_pellets(self):
        return self.ate_all_pellets
    
    #A method to set a new ate_all_pellets boolean for Pac-Man
    def set_ate_all_pellets(self, new_ate_all_pellets):
        self.ate_all_pellets = new_ate_all_pellets

    #A method to return Pac-Man's is_caught boolean
    def get_is_caught(self):
        return self.is_caught
    
    #A method to set a new is_caught boolean for Pac-Man
    def set_is_caught(self, new_is_caught):
        self.is_caught = new_is_caught

    #A method to return Pac-Man's ate_a_ghost boolean
    def get_ate_a_ghost(self):
        return self.ate_a_ghost
    
    #A method to set a new ate_a_ghost boolean for Pac-Man
    def set_ate_a_ghost(self, new_ghost, ghost_eaten):
        self.ate_a_ghost = (new_ghost, ghost_eaten)
    
    #A method to return Pac-Man's character_animation_speed
    def get_character_animation_speed(self):
        return self.character_animation_speed

    #A method to set a new character_animation_speed Pac-Man
    def set_character_animation_speed(self, new_character_animation_speed):
        self.character_animation_speed = new_character_animation_speed

    #A method to return Pac-Man's last_updated_time (in miliseconds) to track his character_animation_speed
    def get_last_updated_time(self):
        return self.last_updated_time
    
    #A method to set a new last_updated_time for Pac-Man (in miliseconds) to track his character_animation_speed
    def set_last_updated_time(self, new_last_updated_time):
        self.last_updated_time = new_last_updated_time
    
    #A method to return Pac-Man's death_animation boolean
    def get_death_animation(self):
        return self.death_animation
    
    #A method to set a new death_animation boolean for Pac-Man
    def set_death_animation(self, new_death_animation):
        self.death_animation = new_death_animation
    
    #A method to return Pac-Man's death_animation_timer
    def get_death_animation_timer(self):
        return self.death_animation_timer
    
    #A method to set a new death_animation_timer for Pac-Man
    def set_death_animation_timer(self, new_death_animation_timer):
        self.death_animation_timer = new_death_animation_timer

    '''
    A series of methods to set the current movement frame of Pac-Man
    '''

    #Circle frame
    def set_CF(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/circle.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Right movement frame 1
    def set_RMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Right movement frame 2
    def set_RMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/right_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Left movement frame 1
    def set_LMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/left_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Left movement frame 2
    def set_LMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/left_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up movement frame 1
    def set_UMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/up_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Up movement frame 2
    def set_UMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/up_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down movement frame 1
    def set_DMF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/down_frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Down movement frame 2
    def set_DMF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Movement/down_frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    '''
    A series of methods to set the current death frame of the character 
    '''

    #Death Frame 1
    def set_DF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Death Frame 2
    def set_DF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Death Frame 3
    def set_DF3(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_3.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Death Frame 4
    def set_DF4(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_4.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Death Frame 5
    def set_DF5(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_5.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Death Frame 6
    def set_DF6(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_6.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    #Death Frame 7
    def set_DF7(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_7.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Death Frame 8
    def set_DF8(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_8.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Death Frame 9
    def set_DF9(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_9.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Death Frame 10
    def set_DF10(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_10.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Death Frame 11
    def set_DF11(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_11.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #Death Frame 12
    def set_DF12(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_12.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    #A method to check what frame Pac-Man is in
    def frame_update(self):
        #If Pac-Man is not caught, the program uses the movement frames
        if(self.is_caught is False):
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
                    
        #Else, the program uses the death frames
        else: 
            match self.frame:
                case 0:
                    self.set_DF1()
                    
                    self.frame = 1
                case 1:
                    self.set_DF2()

                    self.frame = 2
                case 2:
                    self.set_DF3()

                    self.frame = 3
                case 3:
                    self.set_DF4()

                    self.frame = 4
                case 4:
                    self.set_DF5()

                    self.frame = 5
                case 5:
                    self.set_DF6()

                    self.frame = 6
                case 6:
                    self.set_DF7()

                    self.frame = 7
                case 7:
                    self.set_DF8()

                    self.frame = 8
                case 8:
                    self.set_DF9()

                    self.frame = 9
                case 9:
                    self.set_DF10()

                    self.frame = 10
                case 10:
                    self.set_DF11()

                    self.frame = 11
                case 11:
                    self.set_DF12()

                    self.frame = 11
        
        #Debug code for checking frame change
            #print(self.frame)
    
    #A method to update the animation speed for Pac-Man
    def animation_update(self):        
        #Gets the current time in miliseconds
        curr_time = pygame.time.get_ticks()
        
        #A variable to keep track of changing frame of characters
        change_frame = False

        '''
        Updates the animation frame of each character if enough time has passed
            ex) 0 - 0 > 200     False
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
        
        '''
        A section to update Pac-Man's movement animation
            NOTE: If True, the program updates the frame of the character. 
                  If False, the program uses the old frame in runtime
        '''
        if(change_frame and self.movement):
            self.frame_update()

        '''
        A section to update Pac-Man's death animation through an iteration timer
            NOTE: This is a diffrent type of timer compared to the timer used to change the movement frames
                  of the characters 
        '''
        if(self.death_animation):  
            if(self.death_animation_timer % 7 == 0):                
                self.frame_update()
            
            self.death_animation_timer += 1

            #Debug code
                #print(self.death_animation_timer)
    
    #A method for the player to control Pac-Man's movement position in the Gameplay Scene
    def movement_update(self, event, list_obstacles):
        '''
        An if-else chain to teleport Pac-Man when the player travels through the tunnel edge 
        at the left or right side of the game map
        ''' 
        if(self.rect.centerx == -2 and self.rect.centery == 304):
            self.direction = 'Left'
            self.rect.center = (482, 304)
        elif(self.rect.centerx == 482 and self.rect.centery == 304):
            self.direction = 'Right'
            self.rect.center = (-2, 304)
        
        #Creates direction variables for Pac-Man's new and ongoing (old) directions
        new_direction = self.direction
        old_direction = self.direction
        
        '''
        Applies a value to new direction if the player pressed any arrow keys 
            NOTE: If the player didn't press any arrow keys, new & old direction 
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
        If Pac-Man's new direction and position does result in a collision with any walls,  
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
    
    #A method that allows Pac-Man to eat pellets in the Gameplay Scene
    def eat_pellets(self, list_ghosts, list_pellets, list_power_pellets, pellet_channel, power_pellet_channel, pellet_sound, power_pellet_sound): 
        '''
        Checks if the player's minimized hitbox is interacting with a pellet
        '''

        #Updates the position of the minimized rect hitbox
        self.minimized_rect.center = self.rect.center

        #Grabs the index of the pellet that collided with Pac-Man's minimized rect
        pellet_index = self.minimized_rect.collidelist(list_pellets[3])

        '''
        If pellet's index is -1 and the boolean visibility is False, then Pac-Man did not collide 
        with any pellets. Otherwise, the program calculates the X & Y range percentage between the 
        pellet's center and Pac-Man's minimized rect center 
        '''
        if(pellet_index != -1 and list_pellets[1][pellet_index]):
            if(self.minimized_rect.centerx > list_pellets[3][pellet_index].centerx):
                range_x = list_pellets[3][pellet_index].centerx / self.minimized_rect.centerx
            else:
                range_x = self.minimized_rect.centerx / list_pellets[3][pellet_index].centerx
            
            if(self.minimized_rect.centery > list_pellets[3][pellet_index].centery):
                range_y = list_pellets[3][pellet_index].centery / self.minimized_rect.centery
            else: 
                range_y = self.minimized_rect.centery / list_pellets[3][pellet_index].centery

            #Debug code
                #print('\n--')
                #print('range_x: ' + str(range_x * 100) + ' %')
                #print('range_y: ' + str(range_y * 100) + ' %')
                #print('--')

            '''
            If the X & Y range between the pellet's rect and Pac-man's minimized rect is
            98 % (or 2 % apart), then Pac-Man "eats" the pellet
            '''
            if(range_x >= 0.98 or range_y >= 0.98): 
                if(pellet_channel.get_busy() is False):
                    pellet_channel.play(pellet_sound)
                
                list_pellets[1][pellet_index] = False
                
                self.dots_eaten += 1
                self.score += 10
        
        '''
        Checks if the player's minimized hitbox is interacting with a power pellet
        '''

        power_pellet_index = self.minimized_rect.collidelist(list_power_pellets[3])

        if(power_pellet_index != -1 and list_power_pellets[1][power_pellet_index]):
            if(self.minimized_rect.centerx > list_power_pellets[3][power_pellet_index].centerx):
                range_x = list_power_pellets[3][power_pellet_index].centerx / self.minimized_rect.centerx
            else:
                range_x = self.minimized_rect.centerx / list_power_pellets[3][power_pellet_index].centerx
            
            if(self.minimized_rect.centery > list_power_pellets[3][power_pellet_index].centery):
                range_y = list_power_pellets[3][power_pellet_index].centery / self.minimized_rect.centery
            else: 
                range_y = self.minimized_rect.centery / list_power_pellets[3][power_pellet_index].centery

            #Pac-Man eats a power-pellet
            if(range_x > 0.95 and range_y > 0.95):
                '''
                Updates the ghost's state and variables for the power pellet
                    NOTE: These two states are not set to True once the power pellet channel is done because
                          the state_handler method in the ghost class automatically does so
                '''
                for ghost in list_ghosts:
                    #Checks if the ghost is in an Eaten State. If so, the ghost will not change into a Frightened State
                    if(ghost.get_eaten_state()):
                        continue

                    ghost.set_chase_state(False)
                    ghost.set_scatter_state(False)
                    ghost.set_frightened_state_v1(True)
                    ghost.set_frame(0)
                    ghost.set_ghost_scatter_timer(0)

                    #This statement resets the condition for the ghost to turn around again when transitioning to their Frightened state
                    ghost.set_turn_around_occured_once(False)
                
                power_pellet_channel.play(power_pellet_sound)

                list_power_pellets[1][power_pellet_index] = False

                self.dots_eaten += 1
                self.score += 50
        
        #If Pac-Man's current score is higher than his high score, the high score value is updated
        if(self.score > self.high_score):
            self.high_score = self.score

        #If Pac-Man reaches or gets past 10,000 points, he gains an extra life
        if(self.high_score >= 10000 and self.gained_extra_life is False):
            pygame.mixer_music.load('Audio/Sound Effects/Pac-Man Extra Life.wav')
            pygame.mixer_music.play()

            self.list_of_lives = self.list_of_lives + 1
            self.gained_extra_life = True
    
    #A method to check if Pac-Man ate all of the pellets in the Gameplay Scene
    def check_ate_all_pellets(self, list_pellets, list_power_pellets):
        ate_all_small_pellets = True
        ate_all_power_pellets = True
        
        if True in list_pellets[1]:
            ate_all_small_pellets = False
        
        if True in list_power_pellets[1]:
            ate_all_power_pellets = False
        
        #Debug code
            #print(str(ate_all_small_pellets) + ' and ' + str(ate_all_power_pellets))
            #print(ate_all_small_pellets and ate_all_power_pellets)
        
        self.ate_all_pellets = ate_all_small_pellets and ate_all_power_pellets

    #A method to check if Pac-Man is caught by a ghost in the Gameplay Scene
    def check_is_caught(self, blinky, pinky, inky, clyde):
        #Updates the position of Pac-Man's minimized rect hitbox
        self.minimized_rect.center = self.rect.center

        #Checks which ghost Pac-Man collided with
        if(blinky.get_rect().colliderect(self.minimized_rect)):
            ghost = blinky
        elif(pinky.get_rect().colliderect(self.minimized_rect)):
            ghost = pinky
        elif(inky.get_rect().colliderect(self.minimized_rect)):
            ghost = inky
        elif(clyde.get_rect().colliderect(self.minimized_rect)):
            ghost = clyde
        else:
            return
    
        if(self.minimized_rect.centerx > ghost.get_rect().centerx):
            range_x = ghost.get_rect().centerx / self.minimized_rect.centerx
        else:
            range_x = self.minimized_rect.centerx / ghost.get_rect().centerx
        
        if(self.minimized_rect.centery > ghost.get_rect().centery):
            range_y = ghost.get_rect().centery / self.minimized_rect.centery
        else: 
            range_y = self.minimized_rect.centery / ghost.get_rect().centery
        
        '''
        If the X & Y range between the ghost's rect and Pac-man's minimized rect is 
        98 % (or 2 % apart), then Pac-Man is "caught" by the ghost
        '''
        if((range_x > 0.97 and range_y > 0.97) and (ghost.get_chase_state() is True or ghost.get_scatter_state() is True) and (ghost.eaten_state is False)):
            self.is_caught = True
    
    #A method to check if Pac-Man ate a ghost while the ghost is in their Frightened State in the Gameplay Scene
    def check_if_ate_a_ghost(self, ghost_eaten_channel, pac_man_ate_ghost_sound, blinky, pinky, inky, clyde):
        #Updates the position of Pac-Man's minimized rect hitbox
        self.minimized_rect.center = self.rect.center

        #Checks which ghost Pac-Man collided with
        if(blinky.get_rect().colliderect(self.minimized_rect)):
            ghost = blinky
        elif(pinky.get_rect().colliderect(self.minimized_rect)):
            ghost = pinky
        elif(inky.get_rect().colliderect(self.minimized_rect)):
            ghost = inky
        elif(clyde.get_rect().colliderect(self.minimized_rect)):
            ghost = clyde
        else:
            return
    
        if(self.minimized_rect.centerx > ghost.get_rect().centerx):
            range_x = ghost.get_rect().centerx / self.minimized_rect.centerx
        else:
            range_x = self.minimized_rect.centerx / ghost.get_rect().centerx
        
        if(self.minimized_rect.centery > ghost.get_rect().centery):
            range_y = ghost.get_rect().centery / self.minimized_rect.centery
        else: 
            range_y = self.minimized_rect.centery / ghost.get_rect().centery            
        
        '''
        If the X & Y range between the ghost's rect and Pac-man's minimized rect is 
        98 % (or 2 % apart), then Pac-Man "ate" a ghost
        '''
        if((range_x > 0.95 and range_y > 0.95) and (ghost.get_frightened_state_v1() is True or ghost.get_frightened_state_v2() is True) and (ghost.get_eaten_state() is False)):
            self.ate_a_ghost = (ghost, True)
            
            ghost.set_frightened_state_v1(False)
            ghost.set_frightened_state_v2(False)
            ghost.set_eaten_state(True)
            ghost.set_movement(False)
            ghost.set_frame(0)
            
            ghost_eaten_channel.play(pac_man_ate_ghost_sound)

            #Updates Pac-Man's score based on the number of ghosts Pac-Man ate in a row
            self.score_streak += 1
            self.score += int(math.pow(2, self.score_streak) * 100) #200, 400, 800, 1600 (the streak keeps going so long as the power_pellet channel is active)

            #Debug code
                #print(self.ate_a_ghost)