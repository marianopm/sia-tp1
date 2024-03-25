from collections import deque

# Definición del tablero y constantes
tablero_inicial = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', 'J', 'O', 'C', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]

MovimientosPosibles = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Define el estado final
def es_estado_final(tablero):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 'C':
                # Si una caja no está sobre un objetivo, el estado no es final
                if tablero_inicial[fila][columna] != 'O':
                    return False
    return True

# Funcion para obtener la posicion actual del jugador
def getPosActualJugador(tablero):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 'J':
                return (fila, columna)
                
def moverJugador(tablero, nuevoTablero, posJugadorFutura, posActualJugador, action):     
    if posJugadorFutura is not None and nuevoTablero[posJugadorFutura[0]][posJugadorFutura[1]] != '#':
        # Movemos el jugador a la nueva posicion si no hay nada
        if nuevoTablero[posJugadorFutura[0]][posJugadorFutura[1]] == ' ':
            nuevoTablero[posJugadorFutura[0]][posJugadorFutura[1]] = 'J'
            nuevoTablero[posActualJugador[0]][posActualJugador[1]] = ' '
            
        # Si la posicion futura es un objetivo, guardamos la posicion del objetivo y movemos jugador
#        elif nuevoTablero[posJugadorFutura[0]][posJugadorFutura[1]] == 'O':
#            nuevoTablero[posJugadorFutura[0]][posJugadorFutura[1]] = 'J'
#            nuevoTablero[posActualJugador[0]][posActualJugador[1]] = ' '
            
        # Si hay una caja en la posicion futura
        elif nuevoTablero[posJugadorFutura[0]][posJugadorFutura[1]] == 'C':
            posCajaFutura = None 
            if action == 'UP':
                posCajaFutura = (posJugadorFutura[0] -1 , posJugadorFutura[1])
            elif action == 'DOWN':
                posCajaFutura = (posJugadorFutura[0] + 1 , posJugadorFutura[1])
            elif action == 'LEFT':
                posCajaFutura = (posJugadorFutura[0], posJugadorFutura[1] - 1)
            elif action == 'RIGHT':
                posCajaFutura = (posJugadorFutura[0], posJugadorFutura[1] + 1)
            #Verificamos si se puede empujar
            if tablero[posCajaFutura[0]][posCajaFutura[1]] != 'C' and tablero[posCajaFutura[0]][posCajaFutura[1]] != '#':
                nuevoTablero[posCajaFutura[0]][posCajaFutura[1]] = 'C'
                nuevoTablero[posJugadorFutura[0]][posJugadorFutura[1]] = 'J'
                nuevoTablero[posActualJugador[0]][posActualJugador[1]] = ' '
    return nuevoTablero
    
# define action function
def mainMovimiento(tablero, action):
    nuevoTablero = [row[:] for row in tablero]

    # Obtenemos la posicion del jugador
    posActualJugador = getPosActualJugador(tablero)

    # en funcion del movimiento elegido se mueve el jugador
    posJugadorFutura = None
    if action == 'UP':
        posJugadorFutura = (posActualJugador[0] - 1, posActualJugador[1])
    elif action == 'DOWN':
        posJugadorFutura = (posActualJugador[0] + 1, posActualJugador[1])
    elif action == 'LEFT':
        posJugadorFutura = (posActualJugador[0], posActualJugador[1] - 1)
    elif action == 'RIGHT':
        posJugadorFutura = (posActualJugador[0], posActualJugador[1] + 1)

    # devuelve el tablero
    if posJugadorFutura is not None and nuevoTablero[posJugadorFutura[0]][posJugadorFutura[1]] != '#':
        nuevoTablero = moverJugador(tablero, nuevoTablero, posJugadorFutura, posActualJugador, action)

    return nuevoTablero

def generate_next_states(state):
    next_states = []
    for action in MovimientosPosibles:
        nuevoTablero = mainMovimiento(state, action)
        if nuevoTablero not in next_states:
            next_states.append(nuevoTablero)
    return next_states

# Define la función de búsqueda en profundidad (DFS)
def dfs_solve(initial_state):
    # Inicializa la pila con el estado inicial
    stack = [initial_state]
    # Inicializa un conjunto vacío para realizar un seguimiento de los estados visitados
    visited = set()
    # Inicializa un diccionario para realizar un seguimiento del camino hacia cada estado
    parent = {str(initial_state): None}
    expanded_nodes = 0  # Contador de nodos expandidos
    frontier_nodes = 1  # Contador de nodos en la frontera (el estado inicial está en la frontera)

    # Continúa la búsqueda hasta que la pila esté vacía
    while stack:
        # Obtiene el primer estado de la pila
        current_state = stack.pop()
        # Incrementa el contador de nodos expandidos
        expanded_nodes += 1

        # Comprueba si el estado actual es el estado objetivo
        if es_estado_final(current_state):
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

