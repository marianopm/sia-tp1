import configparser
from collections import defaultdict
from sokobanGame import SokobanGame
from a import A
from bfs import BFS
from dfs import DFS
from greedy import Greedy
from boards import board_1, board_2, board_3

def main():
    # Lee las configuraciones del archivo config_file
    config_params = read_config('config_file.config')
    
    # Crea el juego Sokoban con los parámetros leídos
    initial_node = eval(config_params['Sokoban']['initial_state'])
    goal_state = eval(config_params['Sokoban']['goal_state'])
    heuristic = eval(config_params['Heuristic']['heuristic'])
    board = eval(config_params['Board']['board'])
    game = SokobanGame(initial_node, goal_state, board)
    
     # Ejecuta algoritmo A
    if config_params['Algorithm']['a'] == 'True':
        solution_A, solution, expanded_nodes, frontier_nodes = A.search(game, heuristic)
        print("A* Solution:", solution_A)
        
     # Ejecuta algoritmo BFS
    if config_params['Algorithm']['bfs'] == 'True':
        solution, expanded_nodes, frontier_nodes  = BFS.search(game)
    
    # Ejecuta algoritmo DFS
    if config_params['Algorithm']['dfs'] == 'True':
        solution, expanded_nodes, frontier_nodes  = DFS.search(game)

    # Ejecuta algoritmo Greedy
    if config_params['Algorithm']['greedy'] == 'True':
        solution_greedy, solution, expanded_nodes, frontier_nodes  = Greedy.search(game, heuristic)
        print("Greedy Solution:", solution_greedy)
        
    print_solution(solution, expanded_nodes, frontier_nodes)

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    params = defaultdict(dict)
    for section in config.sections():
        for key, value in config.items(section):
            params[section][key] = value
    return params
    

def print_solution(solution, expanded_nodes, frontier_nodes):
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

if __name__ == "__main__":
    main()