'''
Description: The GameStateManager class manages and switches between different game states by tracking keys 
             that correspond to the scene instances in the Main module. Using the list_of_states dictionary,   
             the GameStateManager can dynamically transition between scenes based on specific events in the 
             game
'''
class GameStateManager:
    #A constructor to initialize an instance of GameStateManager
    def __init__(self, state):
        self.state = state
    
    #A method to grab the current state of the game
    def get_state(self):
        return self.state

    #A method to set the current state of the game
    def set_state(self, new_state):
        self.state = new_state