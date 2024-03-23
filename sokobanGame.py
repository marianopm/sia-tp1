class SokobanGame:
        def __init__(self, initial_state, goal_state):
            self.initial_state = initial_state
            self.goal_state = goal_state
            
        def is_goal_state(self, state):
            return state == self.goal_state

        def get_initial_state(self):
            return self.initial_state

        def get_neighbors(self, state):
            # logica para obtener vecins
            pass