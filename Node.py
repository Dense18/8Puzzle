class Node:
    def __init__(self, state, parent = None, action = None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.parent = path_cost
        self.depth = 0

        if (parent):
            self.depth = parent.depth + 1
