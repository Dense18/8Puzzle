import pygame
from EightPuzzleSolver import *
from EightPuzzle import *
from settings import *
from colors import *
from EightPuzzleGenerator import *

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eight Puzzle")
clock = pygame.time.Clock()

TILE_FONT = pygame.font.SysFont("1", 30)
SOLVING_TEXT = TILE_FONT.render("Solving....", 1, BLACK)

TILE_GAP = 10 
starting_x = WIDTH//2 - (TILE_SIZE + TILE_GAP) * 3 //2 + 3
starting_y = HEIGHT//2 - (TILE_SIZE + TILE_GAP) * 3 //2 + 3

numMoves = 0
def main():
    global numMoves
    isRunning = True

    puzzle = EightPuzzle(EightPuzzleGenerator.generate_random_puzzle_state())
    puzzle.setOnChangeListener(onChangeState)

    while (isRunning):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (not puzzle.is_goal(puzzle.state)):
                    puzzle_index = get_puzzle_index(pos)
                    move(puzzle, puzzle_index)

            if event.type == pygame.KEYDOWN:
                if not puzzle.is_goal(puzzle.state):
                    possible_actions = puzzle.get_possible_actions(puzzle.state)
                    if puzzle.LEFT in possible_actions and event.key == pygame.K_LEFT :
                        puzzle.state = puzzle.move_action(puzzle.state, puzzle.LEFT)
                    if puzzle.RIGHT in possible_actions and event.key == pygame.K_RIGHT:
                        puzzle.state = puzzle.move_action(puzzle.state, puzzle.RIGHT)
                    if puzzle.UP in possible_actions and event.key == pygame.K_UP :
                        puzzle.state = puzzle.move_action(puzzle.state, puzzle.UP)
                    if puzzle.DOWN in possible_actions and event.key == pygame.K_DOWN :
                        puzzle.state = puzzle.move_action(puzzle.state, puzzle.DOWN)

                if event.key == pygame.K_r:
                    puzzle.state = EightPuzzleGenerator.generate_random_puzzle_state()
                    numMoves = 0

                if event.key == pygame.K_s:
                    solve_puzzle(puzzle)
        
        draw_puzzle(WIN, puzzle)
        draw_instructions(WIN)

        clock.tick(FPS)

        
    pygame.quit()

def draw_puzzle(win, puzzle, isSolving = False):
    global starting_x, starting_y, numMoves
    WIN.fill((255,255,200))
    x = starting_x
    y = starting_y

    if (isSolving):
        WIN.blit(TILE_FONT.render("Solving....", 1, BLACK), 
                (x - TILE_GAP + (TILE_SIZE + TILE_GAP) * 3 + TILE_GAP + 100,
                y - TILE_GAP + ((TILE_SIZE + TILE_GAP) * 3 + TILE_GAP)//2))

    elif (puzzle.is_goal(puzzle.state)):
        WIN.blit(TILE_FONT.render("Solved!", 1, BLACK), 
                (x - TILE_GAP + (TILE_SIZE + TILE_GAP) * 3 + TILE_GAP + 100,
                y - TILE_GAP + ((TILE_SIZE + TILE_GAP) * 3 + TILE_GAP)//2))

    #Draw border
    pygame.draw.rect(win, BLACK, (x - TILE_GAP, y - TILE_GAP, 
                        (TILE_SIZE + TILE_GAP) * 3 + TILE_GAP, (TILE_SIZE + TILE_GAP) * 3 + TILE_GAP), 
                        8)

    #Draw puzzle state
    for i, tile in enumerate(puzzle.state):
        if (i % 3 == 0 and i != 0):
            y += TILE_SIZE + TILE_GAP
            x =  starting_x

        if tile != 0 :
            pygame.draw.rect(win, RED, (x, y, TILE_SIZE, TILE_SIZE))
            text = TILE_FONT.render(str(tile), 1, BLACK)
            win.blit(text, (x + TILE_SIZE//2 - text.get_width()//2, y + TILE_SIZE//2 - text.get_height()//2))
            
        x += TILE_SIZE + TILE_GAP

    ##Draw number of moves
    move_text = TILE_FONT.render("Number of Moves : " + str(numMoves), 1, BLACK)
    win.blit(move_text, (WIDTH//2 - move_text.get_width()//2, starting_y + (TILE_SIZE + TILE_GAP) * 3 + TILE_SIZE))

    #Draw instructions
    draw_instructions(win)
        
    pygame.display.update()

def move(puzzle, puzzle_index):
    blank_index = puzzle.find_blank_square(puzzle.state)
    possible_actions = puzzle.get_possible_actions(puzzle.state)

    if (puzzle.UP in possible_actions and blank_index + puzzle.DIR[puzzle.UP] == puzzle_index):
        puzzle.state = puzzle.move_action(puzzle.state, puzzle.UP)
    if (puzzle.DOWN in possible_actions and blank_index + puzzle.DIR[puzzle.DOWN] == puzzle_index):
        puzzle.state = puzzle.move_action(puzzle.state, puzzle.DOWN)
    if (puzzle.LEFT in possible_actions and blank_index + puzzle.DIR[puzzle.LEFT] == puzzle_index):
        puzzle.state = puzzle.move_action(puzzle.state, puzzle.LEFT)
    if (puzzle.RIGHT in possible_actions and blank_index + puzzle.DIR[puzzle.RIGHT] == puzzle_index):
        puzzle.state = puzzle.move_action(puzzle.state, puzzle.RIGHT)


def get_puzzle_index(pos):
    x, y = pos
    if (x < starting_x or x > starting_x + TILE_SIZE * 3 + TILE_GAP * 2 ):
        return
    if (y < starting_y or y > starting_y + TILE_SIZE * 3 + TILE_GAP * 2 ):
        return

    row = (y - starting_y) // (TILE_SIZE + TILE_GAP)
    col = (x - starting_x) // (TILE_SIZE + TILE_GAP)
    if (0 <= row < 3 and 0 <= col < 3):
        puzzle_index = col + row * 3
        return puzzle_index

def draw_instructions(win):
    global starting_y, starting_x
    random_text = TILE_FONT.render("Press 'r' to generate a new random puzzle", 1, BLACK)
    solve_text = TILE_FONT.render("Press 's' to solve the puzzle", 1, BLACK)
    
    win.blit(random_text, (WIDTH //2 - random_text.get_width()//2, starting_y - TILE_GAP - TILE_SIZE - solve_text.get_height() - 17))
    win.blit(solve_text, (WIDTH //2 - solve_text.get_width()//2, starting_y - TILE_GAP - TILE_SIZE))

def solve_puzzle(puzzle):
    node_solution = Astar_algorithm(puzzle, manhattan)
    actions = node_solution.solution()
    for action in actions:
        clock.tick(5)
        if action == "UP":
            puzzle.state = puzzle.move_action(puzzle.state, puzzle.UP)
        elif action == "DOWN":
            puzzle.state = puzzle.move_action(puzzle.state, puzzle.DOWN)
        elif action == "LEFT":
            puzzle.state = puzzle.move_action(puzzle.state, puzzle.LEFT)
        elif action == "RIGHT":
            puzzle.state = puzzle.move_action(puzzle.state, puzzle.RIGHT)
        draw_puzzle(WIN, puzzle, isSolving=True)
                        
    clock.tick(FPS)

def onChangeState():
    global numMoves
    numMoves += 1

if __name__ == "__main__":
    main()