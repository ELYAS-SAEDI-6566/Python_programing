from collections import deque

class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

queue = deque([PuzzleNode([[2],[3],[4]])])

node = PuzzleNode([[2],[3],[4]])
print(queue.popleft.state)
