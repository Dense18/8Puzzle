import random
import EightPuzzle as puzzle
import copy

class EightPuzzleGenerator:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_random_puzzle():
        state = [0,1,2,3,4,5,6,7,8]
        while (True):
            random.shuffle(state)
            if (EightPuzzleGenerator.is_solvable(state)):
                return puzzle.EightPuzzle(state)
    
    @staticmethod
    def generate_random_puzzle_state():
        state = [0,1,2,3,4,5,6,7,8]
        while (True):
            random.shuffle(state)
            if (EightPuzzleGenerator.is_solvable(state)):
                return state

    @staticmethod
    def is_solvable(state):
        #return EightPuzzleGenerator.get_inversion_count(state) % 2 == 0
        return EightPuzzleGenerator.get_inversion_count_merge(state) % 2 == 0

    @staticmethod
    def get_inversion_count(state):
        inv_count = 0

        for i in range (len(state)):
            for j in range(i+1, len(state)):
                if (state[i] != 0 and state[j] != 0 and state[i] > state[j]):
                    inv_count += 1
        
        return inv_count

    @staticmethod
    def get_inversion_count_merge( state):
        arr = list(copy.deepcopy(state))
        inv_count = EightPuzzleGenerator.__merge_sort(arr, 0, len(arr) - 1)
        return inv_count

    @staticmethod
    def __merge_sort(arr, left, right):

        inv_count = 0

        if (left < right):
            mid = (left + right)//2

            inv_count += EightPuzzleGenerator.__merge_sort(arr, left, mid)
            inv_count += EightPuzzleGenerator.__merge_sort(arr, mid+1, right)
            inv_count += EightPuzzleGenerator.__merge(arr, left, mid, right)
        
        return inv_count
    
    @staticmethod
    def __merge(arr, left, mid, right):
        inv_count = 0        
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
                    inv_count += mid - left + 1 - i 
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

    