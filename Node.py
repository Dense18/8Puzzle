class Node:
    def __init__(self, state, parent = None, action = None, path_cost = 0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

        self.f = float("inf")
        self.g = float("inf")
        self.h = 0

        self.depth = 0
        if (parent):
            self.depth = parent.depth + 1
    
    def __eq__(self, other):
        #isinstance(self, other) and 
        return tuple(self.state) == tuple(other.state)
    
    def get_neighbors(self, problem):
        return [self.get_child_node(problem, action) for action in problem.get_possible_actions(self.state) ]
    
    def get_child_node(self, problem, action):
        result_state = problem.do_action(self.state, action)
        result_node = Node(result_state, self, action, problem.path_cost(self.path_cost, self.state, action, result_state))
        return result_node
    
    def get_path(self):
        path = []
        node = self

        while (node):
            path.append(node)
            node = node.parent
        
        return list(reversed(path))

    def solution(self):
        return [node.action for node in self.get_path()]

    def __hash__(self):
        return hash(tuple(self.state))
    

