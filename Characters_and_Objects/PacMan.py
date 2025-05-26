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

        #Variables to lower hitbox detection for eating pellets
        self.minimized_image = pygame.transform.scale(self.image, (25, 25))
        self.minimized_rect = self.minimized_image.get_rect()
        self.minimized_rect.center = self.rect.center

        #Variables to keep track of the scale, direction, movement boolean, and frame of Pac-Man
        self.horizontal_scale = horizontal_scale
        self.vertical_scale = vertical_scale
        self.direction = direction
        self.movement = movement
        self.frame = 0

        #Variables to keep track of Pac-Man's list of lives, high score, and current score
        self.list_of_lives = 3
        self.high_score = 0
        self.score = 0

        #Variables to check if Pac-Man ate a power pellet to can eat ghosts or is caught by a ghost
        self.eat_ghosts = False
        self.is_caught = False

        #Initializes a variable timer to dynamically change ghost state animation after Pac-Man eats a power pellet
        self.ghost_scatter_timer = 0

        #Variables to control character animation speed
        self.character_animation_speed = character_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds

        #Variables to create a timer for playing Pac-Man's death animation
        self.death_animation = False
        self.death_animation_timer = 0

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
    
    #A method to return Pac-Man's image
    def get_minimized_image(self):
        return self.minimized_image

    #A method to set a new image for Pac-Man
    def set_minimized_image(self, new_minimized_image):
        self.minimized_image = new_minimized_image

    #A method to return the rect of Pac-Man's image
    def get_minimized_rect(self):
        return self.minimized_rect
    
    #A method to set a new rect for Pac-Man
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
    
    #A method to return Pac-Man's animation speed
    def get_character_animation_speed(self):
        return self.character_animation_speed

    #A method to update Pac-Man's animation speed
    def set_character_animation_speed(self, new_character_animation_speed):
        self.character_animation_speed = new_character_animation_speed

    #A method to return Pac-Man's current frame
    def get_frame(self):
        return self.frame
    
    #A method to set a new frame for Pac-Man
    def set_frame(self, new_frame):
        self.frame = new_frame
    
    #A method to get Pac-Man's list of lives
    def get_list_of_lives(self):
        return self.list_of_lives

    #A method to set Pac-Man's list of lives
    def set_list_of_lives(self, new_list_of_lives):
        self.list_of_lives = new_list_of_lives
    
    #A method to get Pac-Man's high score
    def get_high_score(self):
        return self.high_score
    
    #A method to set Pac-Man's high score
    def set_high_score(self, new_high_score):
        self.high_score = new_high_score

    #A method to get Pac-Man's current score
    def get_score(self):
        return self.score
    
    #A method to set Pac-Man's current score
    def set_score(self, new_score):
        self.score = new_score
    
    #A method to return a boolean for Pac-Man's eat_ghosts
    def get_eat_ghosts(self):
        return self.eat_ghosts
    
    #A method to set a new boolean for Pac-Man's eat_ghosts
    def set_eat_ghosts(self, eat_ghosts):
        self.eat_ghosts = eat_ghosts

    #A method to return a boolean for Pac-Man's is_caught
    def get_is_caught(self):
        return self.is_caught
    
    #A method to set a new boolean for Pac-Man's is_caught
    def set_is_caught(self, new_is_caught):
        self.is_caught = new_is_caught

    #A method to return the ghost scatter timer
    def get_ghost_scatter_timer(self):
        return self.ghost_scatter_timer
    
    #A method to set the ghost scatter timer
    def set_ghost_scatter_timer(self, new_ghost_scatter_timer):
        self.ghost_scatter_timer = new_ghost_scatter_timer
    
    #A method to return a boolean for Pac-Man's death_animation
    def get_death_animation(self):
        return self.death_animation
    
    #A method to set a new boolean for Pac-Man's death_animation
    def set_death_animation(self, new_death_animation):
        self.death_animation = new_death_animation
    
    #A method to return a boolean for Pac-Man's death_animation_timer
    def get_death_animation_timer(self):
        return self.death_animation_timer
    
    #A method to set a new boolean for Pac-Man's death_animation_timer
    def set_death_animation_timer(self, new_death_animation_timer):
        self.death_animation_timer = new_death_animation_timer

    '''
    A series of methods to set the current movement frame of the character 
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
    
    '''
    A series of methods to set the current death frame of the character 
    '''
    def set_DF1(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_1.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    def set_DF2(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_2.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DF3(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_3.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DF4(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_4.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    def set_DF5(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_5.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    def set_DF6(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_6.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))

    def set_DF7(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_7.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DF8(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_8.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DF9(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_9.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DF10(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_10.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
    def set_DF11(self):
        self.image = pygame.image.load('Images/Pac-Man/Death/frame_11.png')
        self.image = pygame.transform.scale(self.image, (self.horizontal_scale, self.vertical_scale))
    
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
        
        '''
        A section to update Pac-Man's movement animation
            Note: If True, then the program updates the frame of the character. 
                  If False, then the program uses the old frame in runtime
        '''
        if(change_frame and self.movement):
            self.frame_update()

        '''
        A section to update Pac-Man's death animation through an iteration timer
            Note: This is a diffrent type of timer compared to the timer used to change the movement frames
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
        An if-else statement to teleport Pac-Man when the player travels through the tunnel edge 
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
    
    #A method for the player to eat pellets in the Gameplay Scene
    def eat_pellets(self, list_pellets, list_power_pellets, pellet_channel, power_pellet_channel, pellet_sound, power_pellet_sound): 
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
                #list_pellets[3][pellet_index].center = (0, 0)

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

            if(range_x > 0.95 and range_y > 0.95):
                #If Pac-Man has already eaten a Power Pellet, then the ghost scatter timer gets reset
                if(power_pellet_channel.get_busy()):
                    self.ghost_scatter_timer = -1
                
                power_pellet_channel.play(power_pellet_sound)

                list_power_pellets[1][power_pellet_index] = False

                '''
                Sets the eat_ghosts variable to True so the event handler method in the Gameplay Scene 
                can set the ghosts to scatter mode
                '''
                self.eat_ghosts = True

                self.score += 50
        
        #If Pac-Man's current score is higher than his high score, the high score value is updated
        if(self.score > self.high_score):
            self.high_score = self.score
    
    #A method to check if Pac-Man is caught by a ghost
    def check_is_caught(self, blinky, pinky, inky, clyde):
        '''
        Checks if the player's minimized hitbox is interacting with a pellet
        '''

        #Updates the position of the minimized rect hitbox
        self.minimized_rect.center = self.rect.center

        for ghost in [blinky, pinky, inky, clyde]:
            #Grabs the index of the ghost that collided with Pac-Man's minimized rect
            ghost_index = ghost.get_rect().colliderect(self.minimized_rect)
            
            '''
            If the index is -1, then Pac-Man did not collide with a ghost. Otherwise, the program grabs
            the ghost that collided with Pac-Man, and calculates the X & Y range percentage between the 
            ghost's center and Pac-Man's minimized rect center 
            '''
            if(ghost_index != -1):
                #Checks which ghost Pac-Man collided with
                if(blinky.get_rect().colliderect(self.minimized_rect) != -1):
                    ghost = blinky
                elif(pinky.get_rect().colliderect(self.minimized_rect) != -1):
                    ghost = pinky
                elif(inky.get_rect().colliderect(self.minimized_rect) != -1):
                    ghost = inky
                elif(clyde.get_rect().colliderect(self.minimized_rect) != -1):
                    ghost = clyde
            
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

                Note: If all the ghosts are in their vulnerable state after Pac-Man ate a Power
                    Pellet, then Pac-Man won't get caught 
                '''
                if(range_x > 0.98 and range_y > 0.98 and self.eat_ghosts is False):
                    self.set_is_caught(True)