import time
from collections import deque
from sokobanGame import trace_back

class DFS:
    def search(game):
        # Inicia el cronometro
        start = time.time()
        
        # Implementa el algoritmo DFS
        total_steps = 0
        nodes_expanded = 0
        frontier_nodes = 0
        
        visited = set()
        solution_path = []
        solved = False
        initial_node = game.initial_node
        goal_node = game.goal_node
        queue = deque([initial_node])
        
        ## Busca hasta que solved sea tru o que la cola este vacia (no hay mas nodos que explorar)
        while not solved and queue:
            current_node = queue.popleft()
            if current_node == goal_node:
                solution_path = trace_back(current_node, solution_path)
                solved = True
            else:
                if current_node not in visited:
                    visited.add(current_node)

                children = current_node.get_children(game.board)
                for child in children:
                    queue.append(child)

        solution_path.reverse()
        
        
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        
        print("DFS: Tiempo de ejecución", total_time, "segundos") 
        print("DFS: Numero de pasos:", total_steps)
        print("DFS: Numero de nodos expandidos:", nodes_expanded) 
        print("DFS: Numero de nodos frontera:", frontier_nodes) 
        
        return solution_path, visited