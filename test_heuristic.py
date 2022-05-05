from EightPuzzle import *
from Node import *
from main import *

def test_gasching():
    state=(6,0,1,2,8,3,5,4,7)
    node = Node(state)
    assert gasching(node) == 9

    state=(6,0,1,2,8,3,5,7,4)
    node = Node(state)
    assert gasching(node) == 10

def test_manhattan():
    state=(6,0,1,2,8,3,5,4,7)
    node = Node(state)
    assert manhattan(node) == 15

    state=(6,0,1,2,8,3,5,7,4)
    node = Node(state)
    assert manhattan(node) == 15

    state = (0,1,3,4,2,5,7,8,6)
    node = Node(state)
    assert manhattan(node) == 4

def test_misplaced():
    state = (4, 3, 8, 6, 5, 1, 7, 0, 2)
    node = Node(state)
    assert misplaced(node) == 6

    state = (5, 7, 6, 0, 8, 4, 1, 3, 2)
    node = Node(state)
    assert misplaced(node) == 8

    state = (1, 3, 2, 4, 0, 5, 6, 7, 8)
    node = Node(state)
    assert misplaced(node) == 6

def test_heuristic():
    test_misplaced()
    test_manhattan()
    test_gasching()

if __name__ == '__main__':
    test_heuristic()
    print("All test passed!")

