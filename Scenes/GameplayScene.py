'''
Description: The GameplayScene class helps run the levels of the game. For every level the player passes,
             the high score continues to increase and the ghosts will become more difficult
'''

#Imports pygame and other libraries
import pygame
import os
from Characters_and_Objects.PacMan import PacMan
from Characters_and_Objects.Ghosts.Blinky import Blinky
from Characters_and_Objects.Ghosts.Pinky import Pinky
from Characters_and_Objects.Ghosts.Inky import Inky
from Characters_and_Objects.Ghosts.Clyde import Clyde
from Characters_and_Objects.Pellet import Pellet
from Characters_and_Objects.PowerPellet import PowerPellet

class GameplayScene:
    #A constructor to initialize an instance of Gameplay Scene
    def __init__(self, display_surface, game_state_manager, WINDOW_WIDTH, WINDOW_HEIGHT):
        #Initializes the display surface and game state manager
        self.display_surface = display_surface
        self.game_state_manager = game_state_manager
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

        '''
        Sets up the Gameplay Scene surface to continiously update and blit it onto the display surface
            Note: pygame.SRCALPHA must be included to access the alpha channel so that the program
                  can change the transparency of the surface object below during runtime
        '''
        self.gameplay_surface = pygame.Surface((self.WINDOW_WIDTH, self.WINDOW_HEIGHT), pygame.SRCALPHA)

        #Initializes a variable current level
        self.level_counter = 5

        #Initializes the character objects
        self.pac_man = PacMan(30, 30, 'Left', self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 138, True, 50)
        self.blinky = Blinky(30, 30, "Left", self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 68, True, 100, self.level_counter, self.game_state_manager)
        self.pinky = Pinky(30, 30, "Down", self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 20, True, 100, self.level_counter, self.game_state_manager)
        self.inky = Inky(30, 30, "Up", self.WINDOW_WIDTH / 2 - 33, self.WINDOW_HEIGHT / 2 - 20, True, 100, self.level_counter, self.game_state_manager)
        self.clyde = Clyde(30, 30, "Up", self.WINDOW_WIDTH / 2 + 33, self.WINDOW_HEIGHT / 2 - 20, True, 100, self.level_counter, self.game_state_manager)
        
        #Initializes two lists of obstacles for the game map
        self.list_blue_obstacles = None
        self.list_white_obstacles = None
        self.load_obstacles()
        self.default_obstacles = True #True = blue obstacles, False = white obstacles

        #Initializes the pellet objects
        self.pellet = Pellet('Images/Pellets/pellet.png')
        self.power_pellet = PowerPellet(200)

        #Initializes the list of pellets for the game map
        self.list_pellets = self.pellet.load_pellets()
        self.list_power_pellets = self.power_pellet.load_power_pellets()

        #Initializes pygame mixer channels for utilizing music or sound effects
        self.end_round_channel = pygame.mixer.Channel(1)
        self.pellet_channel = pygame.mixer.Channel(2)
        self.power_pellet_channel = pygame.mixer.Channel(3)
        self.siren_channel = pygame.mixer.Channel(4)
        self.ghost_eaten_channel = pygame.mixer.Channel(5)
        self.ghost_return_channel = pygame.mixer.Channel(6)

        #Initializes music and sound effects
        self.pac_man_death_sound = pygame.mixer.Sound('Audio/Sound Effects/Pac-Man Death.wav')
        self.pellet_sound = pygame.mixer.Sound('Audio/Sound Effects/Waka (Cut Version).wav')
        self.power_pellet_sound = pygame.mixer.Sound('Audio/Sound Effects/Power-Up.wav')
        self.siren_v1_sound = pygame.mixer.Sound('Audio/Sound Effects/Ghost Siren V1.wav')
        self.siren_v2_sound = pygame.mixer.Sound('Audio/Sound Effects/Ghost Siren V2.wav')
        self.pac_man_ate_ghost_sound = pygame.mixer.Sound('Audio/Sound Effects/Pac-Man Eating A Ghost.wav')
        self.ghost_return = pygame.mixer.Sound('Audio/Sound Effects/Ghost Return.wav')

        #Initializes variables to start a new round
        self.round_intro = True
        self.fresh_start = True
        self.pac_man_life_deduct = True
        self.transition_to_next_round_timer = 0

        #Initializes variables to end the round
        self.ghost_disappear_timer = 0
        self.game_over_text_timer = 0
        self.transition_to_main_menu_timer = 0
        self.round_end = False
        self.pac_man_death_sound_is_playing = False
        self.transition_to_main_menu = False

        #Initializes a variable to showcase the "1UP" text for the Gameplay Scene UI
        self.one_up_text_timer = 0

    #A method to run the Gameplay Scene
    def run(self, event):  
        #Fills the background of the display surface
        self.display_surface.fill('black')

        #Checks if the player is starting a new round
        if(self.round_intro):
            self.start_round()
        #Checks if the the game is ending the round
        elif(self.round_end):
            self.end_round()
        #Else, the player is playing the game
        else:     
            #A method to set up the updated Gameplay Scene surface during when the player controls Pac-Man
            self.set_up_gameplay_surface()

            #A method to check player and game events for the Gameplay Scene
            self.event_handler(event)            

            #Blits the Gameplay Scene surface onto the display surface
            self.display_surface.blit(self.gameplay_surface, (0, 0))
    
    #A method to setup and blit surface objects onto the Gameplay Scene during gameplay 
    def set_up_gameplay_surface(self):        
        #Resets the Gameplay Scene background
        self.gameplay_surface.fill('black')

        '''
        Updates Pac-Man's animation based on his character_animation_speed variable, and blits each ghost's 
        images and rects onto the Gameplay Scene
            Note: Pac-Man's section comes before blitting the pellets because the pellets would show up in his mouth. 
                  Note that, the pellets dissapear once they reach Pac-Man's mouth. In contrast, the ghosts are blit 
                  after the pellets since the pellets do not dissapear when they interact with them
        '''
        self.pac_man.animation_update()
        self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())

        #Blits obstacles on the Gameplay Scene
        for i in range(len(self.list_blue_obstacles[0])): 
            self.gameplay_surface.blit(self.list_blue_obstacles[1][i], self.list_blue_obstacles[2][i])

        #Blits the pellets on the Gameplay Scene
        for i in range(len(self.list_pellets[0])):
                #Checks if the pellet hasn't been eaten by Pac-Man
                if(self.list_pellets[1][i]):
                    self.gameplay_surface.blit(self.list_pellets[2], self.list_pellets[3][i])

        #Blits the power pellets on the Gameplay Scene
        for i in range(len(self.list_power_pellets[0])):
            #Checks if the power pellet hasn't been eaten by Pac-Man
            if(self.list_power_pellets[1][i]):
                #Updates the animation of the power pellet
                self.list_power_pellets[2] = self.power_pellet.animation_update(self.list_power_pellets[2])

                self.gameplay_surface.blit(self.list_power_pellets[2], self.list_power_pellets[3][i])
        '''
        Updates each ghost's animation based on their character_animation_speed variable, and blits each ghost's 
        images and rects onto the Gameplay Scene
        '''
        for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
            ghost.animation_update()
            self.gameplay_surface.blit(ghost.get_image(), ghost.get_rect())
        
        #A method to showcase list of lives, high score, current score, food images, etc. for the Gameplay Scene
        self.interface_update()

    #A method to load and update the Gameplay Scene interface (list of lives, high score, current score, food images, etc.)
    def interface_update(self):
        '''
        A section to set up Pac-Man's list of lives
        '''
        
        #Grabs Pac-Man's list of lives
        list_of_lives = self.pac_man.get_list_of_lives()
        life_image_offset = 40

        #A while loop to blit each life Pac-Man has onto the Gameplay Scene surface
        while list_of_lives > 0:
            life_image = pygame.transform.scale(pygame.image.load('Images/Pac-Man/Movement/left_frame_1.png'), (40, 40))
            life_rect = life_image.get_rect()
            life_rect.bottomleft = (life_image_offset, 633)

            self.gameplay_surface.blit(life_image, life_rect)

            life_image_offset += 45

            list_of_lives -= 1
        
        '''
        A section to set up Pac-Man's high score and score
        '''

        #Grabs Pac-Man's high score
        if(self.pac_man.get_high_score() == 0):
            high_score = '00'
        else:
            high_score = self.pac_man.get_high_score()
        
        #Grabs Pac-Man's current score
        if(self.pac_man.get_score() == 0):
            score = '00'
        else:
            score = self.pac_man.get_score()

        pixel_font = pygame.font.Font('Fonts/Pixel/DePixelHalbfett.ttf', 18)

        #Sets up 1UP text
        one_up_text = pixel_font.render('1UP', True, 'White')
        one_up_text_rect = one_up_text.get_rect()
        one_up_text_rect.topright = (100, 5)

        #Sets up Pac-Man's score number text
        score_num_text = pixel_font.render(str(score), True, 'White')
        score_num_text_rect = score_num_text.get_rect()
        score_num_text_rect.topright = (115, 30)

        #Sets up Pac-Man's high score text
        high_score_text = pixel_font.render('HIGH  SCORE', True, 'White')
        high_score_text_rect = high_score_text.get_rect()
        high_score_text_rect.topright = (320, 5)
        
        #Sets up Pac-Man's high score number text
        high_score_num_text = pixel_font.render(str(high_score), True, 'White')
        high_score_num_text_rect = high_score_num_text.get_rect()
        high_score_num_text_rect.topright = (290, 30)

        #Blits the 1UP text on the Gameplay Scene via a timer
        if(self.one_up_text_timer <= 15):
            self.gameplay_surface.blit(one_up_text, one_up_text_rect)
            self.one_up_text_timer += 1
        elif(self.one_up_text_timer > 15 and self.one_up_text_timer <= 30): 
            self.one_up_text_timer += 1
        else:
            self.one_up_text_timer = 0

        #Blits the rest of the texts on the Gameplay Scene
        self.gameplay_surface.blit(score_num_text, score_num_text_rect)
        self.gameplay_surface.blit(high_score_text, high_score_text_rect)
        self.gameplay_surface.blit(high_score_num_text, high_score_num_text_rect)

    #A method to load a list of blue and white that contains an set of coordinates, images, and rects of each image
    def load_obstacles(self):
        '''
        First parameter:  [X, Y] coordinates of the image
        Second parameter: Surface object of the image
        Third parameter:  Rect of the image
        Fourth parameter: Contains the index for the pink gate image
        '''
        self.list_blue_obstacles = [[], [], [], -1]

        #An index to keep track of which file is the gate image in the for loop below
        gate_index = 0

        #A for loop to iterate through all image files in the obstacles folder
        for filename in os.listdir('Images/Obstacles/Blue'):
            '''
            A section to grab the top left X & Y coordinate of each file as an array 
                Note: The coordinates for the file are stored in the file name
            '''
            coordinates = filename
            coordinates = coordinates.removeprefix('(')
            coordinates = coordinates.removesuffix(').png')
            coordinates = coordinates.split(',')
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            
            #Appends the coordinates in the first list
            self.list_blue_obstacles[0].append(coordinates)

            '''
            A section to grab the image and rect of the file
            '''
            image = pygame.image.load('Images/Obstacles/Blue/' + filename)
            image_rect = image.get_rect()
            image_rect.topleft = (coordinates[0], coordinates[1])

            #Stores image in the second list and the rect in the third list
            self.list_blue_obstacles[1].append(image)
            self.list_blue_obstacles[2].append(image_rect)

            '''
            A section to save the index of the pink gate image
            '''
            if(filename.removesuffix('.png') == '(223,268)'):
                self.list_blue_obstacles[3] = gate_index 
            elif(self.list_blue_obstacles[3] == -1):
                gate_index += 1

        self.list_white_obstacles = [[], [], []]

        for filename in os.listdir('Images/Obstacles/White'):
            coordinates = filename
            coordinates = coordinates.removeprefix('(')
            coordinates = coordinates.removesuffix(').png')
            coordinates = coordinates.split(',')
            coordinates[0] = int(coordinates[0])
            coordinates[1] = int(coordinates[1])
            
            self.list_white_obstacles[0].append(coordinates)

            image = pygame.image.load('Images/Obstacles/White/' + filename)
            image_rect = image.get_rect()
            image_rect.topleft = (coordinates[0], coordinates[1])

            self.list_white_obstacles[1].append(image)
            self.list_white_obstacles[2].append(image_rect)

    #A method to showcase the start of the round to the player
    def start_round(self):       
        #Resets the Gameplay Scene background
        self.gameplay_surface.fill('black')

        #Checks if the player is starting the game for the first time
        if(self.fresh_start):
            #Checks if the Pac-Man start theme is still playing. If the theme ends, then the Pac-Man & the ghosts start moving
            if(pygame.mixer_music.get_busy() is False):
                self.round_intro = False
                self.fresh_start = False
                pygame.mixer_music.unload()

                #Resumes all character movements
                self.pac_man.set_movement(True)

                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:  
                    ghost.set_movement(True)
            
            '''
            A section to set up the obstacles and pellets
            '''
            
            #Sets up the obstacles on the Gameplay Scene 
            for i in range(len(self.list_blue_obstacles[0])): 
                self.gameplay_surface.blit(self.list_blue_obstacles[1][i], self.list_blue_obstacles[2][i])
            
            #Sets up the pellets on the Gameplay Scene
            for i in range(len(self.list_pellets[0])):
                if(self.list_pellets[1][i]):
                    self.gameplay_surface.blit(self.list_pellets[2], self.list_pellets[3][i])

            #Sets up the power pellets on the Gameplay Scene
            for i in range(len(self.list_power_pellets[0])):
                if(self.list_power_pellets[1][i]):
                    self.gameplay_surface.blit(self.list_power_pellets[2], self.list_power_pellets[3][i])
            
            '''
            A section to dynamically showcase text based on the number of seconds left in the Pac-Man start theme
            '''

            pixel_font = pygame.font.Font('Fonts/Pixel/DePixelHalbfett.ttf', 18)

            #Displays the "READY!" text throughout the entire theme
            ready_text = pixel_font.render('READY!', True, 'Yellow')
            ready_text_rect = ready_text.get_rect()
            ready_text_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 35)

            self.gameplay_surface.blit(ready_text, ready_text_rect)

            #Displays the "PLAYER ONE" text up to 3 seconds of the theme
            if(pygame.mixer_music.get_pos() / 1000 >= 0.01 and pygame.mixer_music.get_pos() / 1000 <= 2.5):
                player_one_text = pixel_font.render('PLAYER ONE', True, 'Cyan')
                player_one_text_rect = player_one_text.get_rect()
                player_one_text_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 68)

                self.gameplay_surface.blit(player_one_text, player_one_text_rect)
            #Else, the program displays the characters and their positions before the theme ends
            else:
                '''
                Deducts one life from Pac-Man on the Gameplay Scene interface when  
                Pac-Man & the ghosts show up
                '''
                if(self.pac_man_life_deduct):
                    self.pac_man.set_list_of_lives(self.pac_man.get_list_of_lives() - 1)

                    self.pac_man_life_deduct = False

                #Sets Pac-Man's variables back to normal
                self.pac_man.set_direction('Left')
                self.pac_man.set_frame(0)
                self.pac_man.set_CF()
                self.pac_man.set_death_animation_timer(0)
                self.pac_man.frame_update()

                #Resets all ghosts to their default direction
                self.blinky.set_direction('Left')
                self.pinky.set_direction('Down')
                self.inky.set_direction('Up')
                self.clyde.set_direction('Up')

                #Resets the all ghosts' state, frame, and timers back to normal
                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                    ghost.set_frame(0)
                    ghost.set_chase_state(False)
                    ghost.set_scatter_state(True) #The first phase ghosts will be in at the start of each round is Scatter phase
                    ghost.set_frightened_state_v1(False)
                    ghost.set_frightened_state_v2(False)
                    ghost.set_eaten_state(False)
                    ghost.reset_chase_and_scatter_cycle()
                    ghost.set_ghost_scatter_timer(0)
                    ghost.frame_update()
                
                #Resets the position of all characters
                self.pac_man.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 138)
                self.blinky.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 68)
                # self.pinky.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 20)
                # self.inky.get_rect().center = (self.WINDOW_WIDTH / 2 - 33, self.WINDOW_HEIGHT / 2 - 20)
                # self.clyde.get_rect().center = (self.WINDOW_WIDTH / 2 + 33, self.WINDOW_HEIGHT / 2 - 20)

                self.pinky.get_rect().center = (238, 352)
                self.inky.get_rect().center = (160, 298)
                self.clyde.get_rect().center = (318, 300)

                #Blits the characters onto the Gameplay surface
                self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())

                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                    self.gameplay_surface.blit(ghost.get_image(), ghost.get_rect())

            #A method to showcase list of lives, high score, current score, food images, etc. for the start round
            self.interface_update()

            #Blits the Gameplay Scene surface onto the display surface
            self.display_surface.blit(self.gameplay_surface, (0, 0))
        #Else, the program will start the next round with a short intro since Pac-Man ate all the pellets or got caught by a ghost
        else:
            #Debug code
                #print('The outer else statement of the start_round() method is running')
                #print('transition_to_next_round_timer: ' + str(self.transition_to_next_round_timer))
            
            '''
            Sets a timer to pause for a 50 iterations before showcasing all of the obstacles, pellets, 
            and characters when starting the next round
                Note: This is a diffrent type of timer compared to the timer used to change the movement frames
                      of the characters
            '''
            if(self.transition_to_next_round_timer >= 50):
                '''
                A section to set showcase 'READY' text 
                '''

                pixel_font = pygame.font.Font('Fonts/Pixel/DePixelHalbfett.ttf', 18)

                #Displays the "READY!" text throughout the entire theme
                ready_text = pixel_font.render('READY!', True, 'Yellow')
                ready_text_rect = ready_text.get_rect()
                ready_text_rect.center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 35)

                self.gameplay_surface.blit(ready_text, ready_text_rect)

                '''
                A section to set up the obstacles, pellets, and characters
                '''

                #Sets up the obstacles on the Gameplay Scene
                for i in range(len(self.list_blue_obstacles[0])): 
                    self.gameplay_surface.blit(self.list_blue_obstacles[1][i], self.list_blue_obstacles[2][i])
                
                #Sets up the pellets on the Gameplay Scene
                for i in range(len(self.list_pellets[0])):
                    if(self.list_pellets[1][i]):
                        self.gameplay_surface.blit(self.list_pellets[2], self.list_pellets[3][i])

                #Sets up the power pellets on the Gameplay Scene
                for i in range(len(self.list_power_pellets[0])):
                    if(self.list_power_pellets[1][i]):
                        self.gameplay_surface.blit(self.list_power_pellets[2], self.list_power_pellets[3][i])

                #Deducts one life from Pac-Man
                if(self.pac_man_life_deduct):
                    self.pac_man.set_list_of_lives(self.pac_man.get_list_of_lives() - 1)

                    self.pac_man_life_deduct = False

                #Sets Pac-Man's variables back to normal
                self.pac_man.set_direction('Left')
                self.pac_man.set_frame(0)
                self.pac_man.set_CF()
                self.pac_man.set_death_animation_timer(0)
                self.pac_man.frame_update()

                #Resets all ghosts to their default direction
                self.blinky.set_direction('Left')
                self.pinky.set_direction('Down')
                self.inky.set_direction('Up')
                self.clyde.set_direction('Up')

                #Resets the all ghosts' state, frame, and timers back to normal
                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                    ghost.set_frame(0)
                    ghost.set_chase_state(False)
                    ghost.set_scatter_state(True) #The first phase ghosts will be in at the start of each round is Scatter phase
                    ghost.set_frightened_state_v1(False)
                    ghost.set_frightened_state_v2(False)
                    ghost.set_eaten_state(False)
                    ghost.reset_chase_and_scatter_cycle()
                    ghost.set_ghost_scatter_timer(0)
                    ghost.frame_update()
                
                #Resets the position of all characters
                self.pac_man.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 138)
                self.blinky.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 68)
                self.pinky.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 20)
                self.inky.get_rect().center = (self.WINDOW_WIDTH / 2 - 33, self.WINDOW_HEIGHT / 2 - 20)
                self.clyde.get_rect().center = (self.WINDOW_WIDTH / 2 + 33, self.WINDOW_HEIGHT / 2 - 20)

                #Blits the characters onto the Gameplay surface
                self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())

                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                    self.gameplay_surface.blit(ghost.get_image(), ghost.get_rect())

                #A method to showcase list of lives, high score, current score, food images, etc. for the start round
                self.interface_update()

                #Blits the Gameplay Scene surface onto the display surface
                self.display_surface.blit(self.gameplay_surface, (0, 0))

                #After another 200 iterations, the gameplay for the play will resume
                if(self.transition_to_next_round_timer >= 200):
                    #Ensures that the methods in the else statement of the run() method can start
                    self.round_intro = False

                    #Resumes all character movements
                    self.pac_man.set_movement(True)

                    for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:  
                        ghost.set_movement(True)

                    #Resets the timer when Pac-Man goes to the next round
                    self.transition_to_next_round_timer = 0
                else:
                    self.transition_to_next_round_timer += 1
            else:
                    self.transition_to_next_round_timer += 1
            
        #Debug code
            #print(self.fresh_start)

    #A method to end the round based on various events
    def end_round(self):
        #Resets the Gameplay Scene background
        self.gameplay_surface.fill('black')
        
        #An if statement to check if Pac-Man ate all the pellets to move to the next round
        if(self.pac_man.get_ate_all_pellets()):
            #Stops the all relative sound channels
            self.siren_channel.stop()
            self.power_pellet_channel.stop()
            self.pellet_channel.stop()
            
            #Stops Pac-Man from frame change and movement
            self.pac_man.set_movement(False)

            #Stops the ghosts from moving
            for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                ghost.set_movement(False)

            '''
            Sets a timer to pause for a 100 iterations before continuing with the end of the round
                Note: This is a diffrent type of timer compared to the timer used to change the movement frames
                      of the characters
            '''
            if(self.ghost_disappear_timer >= 100):
                #Makes the ghosts disappear
                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                    ghost.get_rect().center = (-100, -100)

                #A switch statement to switch the obstacle colors between blue and white for every 15 iterations
                match self.ghost_disappear_timer:
                    case 115:
                        self.default_obstacles = False
                    case 130:
                        self.default_obstacles = True
                    case 145:
                        self.default_obstacles = False
                    case 160:
                        self.default_obstacles = True
                    case 175:
                        self.default_obstacles = False
                    case 190:
                        self.default_obstacles = True
                    case 205:
                        self.default_obstacles = False
                    case 220:
                        self.default_obstacles = True
                
                #Transitions to the next level
                if(self.ghost_disappear_timer == 235):
                    #Resets variables to start a new round
                    self.round_intro = True
                    self.round_end = False
                    self.level_counter += 1

                    #Resets ghost disappear timer
                    self.ghost_disappear_timer = 0

                    #A for loop to have all eaten pellets visible again
                    for i in range(len(self.list_pellets[0])):
                        #Enables visibility of pellet
                        self.list_pellets[1][i] = True
                    
                    #A for loop to have all eaten power pellets visible again
                    for i in range(len(self.list_power_pellets[0])):
                        #Enables visibility of power pellet
                        self.list_power_pellets[1][i] = True

            '''
            If True, the player sees a black screen when the level resets. Otherwise, changes from previous if statement 
            are applied to the Gameplay Scene
            '''
            if(self.round_intro != True):
                #Displays the original Gameplay Scene
                if(self.ghost_disappear_timer < 100):
                    self.set_up_gameplay_surface()
                #Otherwise, the program alternates the color of the obstacles to blue and white
                else:
                    #Uses the blue obstacles if in a default state
                    if(self.default_obstacles):
                        #Blits blue obstacles on the Gameplay Scene
                        for i in range(len(self.list_blue_obstacles[0])): 
                            #All obstacles are blit on this scene except for the gate image
                            if(i != self.list_blue_obstacles[3]):
                                self.gameplay_surface.blit(self.list_blue_obstacles[1][i], self.list_blue_obstacles[2][i])
                    else:
                        #Blits white obstacles on the Gameplay Scene
                        for i in range(len(self.list_white_obstacles[0])): 
                            self.gameplay_surface.blit(self.list_white_obstacles[1][i], self.list_white_obstacles[2][i])
                    
                    #Blits Pac-Man on the Gameplay Scene
                    self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())

                    #Conducts an interface update
                    self.interface_update()

                #Blits the gameplay surface onto the display surface
                self.display_surface.blit(self.gameplay_surface, (0, 0))

                #Iterates ghost dissapear timer for the previous if statement
                self.ghost_disappear_timer += 1

        #An else-if statement to check if Pac-Man got caught by a ghost but still have lives to continue
        elif(self.pac_man.get_list_of_lives() > 0):            
            #Stops the all relative sound channels
            self.siren_channel.stop()
            self.power_pellet_channel.stop()
            self.pellet_channel.stop()
            
            #Stops Pac-Man from frame change and movement
            self.pac_man.set_movement(False)

            #Stops the ghosts from moving
            for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                ghost.set_movement(False)

            '''
            Sets a timer to pause for a 50 iterations before continuing with the end of the round
                Note: This is a diffrent type of timer compared to the timer used to change the movement frames
                      of the characters
            '''
            if(self.ghost_disappear_timer == 50):
                #Makes the ghosts disappear
                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                    ghost.get_rect().center = (-100, -100)

                #Starts Pac-Man's death animation
                if(self.pac_man_death_sound_is_playing is False):
                    self.end_round_channel.play(self.pac_man_death_sound)
                    self.pac_man_death_sound_is_playing = True

                    #Sets Pac-Man's frame and animation boolean as setup for his death animation
                    self.pac_man.set_frame(0)
                    self.pac_man.set_death_animation(True)

                #Once Pac-Man's death animation stops, character and game variables are reset for the next round
                if(self.end_round_channel.get_busy() is False):
                    #Resets variables back for when Pac-Man gets caught again 
                    self.pac_man.set_death_animation(False)
                    self.pac_man.set_death_animation_timer(0)
                    self.pac_man.set_is_caught(False)
                    self.pac_man_death_sound_is_playing = False
                    self.ghost_disappear_timer = 0

                    #Resets round variables to start a new round
                    self.round_intro = True
                    self.round_end = False
                    self.pac_man_life_deduct = True
            else:
                self.ghost_disappear_timer += 1
            
            #Sets up and blits all objects onto the display surface
            self.set_up_gameplay_surface()
            self.display_surface.blit(self.gameplay_surface, (0, 0))
            
            #Debug code
                #print(self.ghost_disappear_timer)
        #An else statement for when Pac-Man gets caught and has no more lives
        else:
            #Stops the all relative sound channels
            self.siren_channel.stop()
            self.power_pellet_channel.stop()
            self.pellet_channel.stop()
            
            #Stops Pac-Man from frame change and movement
            self.pac_man.set_movement(False)

            #Stops the ghosts from moving
            for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                ghost.set_movement(False)

            '''
            Sets a timer to pause for a 50 iterations before continuing with the end of the round
                Note: This is a diffrent type of timer compared to the timer used to change the movement frames
                      of the characters
            '''
            if(self.ghost_disappear_timer == 50):
                #Makes the ghosts disappear
                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:
                    ghost.get_rect().center = (-100, -100)

                #Starts Pac-Man's death animation
                if(self.pac_man_death_sound_is_playing is False):
                    self.end_round_channel.play(self.pac_man_death_sound)
                    self.pac_man_death_sound_is_playing = True

                    #Sets Pac-Man's frame and animation boolean as setup for his death animation
                    self.pac_man.set_frame(0)
                    self.pac_man.set_death_animation(True)

                #Plays Pac-Man's death animation until the death sound stops
                if(self.end_round_channel.get_busy() is False):
                    #Sets a boolean to have the player transition to the Main Menu Scene
                    self.transition_to_main_menu = True
            else:
                self.ghost_disappear_timer += 1

            '''
            Sets up all objects onto the gameplay surface
                Note: This occurs before the transition_to_main_menu if statement so that the "GAME OVER" 
                      text can overlay the gameplay surface
            '''
            self.set_up_gameplay_surface()

            #Transitions the player to the Main Menu Scene
            if(self.transition_to_main_menu):                
                #Sets a timer to pause for a 100 iterations to showcase the game over text
                if(self.game_over_text_timer != 100):
                    pixel_font = pygame.font.Font('Fonts/Pixel/DePixelHalbfett.ttf', 18)

                    #Displays the "GAME OVER" text
                    game_text = pixel_font.render('GAME', True, 'Red')
                    game_text_rect = game_text.get_rect()
                    game_text_rect.center = (self.WINDOW_WIDTH / 2 - 50, self.WINDOW_HEIGHT / 2 + 35)

                    over_text = pixel_font.render('OVER', True, 'Red')
                    over_text_rect = over_text.get_rect()
                    over_text_rect.center = (self.WINDOW_WIDTH / 2 + 58, self.WINDOW_HEIGHT / 2 + 35)
                    
                    self.gameplay_surface.blit(game_text, game_text_rect)
                    self.gameplay_surface.blit(over_text, over_text_rect)

                    #Blits the 'GAME OVER' text on the Gameplay Scene
                    self.gameplay_surface.blit(game_text, game_text_rect)
                    self.gameplay_surface.blit(over_text, over_text_rect)

                    #Increments the timer
                    self.game_over_text_timer += 1

                    #Debug code
                        #print('Display Game Over Text')
                else:
                    '''
                    Sets an iteration timer to pause for another 50 iterations before continuing from 
                    a black screen to the Main Menu Scene
                    '''
                    if(self.transition_to_main_menu_timer == 50):
                        #Resets variables to start a new round from the Main Menu Scene
                        self.round_intro = True
                        self.fresh_start = True
                        self.round_end = False
                        self.level_counter = 1
                        self.pac_man_life_deduct = True
                        
                        #Resets variables for when Pac-Man gets caught again
                        self.pac_man.set_death_animation(False)
                        self.pac_man.set_death_animation_timer(0)
                        self.pac_man.set_score(0)
                        self.pac_man.set_is_caught(False)
                        self.ghost_disappear_timer = 0
                        self.pac_man_death_sound_is_playing = False

                        #Resets the game over text timer for when Pac-Man loses all of his lives again
                        self.game_over_text_timer = 0

                        #Resets the transition boolean and black screen timer
                        self.transition_to_main_menu = False
                        self.transition_to_main_menu_timer = 0

                        #A for loop to have all eaten pellets visible again
                        for i in range(len(self.list_pellets[0])):
                            #Enables visibility of pellet
                            self.list_pellets[1][i] = True
                        
                        #A for loop to have all eaten power pellets visible again
                        for i in range(len(self.list_power_pellets[0])):
                            #Enables visibility of power pellet
                            self.list_power_pellets[1][i] = True

                        #Loads and plays the Pac-Man Theme Remix when switching to the Main Menu Scene
                        pygame.mixer_music.load('Audio/Music/Pac-Man Theme Remix.wav')
                        pygame.mixer_music.play(-1)

                        #Transitions the player to the Main Menu Scene
                        self.game_state_manager.set_scene_state('Main Menu Scene')
                    else:
                        self.transition_to_main_menu_timer += 1

            #Sets the display surface to black when transitioning from Gameplay Scene to Main Menu Scene
            if(1 <= self.transition_to_main_menu_timer and self.transition_to_main_menu_timer <= 50):
                self.display_surface.fill('black')
            #Else, blits the Gameplay Scene surface onto the display surface
            elif(self.game_state_manager.get_scene_state() != 'Main Menu Scene'):
                self.display_surface.blit(self.gameplay_surface, (0, 0))

    #A method to handle player and game events for the Gameplay Scene
    def event_handler(self, event):
        #Checks if Pac-Man ate all of the pellets
        self.pac_man.check_ate_all_pellets(self.list_pellets, self.list_power_pellets)

        #Checks if Pac-Man is caught by a ghost
        self.pac_man.check_is_caught(self.blinky, self.pinky, self.inky, self.clyde)

        #Checks if Pac-Man ate a ghost (while the ghost was in a frightened state)
        self.pac_man.check_if_ate_a_ghost(self.ghost_eaten_channel, self.pac_man_ate_ghost_sound, self.blinky, self.pinky, self.inky, self.clyde)

        #A method to run gameplay and check a series of conditions
        self.gameplay_sequence(event)
    
    #A method to run gameplay and check a series of conditions for the current round
    def gameplay_sequence(self, event):
        #An if statement to check if Pac-Man ate all of the pellets or is caught by a ghost, which makes the round end
        if(self.pac_man.get_ate_all_pellets() or self.pac_man.get_is_caught()):
            self.round_end = True

            #Stops all relevant channels from playing over the end round channel
            for channel in [self.siren_channel, self.pellet_channel, self.ghost_eaten_channel, self.ghost_return_channel]:
                channel.stop()
        
        #An else-if statement to pause momentarily after Pac-Man eats a ghost (Note: get_ate_a_ghost is [ghost object, boolean])
        elif(self.pac_man.get_ate_a_ghost()[1]):
            #Stops the ghost_return channel (if a ghost has been eaten beforehand)
            if(self.ghost_return_channel.get_busy()):
                self.ghost_return_channel.stop()

            #Grabs the ghost that was caught
            ghost = self.pac_man.get_ate_a_ghost()[0]

            #Momentarily pauses all characters after Pac-Man eats a ghost
            if self.ghost_eaten_channel.get_busy():
                #Debug code
                    # print(str(ghost.get_name()) + " Ghost has been eaten")
                
                self.pac_man.set_movement(False)
                self.blinky.set_movement(False)
                self.pinky.set_movement(False)
                self.inky.set_movement(False)
                self.clyde.set_movement(False)

                self.pac_man.get_image().set_alpha(0)
                ghost.get_image().set_alpha(0)  

                '''
                Showcases the amount of score Pac-Man recieves when he eats a ghost
                '''
                score_streak_image = None
                score_streak_image_rect = None

                match self.pac_man.get_score_streak():
                    case 1: 
                        score_streak_image = pygame.transform.scale(pygame.image.load('Images/Score Streak (# of Ghosts Eaten)/200.png'), (30, 15))
                    case 2:
                        score_streak_image = pygame.transform.scale(pygame.image.load('Images/Score Streak (# of Ghosts Eaten)/400.png'), (30, 15))
                    case 3:
                        score_streak_image = pygame.transform.scale(pygame.image.load('Images/Score Streak (# of Ghosts Eaten)/800.png'), (30, 15))
                    case 4:
                        score_streak_image = pygame.transform.scale(pygame.image.load('Images/Score Streak (# of Ghosts Eaten)/1600.png'), (30, 15))
                
                score_streak_image_rect = score_streak_image.get_rect()
                score_streak_image_rect.center = self.pac_man.get_rect().center

                self.gameplay_surface.blit(score_streak_image, score_streak_image_rect)

            #Resumes all character movements                         
            else:          
                self.pac_man.set_movement(True)

                for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:  
                    ghost.set_movement(True)

                self.pac_man.get_image().set_alpha(1)
                ghost.get_image().set_alpha(1)

                #Resets the score streak after all four ghosts have been eaten in a row (regardless if another Power Pellet was eaten)
                if(self.pac_man.get_score_streak() == 4):
                    self.pac_man.set_score_streak(0)

                #Although the ghost will move to the gate to respawn, Pac-Man is allowed eat another ghost
                self.pac_man.set_ate_a_ghost(None, False)

        #An else statement to resume gameplay as normal
        else:
            #Loops the ghost siren sound effect
            if(self.power_pellet_channel.get_busy()):
                   self.siren_channel.stop()
            else:                
                if(self.siren_channel.get_busy() is False):
                    self.siren_channel.play(self.siren_v1_sound)

                #Resets Pac-Man's score streak (# of ghosts eaten in a row) when the power_pellet_channel ends
                self.pac_man.set_score_streak(0)

            for ghost in [self.blinky, self.pinky, self.inky, self.clyde]:                
                ghost.state_handler(self.siren_channel, self.ghost_return_channel, self.ghost_return, self.power_pellet_channel)
                ghost.movement_update(self.list_blue_obstacles, self.pac_man.get_rect().center)

            # self.blinky.movement_update(self.list_blue_obstacles, self.pac_man.get_rect().center)
            
            self.pac_man.movement_update(event, self.list_blue_obstacles)

            #A method to allow Pac-Man to eat pellets
            self.pac_man.eat_pellets([self.blinky, self.pinky, self.inky, self.clyde],
                                     self.list_pellets, self.list_power_pellets, 
                                     self.pellet_channel, self.power_pellet_channel,
                                     self.pellet_sound, self.power_pellet_sound)