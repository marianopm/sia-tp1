import time
from collections import deque
from .sokobanGame import es_estado_final, generate_next_states, reconstruct_path

class DFS:
    def search(game):
        # Implementa el algoritmo DFS
        
        # Inicializa la pila con el estado inicial
        stack = [game.board]
        # Inicializa un conjunto vacío para realizar un seguimiento de los estados visitados
        visited = set()
        # Inicializa un diccionario para realizar un seguimiento del camino hacia cada estado
        parent = {str(game.board): None}
        expanded_nodes = 0  # Contador de nodos expandidos
        frontier_nodes = 1  # Contador de nodos en la frontera (el estado inicial está en la frontera)

        # Continúa la búsqueda hasta que la pila esté vacía
        while stack:
            # Obtiene el primer estado de la pila
            current_state = stack.pop()
            # Incrementa el contador de nodos expandidos
            expanded_nodes += 1

            # Comprueba si el estado actual es el estado objetivo
            if es_estado_final(current_state, game.board):
                # Devuelve el camino hacia el estado objetivo junto con las estadísticas
                return reconstruct_path(parent, current_state), expanded_nodes, frontier_nodes

            # Marca el estado actual como visitado
            visited.add(str(current_state))

            # Genera todos los posibles estados siguientes
            for next_state in generate_next_states(current_state):
                # Comprueba si el siguiente estado no ha sido visitado
                if str(next_state) not in visited:
                    # Agrega el siguiente estado a la pila
                    stack.append(next_state)
                    # Incrementa el contador de nodos en la frontera
                    frontier_nodes += 1
                    # Registra el camino hacia el siguiente estado
                    parent[str(next_state)] = current_state
        
        # Si no se encuentra ninguna solución, devuelve None junto con las estadísticas
        return None, expanded_nodes, frontier_nodes
