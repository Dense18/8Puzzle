from EightPuzzle import *

def main():
    state = (1,2,3,4,5,6,7,8,0)
    puzzle = EightPuzzle(state)
    puzzle.display(state)
    print(puzzle.is_goal(state))

if __name__ == '__main__':
    main()