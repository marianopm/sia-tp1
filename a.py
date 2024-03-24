import time

class A:
    def search(game, heuristic):
        # Inicia el cronometro
        start = time.time()
        
        # Implementa el algoritmo A
        total_steps = 0
        nodes_expanded = 0
        frontier_nodes = 0
        time.sleep(2)
        
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        
        print("A*: Tiempo de ejecución", total_time, "segundos") 
        print("A*: Numero de pasos:", total_steps)
        print("A*: Numero de nodos expandidos:", nodes_expanded) 
        print("A*: Numero de nodos frontera:", frontier_nodes) 
        
        return None, None, None, None
    
    
    