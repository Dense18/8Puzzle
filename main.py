from queue import PriorityQueue
from EightPuzzle import *
from Node import *
from queue import PriorityQueue

def main():
    # state_str = str(input("Enter puzzle state (012345678):" ))
    # state = tuple(int(elem) for elem in state_str)
    state = (1,2,6,3,8,0,5,7,4)
 
    puzzle = EightPuzzle(state)

    if not puzzle.is_solvable(state):
        print("Puzzle is not solvable")
        return -1

    print("Initial state:")
    puzzle.display(state)

    print("Solving (using Astar algorithm).......")
    n = Astar_algorithm(puzzle,heuristic=manhattan)
    
    if n:
        print("Solver found a solution!\n")
        print("Results:")
        for node in n.get_path():
            print("Action: ", end = "")
            print(node.action)
            puzzle.display(node.state)
            print("--------")
    
    else:
        print("Solver cannot find solution")

## Heuristic function by counting number of mispalced tiles
def misplaced(n):
    state = n.state
    goal = (1,2,3,4,5,6,7,8,0)

    return sum(tile != goal_tile for (tile, goal_tile) in zip(state, goal) if tile != 0)

## Manhattan heuristic function
def manhattan(n):
    state = n.state
    total = 0
    
    ##Create a coordinate for each value based on x and y axis
    coordinates = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),0:(2,2)}
    for i in range(len(coordinates)):
        if(state[i] != 0):      
            ##Get the coordinate of the value on index i
            x_i,y_i = coordinates[i + 1] if  i != len(coordinates)-1 else coordinates[0] ##goal is (1,2,3,4,5,6,7,8,0)
            
            ##Get the coordinate of  i
            x_goal,y_goal = coordinates[state[i]]
 
            total += abs(x_goal - x_i) + abs(y_goal - y_i)
            
    return total

## Gasching heuristic
# While any tile is out of its goal position do 
#   if the blank is in its own goal, 
#       then swap with any misplaced tile 
#   else swap with the tile that belongs in the blank's position
def gasching(n):
    total_move = 0
    state = list(n.state)

    goal = [1,2,3,4,5,6,7,8,0]
    misplaced_tiles = [s for (s, g) in zip(state, goal) if s != g and s != 0]

    while (len(misplaced_tiles) > 0):
        blank_index = state.index(0)

        ##If blank index is on the correct position
        if (blank_index == goal.index(0)):
            ## swap with any mismatched tiles
            misp_tile = misplaced_tiles[0]
            state[blank_index], state[state.index(misp_tile)] = state[state.index(misp_tile)], state[blank_index]
        else:
            ## Correct tile from the current index
            correct_tile = state.index(blank_index + 1)
            value = blank_index + 1

            state[blank_index], state[correct_tile] = state[correct_tile], state[blank_index]

            misplaced_tiles.remove(value)
        
        total_move += 1
    
    return total_move

def Astar_algorithm(problem, heuristic, display = False):
    start = Node(problem.initial_state)
    
    count = 0

    ##Create node to be searched
    open_queue = PriorityQueue()
    open_queue.put((0,count, start))
    open_queue_hash = {start}

    ##Keep track of node in the open queue
    visited = {start}

    ##keep track of f and g scores
    start.g = 0
    start.h = heuristic(start)
    start.f = start.g + start.h

    while not open_queue.empty():
        ##Pop node from the open_queue
        current = open_queue.get()[2]
        open_queue_hash.remove(current)
        
        if (problem.is_goal(current.state)):
            return current
        
        for neighbor in current.get_neighbors(problem):
            if neighbor.g > current.g + 1:
                neighbor.g = current.g + 1
                neighbor.h = heuristic(neighbor)
                neighbor.f = neighbor.g + neighbor.h

                if (neighbor not in open_queue_hash and neighbor not in visited):
                    count += 1
                    open_queue.put((neighbor.f, count, neighbor))
                    open_queue_hash.add(neighbor)
                    visited.add(neighbor)
    return None

def main_checkInversion():
    state = (3,8,1,4,5,7,2,6,0)
    puzzle = EightPuzzle(state)

    print(f"Inversion count using normal method: {puzzle.get_inversion_count(state)}")
    print(f"Inversion count using merge method: {puzzle.get_inversion_count_merge(state)}")

    puzzle.display(puzzle.initial_state)

if __name__ == '__main__':
    main()