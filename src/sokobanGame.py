from collections import deque

MovimientosPosibles = ['UP', 'DOWN', 'LEFT', 'RIGHT']

class SokobanGame:
        def __init__(self, initial_node, goal_node, board):
            self.initial_node = initial_node
            self.goal_node = goal_node
            self.board = board
            
        def is_goal_node(self, node):
            return node == self.goal_node

        def get_initial_node(self):
            return self.initial_node

        def get_neighbors(self, state):
            # logica para obtener vecins
            pass
        
def reconstruct_path(parent, state):
    # Reconstruct the path from the initial state to the given state
    path = []
    while state is not None:
        path.append(state)
        state = parent[str(state)]
    # Reverse the path to get the correct order
    path.reverse()
    return path

# Define el estado final
def es_estado_final(tablero, tablero_inicial):
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

def count_boxes_not_in_goals(tablero, tablero_inicial):
    count = 0
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 'C' and tablero_inicial[fila][columna] != 'O':
                count += 1
    return count

def get_closest_box_goal_distance(tablero):
    player_pos = getPosActualJugador(tablero)
    closest_box_goal_distance = float('inf')
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == 'O':
                distance = manhattan_distance(player_pos, (fila, columna))
                closest_box_goal_distance = min(closest_box_goal_distance, distance)
    return closest_box_goal_distance