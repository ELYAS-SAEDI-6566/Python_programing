from collections import deque
from tabulate import tabulate

class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

def is_goal_state(state, goal_state):
    return state == goal_state

def get_possible_moves(state):
    moves = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == "":
                if i > 0:
                    moves.append(("UP", (i, j), (i - 1, j)))
                if i < 2:
                    moves.append(("DOWN", (i, j), (i + 1, j)))
                if j > 0:
                    moves.append(("LEFT", (i, j), (i, j - 1)))
                if j < 2:
                    moves.append(("RIGHT", (i, j), (i, j + 1)))
    return moves

def perform_move(state, move):
    action, (i, j), (new_i, new_j) = move
    new_state = [row[:] for row in state]
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state

def bfs_search(initial_state, goal_state):
    queue = deque([PuzzleNode(initial_state)])
    visited = set()
    
    while queue:
        current_node = queue.popleft()
        current_state = current_node.state
        
        if is_goal_state(current_state, goal_state):
            # Path found, reconstruct and return it
            path = []
            while current_node.parent:
                path.append((current_node.action, current_node.state))
                current_node = current_node.parent
            path.reverse()
            return path
        
        visited.add(tuple(map(tuple, current_state)))
        
        possible_moves = get_possible_moves(current_state)
        for move in possible_moves:
            next_state = perform_move(current_state, move)
            if tuple(map(tuple, next_state)) not in visited:
                next_node = PuzzleNode(next_state, current_node, move[0])
                queue.append(next_node)
            
    return None

# Define the initial and goal states
initial_state = [
    [2, 8, 3],
    [1, "", 4],
    [7, 6, 5]
]
# initial_state = [
#     [1, 2, 3],
#     [5, "", 6],
#     [4, 7, 8]
# ]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, ""]
]

# Perform the Breadth-First Search
solution_path = bfs_search(initial_state, goal_state)

if solution_path:
    print("Solution Found:")
    for step, state in solution_path:
        print("Action:", step)
        print(tabulate(state ,tablefmt="simple_grid"))
else:
    print("No solution found.")
