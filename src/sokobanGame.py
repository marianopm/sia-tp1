from collections import deque

MovimientosPosibles = ['UP', 'DOWN', 'LEFT', 'RIGHT']

class SokobanGame:
        def __init__(self, board):
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
def is_final_state(actual_board, initial_board):
    for row in range(len(actual_board)):
        for column in range(len(actual_board[row])):
            if actual_board[row][column] == 'C':
                # Si una caja no está sobre un objetivo, el estado no es final
                if initial_board[row][column] != 'O':
                    return False
    return True

# Funcion para obtener la posicion actual del jugador
def get_actual_position(actual_board):
    for row in range(len(actual_board)):
        for column in range(len(actual_board[row])):
            if actual_board[row][column] == 'J':
                return (row, column)
                
def move_player(actual_board, new_board, posJugadorFutura, posActualJugador, action):     
    if posJugadorFutura is not None and new_board[posJugadorFutura[0]][posJugadorFutura[1]] != '#':
        # Movemos el jugador a la nueva posicion si no hay nada
        if new_board[posJugadorFutura[0]][posJugadorFutura[1]] == ' ':
            new_board[posJugadorFutura[0]][posJugadorFutura[1]] = 'J'
            new_board[posActualJugador[0]][posActualJugador[1]] = ' '
            
        # Si la posicion futura es un objetivo, guardamos la posicion del objetivo y movemos jugador
#        elif new_board[posJugadorFutura[0]][posJugadorFutura[1]] == 'O':
#            new_board[posJugadorFutura[0]][posJugadorFutura[1]] = 'J'
#            new_board[posActualJugador[0]][posActualJugador[1]] = ' '
            
        # Si hay una caja en la posicion futura
        elif new_board[posJugadorFutura[0]][posJugadorFutura[1]] == 'C':
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
            if actual_board[posCajaFutura[0]][posCajaFutura[1]] != 'C' and actual_board[posCajaFutura[0]][posCajaFutura[1]] != '#':
                new_board[posCajaFutura[0]][posCajaFutura[1]] = 'C'
                new_board[posJugadorFutura[0]][posJugadorFutura[1]] = 'J'
                new_board[posActualJugador[0]][posActualJugador[1]] = ' '
    return new_board
    
# define action function
def main_movement(actual_board, action):
    new_board = [row[:] for row in actual_board]

    # Obtenemos la posicion del jugador
    posActualJugador = get_actual_position(actual_board)

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
    if posJugadorFutura is not None and new_board[posJugadorFutura[0]][posJugadorFutura[1]] != '#':
        new_board = move_player(actual_board, new_board, posJugadorFutura, posActualJugador, action)

    return new_board

def generate_next_states(state):
    next_states = []
    for action in MovimientosPosibles:
        new_board = main_movement(state, action)
        if new_board not in next_states:
            next_states.append(new_board)
    return next_states

def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_closest_box_goal_distance(actual_board):
    player_pos = get_actual_position(actual_board)
    closest_box_goal_distance = float('inf')
    for row in range(len(actual_board)):
        for column in range(len(actual_board[row])):
            if actual_board[row][column] == 'O':
                distance = manhattan_distance(player_pos, (row, column))
                closest_box_goal_distance = min(closest_box_goal_distance, distance)
    return closest_box_goal_distance

def count_boxes_not_in_goals(actual_board, initial_board):
    count = 0
    for row in range(len(actual_board)):
        for column in range(len(actual_board[row])):
            if actual_board[row][column] == 'C' and initial_board[row][column] != 'O':
                count += 1
    return count

def get_closest_box_goal_distance(actual_board):
    player_pos = get_actual_position(actual_board)
    closest_box_goal_distance = float('inf')
    for row in range(len(actual_board)):
        for column in range(len(actual_board[row])):
            if actual_board[row][column] == 'O':
                distance = manhattan_distance(player_pos, (row, column))
                closest_box_goal_distance = min(closest_box_goal_distance, distance)
    return closest_box_goal_distance