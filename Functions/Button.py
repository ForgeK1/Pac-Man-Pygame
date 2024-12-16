'''
Description: This class contains methods for creating an interactable button
'''

#Imports pygame libraries
import pygame

class Button:
    #A constructor to create an instance of a Button
    def __init__(self, not_highlighted_file_path, highlighted_file_path, pressed_image_file_path, 
                 text_input, non_hover_text_color, hover_text_color, pressed_text_color, 
                 font_path, font_size):
        #Sets up parameter variables
        self.non_hover_image_file_path = not_highlighted_file_path
        self.hover_image_file_path = highlighted_file_path
        self.pressed_image_file_path = pressed_image_file_path

        self.text_input = text_input
        self.non_hover_text_color = non_hover_text_color
        self.hover_text_color = hover_text_color
        self.pressed_text_color = pressed_text_color
        self.font_path = font_path
        self.font_size = font_size

        #Sets up the image and image rect
        self.image = pygame.image.load(self.non_hover_image_file_path)
        self.image_rect = self.image.get_rect()

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
        return self.image_rect
    
    #A method to return the text's Font from the button
    def get_text_font(self):
        return self.font
    
    #A method to set a new text Font for the button
    def set_text_font(self, new_font_path, new_font_size):
        self.font_path = new_font_path
        self.font_size = new_font_size

        #Updates text after change
        self.update_text()
    
    #A method to return the button's text
    def get_text(self):
        return self.text

    #A method to set a new text for the button
    def set_text(self, new_text):
        self.text = new_text

        #Updates text after change
        self.update_text()

    #A method to return the rect of button's text
    def get_text_rect(self):
        return self.text_rect

    #A method to scale the button using a tuple size (width, length)
    def scale_button(self, image_width, image_length, text_size):
        #Scales the image
        self.image = pygame.transform.scale(self.get_image(), (image_width, image_length))
        self.image_rect = self.get_image().get_rect()

        #Scales the text
        self.font_size = text_size
        self.update_text()
    
    #A method to update text after a change has been applied
    def update_text(self):
        self.font = pygame.font.Font(self.font_path, self.font_size)
        self.text = self.font.render(self.text_input, True, self.non_hover_text_color)
        self.text_rect = self.text.get_rect()

    '''
    A method to check player's input
        Returns True if the player has fully clicked and let go of the button
        Returns False if otherwise
    '''
    def check_input(self, mouse_pos, mouse_click, mouse_let_go): 
        #Checks if the player pressing down the button
        if(mouse_pos[0] in range(self.image_rect.left, self.image_rect.right) and
           mouse_pos[1] in range(self.image_rect.top, self.image_rect.bottom) and
           mouse_click == True and mouse_let_go == False):
            self.image = pygame.image.load(self.pressed_image_file_path)
            self.image_rect = self.image.get_rect()

            self.text = self.font.render(self.text_input, True, self.pressed_text_color)
            self.text_rect = self.text.get_rect()

            #Debug code
                #print("First statement ran")
        #Checks if the player let go of clicking the button after pressing it
        elif(mouse_pos[0] in range(self.image_rect.left, self.image_rect.right) and
             mouse_pos[1] in range(self.image_rect.top, self.image_rect.bottom) and
             mouse_click == False and mouse_let_go == True):
            self.image = pygame.image.load(self.non_hover_image_file_path)
            self.image_rect = self.image.get_rect()

            self.text = self.font.render(self.text_input, True, self.non_hover_text_color)
            self.text_rect = self.text.get_rect()

            #Debug code
                #print("Second statement ran")

            return True
        #Checks if the player is hovering over the button
        elif(mouse_pos[0] in range(self.image_rect.left, self.image_rect.right) and
             mouse_pos[1] in range(self.image_rect.top, self.image_rect.bottom) and
             mouse_click == False and mouse_let_go == False):
            self.image = pygame.image.load(self.hover_image_file_path)
            self.image_rect = self.image.get_rect()

            self.text = self.font.render(self.text_input, True, self.hover_text_color)
            self.text_rect = self.text.get_rect()

            #Debug code
                #print("Third statement ran")
        #Converts button to its normal state if the player is not hovering and/or pressing the button
        else:
            self.image = pygame.image.load(self.non_hover_image_file_path)
            self.image_rect = self.image.get_rect()

            self.text = self.font.render(self.text_input, True, self.non_hover_text_color)
            self.text_rect = self.text.get_rect()

            #Debug code
                #print("Fourth statement ran")
        
        return False