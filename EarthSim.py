# A life simulator thing
import random

GRID_ROWS = 5
GRID_COLUMNS = 5

END_YEAR = 10

# Define tile types
STONE = {
        'symbol': 'S',
        'natural': False
        }

GRASS = {
        'symbol': 'G',
        'natural': True
        }

# A list of tile types, couldn't find a better way to do this
TILES = [STONE, GRASS]

# Returns, well, a random tile
def random_tile():
    return TILES[random.randrange(0, len(TILES))]

# Makes the grid
def make_grid():
    grid = []
    for row in range(GRID_ROWS):
        grid.append([])
        for column in range(GRID_COLUMNS):
            grid[row].append(random_tile())
    return grid

# Gets the grid's tile's symbols and prints them
def print_grid_symbols(grid):
    for row in range(GRID_ROWS):
        for column in range(GRID_COLUMNS):
            print(grid[row][column]['symbol'], end='')
        print('')

# supposed to return a list of the surrounding tile types, haven't found a good way to implement this yet
def check_surrounding_tiles(grid, x, y):
    pass     

if __name__ == '__main__':
    grid = make_grid()
    for year in range(END_YEAR):
        for row in range(GRID_ROWS):
            for column in range(GRID_COLUMNS):
                if grid[row][column] == STONE:
                    print('This is a stone!')
                elif grid[row][column] == GRASS:
                    print('This is grass.')

        # Print out results
        print('year:', year)
        print_grid_symbols(grid)
        print('')
