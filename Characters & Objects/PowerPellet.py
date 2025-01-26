'''
Description: This class contains methods for animations for a PowerPellet object
'''

class PowerPellet:
    #A constuctor to initialize an instance of a PowerPellet
    def __init__(self, image, rect, power_pellet_animation_speed):
        #Variables to keep track of the image and rect
        self.image = image
        self.rect = rect

        #Variables to control character animation speed
        self.power_pellet_animation_speed = power_pellet_animation_speed #In miliseconds
        self.last_updated_time = 0 #In miliseconds
    
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
    
    #