def bfs_solve(tablero_inicial):
    # Initialize the frontier with the initial state
    frontier = [tablero_inicial]
    # Initialize an empty set to keep track of visited states
    visited = set()
    # Initialize a dictionary to keep track of the path to each state
    parent = {str(tablero_inicial): None}
    expanded_nodes = 0  # Counter for expanded nodes
    frontier_nodes = 1  # Counter for nodes in the frontier (initial state is in the frontier)

    # Continue searching until the frontier is empty
    while frontier:
        # Pop the first state from the frontier
        current_state = frontier.pop(0)
        # Increment the count of expanded nodes
        expanded_nodes += 1

        # Check if the current state is the goal state
        if es_estado_final(current_state):
            # Return the path to the goal state along with statistics
            return reconstruct_path(parent, current_state), expanded_nodes, frontier_nodes
        
        # Mark the current state as visited
        visited.add(str(current_state))

        # Generate all possible next states
        for next_state in generate_next_states(current_state):
            # Check if the next state has not been visited
            if str(next_state) not in visited:
                # Add the next state to the frontier
                frontier.append(next_state)
                # Increment the count of frontier nodes
                frontier_nodes += 1
                # Record the path to the next state
                parent[str(next_state)] = current_state

    # If no solution is found, return None along with statistics
    return None, expanded_nodes, frontier_nodes

def reconstruct_path(parent, state):
    # Reconstruct the path from the initial state to the given state
    path = []
    while state is not None:
        path.append(state)
        state = parent[str(state)]
    # Reverse the path to get the correct order
    path.reverse()
    return path


# Función principal para resolver el juego con BFS o DFS
def mainGame(tablero_inicial, metodo='bfs'):
    if metodo == 'bfs':
        return bfs_solve(tablero_inicial)
    elif metodo == 'dfs':
        return dfs_solve(tablero_inicial)
    else:
        raise ValueError("Método de búsqueda no válido. Por favor, elija 'bfs' o 'dfs'.")
        
metodo = 'dfs'  # Cambiar a 'dfs' si se prefiere la búsqueda en profundidad
solution, expanded_nodes, frontier_nodes = mainGame(tablero_inicial, metodo)

if solution:
        print("Exito!")
        print(f"Total number of steps: {len(solution) - 1}")
        print(f"Expanded nodes: {expanded_nodes}")
        print(f"Frontier nodes: {frontier_nodes}")
        # print the board state of each step
for i in range(len(solution) - 1):
    # Encuentra la acción que llevó al estado actual desde el estado anterior
    current_state = solution[i]
    next_state = solution[i+1]
    action = None
    # Encuentra la diferencia entre los dos estados para determinar la acción
    for row in range(len(current_state)):
        for col in range(len(current_state[row])):
            if current_state[row][col] != next_state[row][col]:
                if row < len(current_state) and current_state[row+1][col] == 'J':
                    action = 'UP'
                elif row > 0 and current_state[row-1][col] == 'J':
                    action = 'DOWN'
                elif col < len(current_state[row]) and current_state[row][col+1] == 'J':
                    action = 'LEFT'
                elif col > 0 and current_state[row][col-1] == 'J':
                    action = 'RIGHT'
    print(f"Paso {i+1}) {action}")

else:
    print("Fracaso")
    
    
def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_closest_box_goal_distance(tablero):
    player_pos = getPosActualJugador(tablero)
    closest_box_goal_distance = float('inf')
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 'O':
                distance = manhattan_distance(player_pos, (fila, columna))
                closest_box_goal_distance = min(closest_box_goal_distance, distance)
    return closest_box_goal_distance

def astar_solve(tablero_inicial):
    # Initialize the frontier with the initial state
    frontier = [(tablero_inicial, 0)]  # (state, g)
    # Initialize an empty set to keep track of visited states
    visited = set()
    # Initialize a dictionary to keep track of the path to each state
    parent = {str(tablero_inicial): None}
    expanded_nodes = 0  # Counter for expanded nodes
    frontier_nodes = 1  # Counter for nodes in the frontier (initial state is in the frontier)

    # Continue searching until the frontier is empty
    while frontier:
        # Pop the state with the minimum f value from the frontier
        current_state, current_g = min(frontier, key=lambda x: x[1])
        frontier.remove((current_state, current_g))
        # Increment the count of expanded nodes
        expanded_nodes += 1

        # Check if the current state is the goal state
        if es_estado_final(current_state):
            # Return the path to the goal state along with statistics
            return reconstruct_path(parent, current_state), expanded_nodes, frontier_nodes
        
        # Mark the current state as visited
        visited.add(str(current_state))

        # Generate all possible next states
        for next_state in generate_next_states(current_state):
            # Calculate g value for the next state
            next_g = current_g + 1
            # Calculate h value (Manhattan distance between player and closest box goal)
            h = get_closest_box_goal_distance(next_state)
            # Calculate f value
            f = next_g + h

            # Check if the next state has not been visited
            if str(next_state) not in visited:
                # Add the next state to the frontier
                frontier.append((next_state, f))
                # Increment the count of frontier nodes
                frontier_nodes += 1
                # Record the path to the next state
                parent[str(next_state)] = current_state

    # If no solution is found, return None along with statistics
    return None, expanded_nodes, frontier_nodes