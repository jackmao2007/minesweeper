"""
This file creates a grid for minesweeper with mines and numbers
"""
import random

GRID_SIZE = input('Enter the size of the grid:')
while not GRID_SIZE.isdigit():
    print('Please enter a valid number')
    GRID_SIZE = input('Enter the size of the grid:')
GRID_SIZE = int(GRID_SIZE)

MINES = input('Enter the number of mines:')
while not MINES.isdigit():
    print('Please enter a valid number')
    MINES = input('Enter the number of mines:')
MINES = int(MINES)
while MINES >= GRID_SIZE ** 2:
    print('Too many mines!')
    MINES = input('Enter the number of mines:')
    while not MINES.isdigit():
        print('Please enter a valid number')
        MINES = input('enter the number of mines:')
    MINES = int(MINES)


def create_map(size):
    """This function creates a grid of size * size"""
    grid = []
    for i in range(size):
        a = []
        for j in range(size):
            a.append('0')
        grid.append(a)
    return grid


def create_mirror_map(grid):
    """this creates a mirror grid for a more effective mine deployment"""
    mr_map = []
    size = len(grid)
    for i in range(size):
        for j in range(size):
            mr_map.append([i, j])
    return mr_map


def deploy_mines(grid, mirror, number):
    """This fuction puts number of mines in to the grid"""
    if not number == 0:
        pos = random.choice(mirror)
        mirror.remove(pos)
        grid[pos[0]][pos[1]] = 'X'
        deploy_mines(grid, mirror, number - 1)


def update_clues(grid):
    """This function updates clues to the grid with mines"""
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] != 'X':
                grid[i][j] = str(clue(grid, i, j))


def clue(grid, row, column):
    """This function generate a clue at the location"""
    clu = 0
    for i in range(max(row - 1, 0), min(row + 2, len(grid))):
        for j in range(max(column - 1, 0), min(column + 2, len(grid))):
            if grid[i][j] == 'X':
                clu += 1
    return clu


def finished_map():
    """Gives the finished map"""
    mine_grid = create_map(GRID_SIZE)
    mirror_map = create_mirror_map(mine_grid)
    deploy_mines(mine_grid, mirror_map, MINES)
    update_clues(mine_grid)
    return mine_grid
