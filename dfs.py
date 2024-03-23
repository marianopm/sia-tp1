import time

class DFS:
    def search(game):
        # Inicia el cronometro
        start = time.time()
        
        # Implementa el algoritmo DFS
        total_steps = 0
        nodes_expanded = 0
        frontier_nodes = 0
        
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        
        print("DFS: Tiempo de ejecución", total_time, "segundos") 
        print("DFS: Numero de pasos:", total_steps)
        print("DFS: Numero de nodos expandidos:", nodes_expanded) 
        print("DFS: Numero de nodos frontera:", frontier_nodes) 
        
        pass