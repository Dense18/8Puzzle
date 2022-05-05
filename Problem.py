class Problem:
    def __init__(self, initial_state, goal = None):
        self.initial_state = initial_state
        self.goal = goal
        
    def get_possible_actions(self, state):
        raise NotImplementedError
    
    def do_action(self, state, action):
        raise NotImplementedError

    def is_goal(self, state):
        raise NotImplementedError 
    
    def path_cost(self, current_cost, state, action, new_state):
        raise NotImplementedError
