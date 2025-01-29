'''
Description: This class contains methods for animations for a PowerPellet object
'''

#Imports pygame modules and other libraries
import pygame
import csv

class PowerPellet:
    #A constuctor to initialize an instance of a PowerPellet
    def __init__(self, power_pellet_animation_speed):
        #Variables to keep track of the image and rect
        self.image = pygame.transform.scale(pygame.image.load('Images/Pellets/power_pellet_frame_0.png'), (16, 16))
        self.rect = self.image.get_rect()

        #Variables to control power pellet's animation speed
        self.power_pellet_animation_speed = power_pellet_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds
        self.state = 0
    
    #A method to return the PowerPellet's image
    def get_image(self):
        return self.image
    
    #A method to set PowerPellet's image
    def set_image(self, new_image):
        self.image = new_image
    
    #A method to get PowerPellet's rect
    def get_rect(self):
        return self.rect
    
    #A method to set PowerPellet's rect
    def set_rect(self, new_rect):
        self.rect = new_rect
    
    #A method to return a list of power pellets' coordinates, hidden boolean, images, and rects
    def load_power_pellets(self):
        '''
        First parameter:  [X, Y] coordinates of the image
        Second parameter: Boolean of whether the pellet should be hidden or shown on the map
        Third parameter:  Surface object of the image
        Fourth parameter: Rect of the image

            Note: The reason why this variable is a list of lists instead of a tuple of lists (Ex. list_obstacles or list_pellets
                  in the Gameplay Scene class) is because the program uses the animation_update() method to assign a new image 
                  in the third index of this list. A tuple is immutable and cannot be assigned a new object if already assigned
        '''
        list_power_pellets = [[], [], self.image, []]

        #Opens the power pellets CSV file 
        with open('Images/Pellets/power_pellets_coordinates.csv') as fileObject:
            #next() is used so that we skip the header row Ex) ['X', 'Y', 'Hidden']
            next(fileObject)
            
            #Creates a reader object by passing in the file
            reader = csv.reader(fileObject)

            #A for loop to iterate through each row
            for row in reader:
                '''
                A section to grab and record the coordinates in the first list
                '''
                coordinates = [int(row[0]), int(row[1])]
                list_power_pellets[0].append(coordinates)

                '''
                A section to grab and record the boolean in the second list
                '''
                list_power_pellets[1].append(row[2])

                '''
                A section to grab and record the updated rect position in the fourth list
                    Note: Since all power pellets share the same image, the value has already been assigned in the third parameter
                '''
                power_pellet_image_rect = self.image.get_rect()
                power_pellet_image_rect.topleft = coordinates
                list_power_pellets[3].append(power_pellet_image_rect)

                #Debug code
                    #print(row)
            
            return list_power_pellets
    
    #A method to update the animation of a power pellet that is present on the map by returning an image object
    def animation_update(self, image):
        #Gets the current time in miliseconds
        curr_time = pygame.time.get_ticks()
        
        #A variable to keep track of when to make the power pellet dissapear
        change_frame = False

        '''
        Updates the animation frame of the power pellet if enough time has passed
        Ex) 0 - 0 > 200     False
            100 - 0 > 200   False
            201 - 0 > 200   True  --> 
            201 - 201 > 200 False
            ...
            402 - 201 > 200 True -->
            402 - 402 > 200 
            ... and so on
        '''
        if curr_time - self.last_updated_time > self.power_pellet_animation_speed: 
            #Sets change frame to True 
            change_frame = True

            #Sets up a new time
            self.last_updated_time = curr_time

        '''
        If the first and second case is True, then the program updates the image object of the power pellet. 
        If both cases don't pass, the program uses the image object in runtime
        '''
        if(change_frame and self.state == 0):
            #Debug code
                #print('State 1 ran\n')

            self.state = 1
            
            return pygame.transform.scale(pygame.image.load('Images/Pellets/power_pellet_frame_0.png'), (16, 16))
        elif(change_frame and self.state == 1):
            #Debug code
                #print('State 2 ran\n')

            self.state = 0

            return pygame.transform.scale(pygame.image.load('Images/Pellets/power_pellet_frame_1.png'), (16, 16))
        else:
            #Debug code
                #print('State 3 ran\n')

            return image