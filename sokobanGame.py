class SokobanGame:
        def __init__(self, initial_state, goal_state, board):
            self.initial_state = initial_state
            self.goal_state = goal_state
            self.board = board
            
        def is_goal_state(self, state):
            return state == self.goal_state

        def get_initial_state(self):
            return self.initial_state

        def get_neighbors(self, state):
            # logica para obtener vecins
            pass
        
        def trace_back(node, solution_path):
            while node.parent is not None:
                solution_path.append(node.state)  # Agrega el estado del nodo al camino
                node = node.parent  # Se mueve al nodo padre

            solution_path.append(node.state)  # Agrega el estado del nodo inicial al camino
            return solution_path