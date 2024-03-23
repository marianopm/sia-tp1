import time

class Greedy:
    def search(game):
        # Inicia el cronometro
        start = time.time()
        
        # Implementa el algoritmo Greedy
        total_steps = 0
        nodes_expanded = 0
        frontier_nodes = 0
        
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        
        print("Greedy: Tiempo de ejecución", total_time, "segundos") 
        print("Greedy: Numero de pasos:", total_steps)
        print("Greedy: Numero de nodos expandidos:", nodes_expanded) 
        print("Greedy: Numero de nodos frontera:", frontier_nodes) 
        
        pass