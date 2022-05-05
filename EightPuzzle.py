import random
class EightPuzzle:
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    DIR = {"UP": -3, "DOWN": 3, "LEFT": -1, "RIGHT": 1}

    def __init__(self, initial_state, goal = (1,2,3,4,5,6,7,8,0)):
        if(self.is_solvable(initial_state)):
            self.initial_state = initial_state
            self.goal = goal
        else:
            self.initial_state = initial_state
            self.goal = goal

            # print("Puzzle state is not solvable")
            # return None
    
    def find_blank_square(self, state):
        try:
            return state.index(0)
        except ValueError:
            print("Blank Square not found! Make sure 0 is used to indicate an empty space")
            return -1
    
    def get_possible_actions(self, state):
        blank_index = self.find_blank_square(state)
        possible_actions = []

        if (not blank_index % 3 == 0):
            possible_actions.append(self.LEFT)
        if (not blank_index % 3 == 2):
            possible_actions.append(self.RIGHT)
        if (not blank_index < 3):
            possible_actions.append(self.UP)
        if (not blank_index > 5):
            possible_actions.append(self.DOWN)  
        
        return possible_actions
    
    def do_action(self, state, action):
        blank_index = self.find_blank_square(state)
        updated_state = list(state)

        move_index = blank_index + self.DIR[action]

        updated_state[blank_index], updated_state[move_index] = updated_state[move_index], updated_state[blank_index]

        return updated_state

    def is_goal(self, state):
        return state == self.goal
    
    def get_inversion_count(self, state):
        inv_count = 0

        for i in range (len(state)):
            for j in range(i+1, len(state)):
                if (state[i] != 0 and state[j] != 0 and state[i] > state[j]):
                    inv_count += 1
        
        return inv_count
    
    def is_solvable(self, state):
        return self.get_inversion_count(state) % 2 == 0
    
    def generate_random_puzzle(self):
        state = [0,1,2,3,4,5,6,7, 8, 9]
        while (True):
            random.shuffle(state)
            if (self.is_solvable(state)):
                return state

    def display(self, state):
        for i in range(len(state)):

            value = state[i]
            
            if(value == 0 or value == "0" ):
                value = "*"
                
            if((i + 1) % 3 == 0 ):
                print(value)

            else:
                print(value, end = " ")
        print("-----------")

