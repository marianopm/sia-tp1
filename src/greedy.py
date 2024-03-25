from .sokobanGame import es_estado_final, generate_next_states, reconstruct_path, get_closest_box_goal_distance, count_boxes_not_in_goals

class Greedy:
    def search(game, heuristic):

        # Inicializa un conjunto vacío para realizar un seguimiento de los estados visitados
        visited = set()
        # Initialize the frontier with the initial state
        frontier = [(game.board, 0)]
        parent = {str(game.board): None}
        expanded_nodes = 0  # Counter for expanded nodes
        frontier_nodes = 1  # Counter for nodes in the frontier (initial state is in the frontier)            
                
        # Continue searching until the frontier is empty
        while frontier:
            # Pop the state with the minimum h value from the frontier
            current_state, current_h = min(frontier, key=lambda x: x[1])
            frontier.remove((current_state, current_h))
            # Increment the count of expanded nodes
            expanded_nodes += 1

            # Check if the current state is the goal state
            if es_estado_final(current_state, game.board):
                # Return the path to the goal state along with statistics
                return reconstruct_path(parent, current_state), expanded_nodes, frontier_nodes
            
            # Mark the current state as visited
            visited.add(str(current_state))

            # Generate all possible next states
            for next_state in generate_next_states(current_state):
                # Calculate h value (Manhattan distance between player and closest box goal)
                h = get_closest_box_goal_distance(next_state) if heuristic == 'Manhattan' else count_boxes_not_in_goals(next_state)
                
                # Check if the next state has not been visited
                if str(next_state) not in visited:
                    # Add the next state to the frontier
                    frontier.append((next_state, h))
                    # Increment the count of frontier nodes
                    frontier_nodes += 1
                    # Record the path to the next state
                    parent[str(next_state)] = current_state
                
        return None, expanded_nodes, frontier_nodes