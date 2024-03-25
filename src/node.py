class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.chilfren = []
        
    def __eq__(self, other):
        return self.state == other.state 
    
    def __hash__(self):
        return hash(str(self.state))
    
    def getChildren():
        pass