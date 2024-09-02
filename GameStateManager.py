'''
Description: The GameStateManager class manages and switches between different game states by tracking keys 
             that correspond to the scene instances in the Main module. Using the list_of_states dictionary,   
             the GameStateManager can dynamically transition between scenes based on specific events in the 
             game
'''
class GameStateManager:
    def __init__(self, state):
        self.state = state
    
    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state