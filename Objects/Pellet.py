'''
Description: This class contains methods for animations for a Pellet object
'''

#Imports pygame modules and other libraries
import pygame
import csv

class Pellet:
    #A constuctor to initialize an instance of a Pellet
    def __init__(self, image):
        #Variables to keep track of the image and rect
        self.image = pygame.image.load(image) 
        self.rect = self.image.get_rect()
    
    #A method to return the Pellet's image
    def get_image(self):
        return self.image
    
    #A method to set Pellet's image
    def set_image(self, new_image):
        self.image = new_image
    
    #A method to get Pellet's rect
    def get_rect(self):
        return self.rect
    
    #A method to set Pellet's rect
    def set_rect(self, new_rect):
        self.rect = new_rect
        
    #A method to return a list of pellets' coordinates, hidden boolean, images, and rects
    def load_pellets(self):
        pellet_image = pygame.transform.scale(pygame.image.load('Images/Pellets/pellet.png'), (4, 4)) 

        '''
        First parameter:  [X, Y] coordinates of the image
        Second parameter: Boolean of whether the pellet should be hidden or shown on the map
        Third parameter:  Surface object of the image
        Fourth parameter: Rect of the image
        '''
        list_pellets = ([], [], pellet_image, [])
        
        #Opens the power pellets CSV file 
        with open('Images/Pellets/pellets_coordinates.csv') as fileObject:
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
                list_pellets[0].append(coordinates)

                '''
                A section to grab and record the boolean in the second list
                '''
                list_pellets[1].append(row[2])

                '''
                A section to grab and record the updated rect position in the fourth list
                    Note: Since all pellets share the same image, the value has already been assigned in the third parameter
                '''
                pellet_image_rect = pellet_image.get_rect()
                pellet_image_rect.topleft = coordinates
                list_pellets[3].append(pellet_image_rect)

                #Debug code
                    #print(row)
        
        return list_pellets