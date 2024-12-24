# a little sudoku fun!!!
import numpy as np

def horizontal(grid):
    matches = 0
    for row in range(grid.shape[0]):
        for i in range(grid.shape[1]-3):
            combo = ''.join((grid[row][i],grid[row][i+1],grid[row][i+2],grid[row][i+3]))
            if combo in ('SAMX', 'XMAS'):
                matches += 1
    return matches

def debug_check(grid, cords):
    STR=''
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if (i,j) in cords:
                STR += str.upper(grid[i][j])
                continue
            STR += str.lower(grid[i][j])
        STR += '\n'
    print(STR)
    #input('anykey to continue')

def diagonal(grid):
    matches = 0
    for row in range(grid.shape[0]-3):
        for i in range(grid.shape[1]-3):
            combo = ''.join([grid[row][i],grid[row+1][i+1],grid[row+2][i+2],grid[row+3][i+3]]) 
            if combo in ('XMAS', 'SAMX'):
                matches += 1
                #debug_check(grid, ((row, i), (row+1, i+1), (row+2, i+2), (row+3, i+3)))
    return matches

def find_matches(grid):
    return horizontal(grid)+diagonal(grid)

def check_cross(grid):
    matches = 0
    for row in range(1, grid.shape[0]-1):
        for col in range(1, grid.shape[1]-1):
            if grid[row][col] == 'A':
                d1 = grid[row-1][col-1]+grid[row][col]+grid[row+1][col+1]
                d2 = grid[row+1][col-1]+grid[row][col]+grid[row-1][col+1]
                if 'MAS' in (d1[::-1], d1) and 'MAS' in (d2[::-1], d2):
                    matches += 1
    return matches

with open("input", "r") as f:
    box = np.array(list(map(list, f.read().strip().split('\n'))))

    accumulator = 0
    accumulator += diagonal(box)
    accumulator += diagonal(np.fliplr(box))
    accumulator += horizontal(box)
    accumulator += horizontal(box.T)
    
    print("Part 1:", accumulator)
    accumulator = 0
    accumulator += check_cross(box)
    print("Part 2:", accumulator)
