import time

class BFS:
    def search(game):
        # Inicia el cronometro
        start = time.time()
        
        # Implementa el algoritmo BFS
        total_steps = 0
        nodes_expanded = 0
        frontier_nodes = 0
        
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        
        print("BFS: Tiempo de ejecución", total_time, "segundos") 
        print("BFS: Numero de pasos:", total_steps)
        print("BFS: Numero de nodos expandidos:", nodes_expanded) 
        print("BFS: Numero de nodos frontera:", frontier_nodes) 
        
        pass