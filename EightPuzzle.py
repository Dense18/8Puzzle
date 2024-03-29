import random
import copy
from Problem import *

class EightPuzzle():
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    DIR = {"UP": -3, "DOWN": 3, "LEFT": -1, "RIGHT": 1}

    def __init__(self, state, goal = (1,2,3,4,5,6,7,8,0)):
        self.state = state
        self.goal = goal
        self.onChangeListener = None
    
    def setOnChangeListener(self, listener):
        self.onChangeListener = listener

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
        
        return tuple(updated_state)

    def move_action(self, state, action):
        blank_index = self.find_blank_square(state)
        updated_state = list(state)

        move_index = blank_index + self.DIR[action]

        updated_state[blank_index], updated_state[move_index] = updated_state[move_index], updated_state[blank_index]

        if (self.onChangeListener):
            self.onChangeListener()
        
        return tuple(updated_state)
        
    def is_goal(self, state):
        return state == self.goal

    def generate_random_puzzle(self):
        state = [0,1,2,3,4,5,6,7,8]
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
    
    #----------------------------        Check Solvability  ---------------------------#
    def get_inversion_count(self, state):
        inv_count = 0

        for i in range (len(state)):
            for j in range(i+1, len(state)):
                if (state[i] != 0 and state[j] != 0 and state[i] > state[j]):
                    inv_count += 1
        
        return inv_count
    
    def get_inversion_count_merge(self, state):
        arr = list(copy.deepcopy(state))
        inv_count = self.merge_sort(arr, 0, len(arr) - 1)
        return inv_count
    
    def merge_sort(self, arr, left, right):

        inv_count = 0

        if (left < right):
            mid = (left + right)//2

            inv_count += self.merge_sort(arr, left, mid)
            inv_count += self.merge_sort(arr, mid+1, right)
            inv_count += self.merge(arr, left, mid, right)
        
        return inv_count
            
    def merge(self, arr, left, mid, right):
        inv_count = 0

        # n1 = mid - left + 1
        # n2 = right - mid

        # left_array = []
        # right_array = []

        # for i in range(n1):
        #     left_array.append(arr[left + i])
        
        # for j in range(n2):
        #     right_array.append(arr[mid + 1 + j])
        
        left_array = arr[left : mid + 1]
        right_array = arr[mid + 1: right + 1]

        k = left
        i = j = 0

        ##Merge temp arrays
        while (i < len(left_array) and j < len(right_array)):
            if (left_array[i] <= right_array[j]):
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                if(arr[k] != 0):
                    inv_count += mid - left + 1 - i ##or len(left_array) - 1
                j += 1
            k+= 1
                
        ##Merge Remaining values if exist
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1
        
        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1
        
        return inv_count

    def is_solvable(self, state):
        return self.get_inversion_count_merge(state) % 2 == 0

    ##Assume all cost are one between any state from a valid action
    def path_cost(self, current_cost, state, action, new_state):
        return current_cost + 1

