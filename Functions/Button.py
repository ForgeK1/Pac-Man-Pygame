'''
Description: This class contains methods for creating an interactable button
'''

#Imports pygame libraries
import pygame

class Button:
    #A constructor to create an instance of a Button
    def __init__(self, not_highlighted_file_path, highlighted_file_path, pressed_file_path, text_input, non_hover_text_color, hover_text_color, font_path, font_size):
        #Sets up parameter variables
        self.non_hover_image_file_path = not_highlighted_file_path
        self.hover_image_file_path = highlighted_file_path
        self.pressed_file_path = pressed_file_path
        self.text_input = text_input
        self.non_hover_text_color = non_hover_text_color
        self.hover_text_color = hover_text_color
        self.font_path = font_path
        self.font_size = font_size

        #Sets up the image and image rect
        self.image = pygame.image.load(self.non_hover_image_file_path)
        self.image.get_rect()

        #Sets up the font, text, and text rect
        self.font = pygame.font.Font(self.font_path, self.font_size)
        self.text = self.font.render(self.text_input, True, self.non_hover_text_color)
        self.text_rect = self.text.get_rect()
    
    #A method to return the button's image
    def get_image(self):
        return self.image

    #A method to set a new image for the button
    def set_image(self, new_image):
        self.image = new_image

    #A method to return the rect of button's image
    def get_image_rect(self):
        return self.rect
    
    #A method to set a new rect for button's image
    def set_image_rect(self, new_rect):
        self.rect = new_rect
    
    #A method to return the button's text
    def get_text(self):
        return self.text

    #A method to set a new text for the button
    def set_text(self, new_text):
        self.text = new_text

    #A method to return the rect of button's text
    def get_text_rect(self):
        return self.text_rect
    
    #A method to set a new rect for button's text
    def set_text_rect(self, new_text_rect):
        self.text_rect = new_text_rect

        