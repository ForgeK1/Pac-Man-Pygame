'''
Description: The GameStateManager class manages and switches between different game states by tracking keys 
             that correspond to the scene instances in the Game module. Using the list_of_states dictionary,   
             the GameStateManager can dynamically transition between scenes based on specific events in the 
             game

             Note that, the game loop depends on what Boolean value "running_state" is for ensuring that the 
             game is still running  and the running state is not tied to a specific sceneW
'''
class GameStateManager:
    #A constructor to initialize an instance of GameStateManager
    def __init__(self, scene_state, running_state):
        self.scene_state = scene_state
        self.running_state = running_state
        self.clock_delta_time = None
    
    #A method to grab the current scene_state of the game
    def get_scene_state(self):
        return self.scene_state

    #A method to set the current scene_state of the game
    def set_scene_state(self, new_scene_state):
        self.scene_state = new_scene_state

    #A method to grab the current running_state of the game
    def get_running_state(self):
        return self.running_state

    #A method to set the current running_state of the game
    def set_running_state(self, new_running_state):
        self.running_state = new_running_state

    #A method to set the delta time variable created from the clock when ticking 60 fps in the main game loop
    def set_clock_delta_time(self, delta_time):
        self.clock_delta_time = delta_time

    #A method to get the delta time variable
    def get_clock_delta_time(self):
        return self.clock_delta_time