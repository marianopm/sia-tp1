import configparser
from collections import defaultdict
import time
from src.sokobanGame import SokobanGame
from src.aStar import A
from src.bfs import BFS
from src.dfs import DFS
from src.greedy import Greedy
from src.boards import board_1, board_2, board_3

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
        # Inicia el cronometro
        start = time.time()
        solution, expanded_nodes, frontier_nodes = A.search(game, heuristic)
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        print("A*: Tiempo de ejecución", total_time, "segundos")
        print_solution(solution, expanded_nodes, frontier_nodes)
        
     # Ejecuta algoritmo BFS
    if config_params['Algorithm']['bfs'] == 'True':
        # Inicia el cronometro
        start = time.time()
        solution, expanded_nodes, frontier_nodes  = BFS.search(game)
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        print("BFS: Tiempo de ejecución", total_time, "segundos")
        print_solution(solution, expanded_nodes, frontier_nodes) 
    
    # Ejecuta algoritmo DFS
    if config_params['Algorithm']['dfs'] == 'True':
        # Inicia el cronometro
        start = time.time()
        solution, expanded_nodes, frontier_nodes  = DFS.search(game)
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        print("DFS: Tiempo de ejecución", total_time, "segundos")
        print_solution(solution, expanded_nodes, frontier_nodes)

    # Ejecuta algoritmo Greedy
    if config_params['Algorithm']['greedy'] == 'True':
        # Inicia el cronometro
        start = time.time()
        solution, expanded_nodes, frontier_nodes  = Greedy.search(game, heuristic)
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        print("Greedy: Tiempo de ejecución", total_time, "segundos")
        print_solution(solution, expanded_nodes, frontier_nodes)
        
    

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    params = defaultdict(dict)
    for section in config.sections():
        for key, value in config.items(section):
            params[section][key] = value
    return params

# Método para imprimir el tablero
def print_board(board):
    for row in board:
        print(" ".join(row))

def print_solution(solution, expanded_nodes, frontier_nodes):
    if solution:
            print("Exito!")
            print(f"Total number of steps: {len(solution) - 1}")
            print(f"Expanded nodes: {expanded_nodes}")
            print(f"Frontier nodes: {frontier_nodes}")
            # print the board state of each step
            print("Solución encontrada:")
            for step, state in enumerate(solution):
                print(f"Paso {step}:")
                print_board(state)
    else:
        print("Fracaso")

if __name__ == "__main__":
    main()
