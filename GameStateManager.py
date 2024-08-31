class GameStateManager:
    def __init__(self, state):
        self.state = state
    
    def get_state(self):
        return self.state

    def set_state(self, new_state):
        self.state = new_state