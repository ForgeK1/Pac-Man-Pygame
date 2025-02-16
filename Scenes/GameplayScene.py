'''
Description: The GameplayScene class helps run the levels of the game. For every level the player passes,
             the high score continues to increase and the ghosts will become more difficult
'''

#Imports pygame and other libraries
import pygame
import os
from Objects.PacMan import PacMan
from Objects.Blinky import Blinky
from Objects.Pinky import Pinky
from Objects.Inky import Inky
from Objects.Clyde import Clyde
from Objects.Pellet import Pellet
from Objects.PowerPellet import PowerPellet

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

        #Initializes the list of obstacles for the game map
        self.list_obstacles = self.load_obstacles()

        #Initializes the character objects
        self.pac_man = PacMan(30, 30, 'Left', self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 138, True, 50)
        self.blinky = Blinky(30, 30, "Left", self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 68, True, 100)
        self.pinky = Pinky(30, 30, "Down", self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 20, True, 100)
        self.inky = Inky(30, 30, "Up", self.WINDOW_WIDTH / 2 - 33, self.WINDOW_HEIGHT / 2 - 20, True, 100)
        self.clyde = Clyde(30, 30, "Up", self.WINDOW_WIDTH / 2 + 33, self.WINDOW_HEIGHT / 2 - 20, True, False, False, 100)

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

        #Initializes music and sound effects
        self.pac_man_death_sound = pygame.mixer.Sound('Audio/Sound Effects/Pac-Man Death.wav')
        self.pellet_sound = pygame.mixer.Sound('Audio/Sound Effects/Waka (Cut Version).wav')
        self.power_pellet_sound = pygame.mixer.Sound('Audio/Sound Effects/Power-Up.wav')
        self.siren_v1_sound = pygame.mixer.Sound('Audio/Sound Effects/Ghost Siren V1.wav')
        self.siren_v2_sound = pygame.mixer.Sound('Audio/Sound Effects/Ghost Siren V2.wav')

        #Initializes variables to check if the player is starting a new round
        self.round_intro = True
        self.fresh_start = True
        self.start_theme = True
        self.pac_man_life_deduct = True
        self.next_round_timer = 0

        #Initializes variables to end the round
        self.ghost_disappear_timer = 0
        self.pac_man_death_sound_has_played = False

    #A method to run the Gameplay Scene
    def run(self, event):
        #print('Round intro: ' + str(self.round_intro))
        #print('Fresh start: ' + str(self.fresh_start))
        
        '''
        An if statement to check if the player is starting a new round, if so the player will
        get an introduction to the round
        '''
        if(self.round_intro):
            self.start_round()
        else:
            #Fills the background of the display surface
            self.display_surface.fill('black')
            
            #A method to check and handle player events for the Gameplay Scene
            self.event_handler(event)

            #A method to set up the updated Gameplay Scene surface
            self.set_up_gameplay_surface()

            #Blits the Gameplay Scene surface onto the display surface
            self.display_surface.blit(self.gameplay_surface, (0, 0))
    
    #A method to setup and blit surface objects onto the Gameplay Scene
    def set_up_gameplay_surface(self):        
        #Resets the Gameplay Scene background
        self.gameplay_surface.fill('black')
        
        #Updates all character animation based on the character_animation_speed variable
        self.pac_man.animation_update()
        self.blinky.animation_update()
        self.pinky.animation_update()
        self.inky.animation_update()
        self.clyde.animation_update()

        #Blits all character images and rects onto the Gameplay Scene
        self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
        self.gameplay_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
        self.gameplay_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
        self.gameplay_surface.blit(self.inky.get_image(), self.inky.get_rect())
        self.gameplay_surface.blit(self.clyde.get_image(), self.clyde.get_rect())
    
        #Blits the obstacles on the Gameplay Scene
        for i in range(len(self.list_obstacles[0])): 
            self.gameplay_surface.blit(self.list_obstacles[1][i], self.list_obstacles[2][i])

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
        
        #A method to showcase high score, list of lives, food images, etc. for the Gameplay Scene
        self.interface_update()
    
    #A method to load and update the Gameplay Scene interface (high score, list of lives, food images, etc.)
    def interface_update(self):
        '''
        A section to set up Pac-Man's current list of lives
        '''
        
        #Grabs Pac-Man's current list of lives
        self.list_of_lives = self.pac_man.get_list_of_lives()
        self.life_image_offset = 40

        #A while loop to blit each life Pac-Man has onto the Gameplay Scene surface
        while self.list_of_lives > 0:
            self.life_image = pygame.transform.scale(pygame.image.load('Images/Pac-Man/Movement/left_frame_1.png'), (40, 40))
            self.life_rect = self.life_image.get_rect()
            self.life_rect.bottomleft = (self.life_image_offset, 633)

            self.gameplay_surface.blit(self.life_image, self.life_rect)

            self.life_image_offset += 45

            self.list_of_lives -= 1
        
        '''
        A section to set up Pac-Man's current high score
        '''

    #A method to load obstacles' coordinates, images, and rects to store each respectivly in their lists
    def load_obstacles(self):
        '''
        First parameter:  [X, Y] coordinates of the image
        Second parameter: Surface object of the image
        Third parameter:  Rect of the image
        '''
        list_obstacles = ([], [], [])

        #A for loop to iterate through all image files in the obstacles folder
        for filename in os.listdir('Images/Obstacles'):
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
            list_obstacles[0].append(coordinates)

            '''
            A section to grab the image and rect of the file
            '''
            image = pygame.image.load('Images/Obstacles/' + filename)
            image_rect = image.get_rect()
            image_rect.topleft = (coordinates[0], coordinates[1])

            #Stores image in the second list and the rect in the third list
            list_obstacles[1].append(image)
            list_obstacles[2].append(image_rect)

        return list_obstacles

    #A method to showcase the start of the round to the player
    def start_round(self):
        #Checks if the player is starting the game for the first time
        if(self.fresh_start == True):
            #Checks if the Pac-Man start theme is still playing. If the theme ends, then the Pac-Man & the ghosts start moving
            if(pygame.mixer_music.get_busy() is False):
                self.round_intro = False
                self.fresh_start = False
                self.start_theme = False
                pygame.mixer_music.unload()
            
            #Resets the Gameplay Scene background
            self.gameplay_surface.fill('black')
            
            #Sets up the obstacles on the Gameplay Scene
            for i in range(len(self.list_obstacles[0])): 
                self.gameplay_surface.blit(self.list_obstacles[1][i], self.list_obstacles[2][i])
            
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

                self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
                self.gameplay_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
                self.gameplay_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
                self.gameplay_surface.blit(self.inky.get_image(), self.inky.get_rect())
                self.gameplay_surface.blit(self.clyde.get_image(), self.clyde.get_rect())

            #A method to showcase high score, list of lives, food images, etc. for the start round
            self.interface_update()

            #Blits the Gameplay Scene surface onto the display surface
            self.display_surface.blit(self.gameplay_surface, (0, 0))
        #Else, the program will start the next round with a short intro since Pac-Man ate all the pellets or got caught by a ghost
        else:
            #Debug code
                #print('The outer else statement of the start_round() method is running')
                #print('next_round_timer: ' + str(self.next_round_timer))
            
            #Resets the display scene background to showcase the black screen for transition
            self.display_surface.fill('black')
            
            '''
            Sets a timer to pause for a 50 iterations before showcasing all of the obstacles, pellets, 
            and characters when starting the next round
                Note: This is a diffrent type of timer compared to the timer used to change the movement frames
                      of the characters
            '''
            if(self.next_round_timer >= 50):
                #Resets the Gameplay Scene background
                self.gameplay_surface.fill('black')
                
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
                A section to set up the obstacles, pellets, and obstacles
                '''

                #Sets up the obstacles on the Gameplay Scene
                for i in range(len(self.list_obstacles[0])): 
                    self.gameplay_surface.blit(self.list_obstacles[1][i], self.list_obstacles[2][i])
                
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
                self.pac_man.set_death_animation(False)
                self.pac_man.set_death_animation_timer(0)

                #Resets the positions of all characters
                self.pac_man.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 + 138)
                self.blinky.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 68)
                self.pinky.get_rect().center = (self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 2 - 20)
                self.inky.get_rect().center = (self.WINDOW_WIDTH / 2 - 33, self.WINDOW_HEIGHT / 2 - 20)
                self.clyde.get_rect().center = (self.WINDOW_WIDTH / 2 + 33, self.WINDOW_HEIGHT / 2 - 20)

                #Blits the characters onto the gameplay surface
                self.gameplay_surface.blit(self.pac_man.get_image(), self.pac_man.get_rect())
                self.gameplay_surface.blit(self.blinky.get_image(), self.blinky.get_rect())
                self.gameplay_surface.blit(self.pinky.get_image(), self.pinky.get_rect())
                self.gameplay_surface.blit(self.inky.get_image(), self.inky.get_rect())
                self.gameplay_surface.blit(self.clyde.get_image(), self.clyde.get_rect())

                #A method to showcase high score, list of lives, food images, etc. for the start round
                self.interface_update()

                #Blits the Gameplay Scene surface onto the display surface
                self.display_surface.blit(self.gameplay_surface, (0, 0))

                #After another 150 iterations, the gameplay for the play will resume
                if(self.next_round_timer == 200):
                    #Ensures that the methods in the else statement of the run() method can start
                    self.round_intro = False

                    #Resets the timer when Pac-Man goes to the next round
                    self.next_round_timer = 0
                else:
                    self.next_round_timer += 1
            else:
                    self.next_round_timer += 1
                
    #A method to end the round based on various events
    def end_round(self):
        #An if statement to check if Pac-Man ate all the pellets to move to the next round


        #An if statement to check if Pac-Man got caught by a ghost but still have lives to continue
        if(self.pac_man.get_list_of_lives() > 0):
            #Stops the all relative sound channels
            self.siren_channel.stop()
            self.power_pellet_channel.stop()
            self.pellet_channel.stop()
            
            #Stops Pac-Man from frame change and movement
            self.pac_man.set_movement(False)

            #Stops the ghosts from moving
            self.blinky.set_movement(False)
            self.pinky.set_movement(False)
            self.inky.set_movement(False)
            self.clyde.set_movement(False)

            '''
            Sets a timer to pause for a 50 iterations before continuing with the end of the round
                Note: This is a diffrent type of timer compared to the timer used to change the movement frames
                      of the characters
            '''
            if(self.ghost_disappear_timer == 50):
                #Makes the ghosts disappear
                self.blinky.get_rect().center = (-100, -100)
                self.pinky.get_rect().center = (-100, -100)
                self.inky.get_rect().center = (-100, -100)
                self.clyde.get_rect().center = (-100, -100)

                #Starts Pac-Man's death animation
                if(self.pac_man_death_sound_has_played is False):
                    self.end_round_channel.play(self.pac_man_death_sound)
                    self.pac_man_death_sound_has_played = True

                    #Sets Pac-Man's frame and animation boolean as setup for his death animation
                    self.pac_man.set_frame(0)
                    self.pac_man.set_death_animation(True)
                    #self.pac_man.set_character_animation_speed(10)

                #Plays Pac-Man's death animation until the death sound stops
                if(self.end_round_channel.get_busy() is False):
                    #Sets up variables to start a new round
                    self.round_intro = True
                    self.pac_man_life_deduct = True
                    self.pac_man.set_is_caught(False)

                    #Sets ghost disappear timer & death sound boolean when Pac-Man gets caught again
                    self.ghost_disappear_timer = 0
                    self.pac_man_death_sound_has_played = False
            else:
                self.ghost_disappear_timer += 1
            
            #Debug code
                #print(self.ghost_disappear_timer)

        #An if statement to check if Pac-Man got caught and has no more lives
        

        #Debug code
            #print('The end_round() method is running')

    #A method to check and handle events for the Gameplay Scene
    def event_handler(self, event):
        '''
        A section to handle player events for Pac-Man
        '''

        #Checks if a ghost has caught Pac-Man
        if(self.blinky.get_rect().colliderect(self.pac_man.get_rect()) or 
                                              self.pinky.get_rect().colliderect(self.pac_man.get_rect()) or 
                                              self.inky.get_rect().colliderect(self.pac_man.get_rect()) or 
                                              self.clyde.get_rect().colliderect(self.pac_man.get_rect())):
            self.pac_man.set_is_caught(True)

        #If Pac-Man is caught or eats all of the pellets the round ends. Else, Pac-Man's movement continues to get updated
        if(self.pac_man.get_is_caught() is True):
            self.end_round()
        else:
            self.pac_man.movement_update(event, self.list_obstacles)
            self.blinky.set_movement(True)
            self.pinky.set_movement(True)
            self.inky.set_movement(True)
            self.clyde.set_movement(True)

            #A method to allow Pac-Man to eat pellets
            self.pac_man.eat_pellets(self.list_pellets, self.list_power_pellets, 
                                    self.pellet_channel, self.power_pellet_channel,
                                    self.pellet_sound, self.power_pellet_sound)

            #Checks if Pac-Man ate a power pellet. If so, the ghosts will scatter
            self.ghosts_scatter_timer()
        
    #A method for ghosts to scatter
    def ghosts_scatter_timer(self):
        if(self.pac_man.get_eat_ghosts() is True and self.pac_man.get_is_caught() is False):
            self.siren_channel.stop()

            #Checks if the power pellet sound effect is still going on
            if(self.power_pellet_channel.get_busy() is True):
                self.clyde.set_vulnerable_state(True)
            else:
                self.clyde.set_vulnerable_state(False)

                self.pac_man.set_eat_ghosts(False)
        #Else, the ghosts will continue to chase Pac-Man
        elif(self.pac_man.get_eat_ghosts() is False and self.pac_man.get_is_caught() is False):
            #Loops the siren sound effect
            if(self.siren_channel.get_busy() is False):
                self.siren_channel.play(self.siren_v1_sound)