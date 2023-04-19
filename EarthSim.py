# A life simulator thing
import random
import pygame as pg

GRID_ROWS = 3
GRID_COLUMNS = 3

STONE = {
        'symbol': 'S',
        'natural': False
        }

def random_tile():
    return STONE

def make_grid():
    grid = []
    for row in range(GRID_ROWS):
        grid.append([])
        for column in range(GRID_COLUMNS):
            grid[row].append(random_tile())
    return grid

def print_grid_symbols(grid):
    for row in range(GRID_ROWS):
        for column in range(GRID_COLUMNS):
            print(grid[row][column]['symbol'], end='')
        print('')

if __name__ == '__main__': 
    grid = make_grid()
    print_grid_symbols(grid)
