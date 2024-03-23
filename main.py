import configparser
from collections import defaultdict
from sokobanGame import SokobanGame
from a import A
from bfs import BFS
from dfs import DFS
from greedy import Greedy

def main():
    # Lee las configuraciones del archivo config_file
    config_params = read_config('config_file.config')
    
    # Crea el juego Sokoban con los parámetros leídos
    initial_state = eval(config_params['Sokoban']['initial_state'])
    goal_state = eval(config_params['Sokoban']['goal_state'])
    game = SokobanGame(initial_state, goal_state)
    
     # Ejecuta algoritmo A
    if config_params['Algorithm']['a'] == 'True':
        solution_A = A.search(game)
        print("A* Solution:", solution_A)
        
     # Ejecuta algoritmo BFS
    if config_params['Algorithm']['bfs'] == 'True':
        solution_bfs = BFS.search(game)
        print("BFS Solution:", solution_bfs)
    
    # Ejecuta algoritmo DFS
    if config_params['Algorithm']['dfs'] == 'True':
        solution_dfs = DFS.search(game)
        print("DFS Solution:", solution_dfs)

    # Ejecuta algoritmo Greedy
    if config_params['Algorithm']['greedy'] == 'True':
        solution_greedy = Greedy.search(game)
        print("Greedy Solution:", solution_greedy)

def read_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    params = defaultdict(dict)
    for section in config.sections():
        for key, value in config.items(section):
            params[section][key] = value
    return params
    
if __name__ == "__main__":
    main()