# A life simulator thing
import random

GRASS_GROWTH_MIN_NATURAL = 3
GRASS_GROWTH_CHANCE = 0.5

FLOWER_CHANCE = 0.2


GRID_ROWS = 10
GRID_COLUMNS = 10

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

FLOWER = {
        'symbol': 'F',
        'natural': True
        }

TREE = {
        'symbol': 'T',
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

# supposed to return a list of the surrounding tile types, in progress
def check_surrounding_tiles(grid, base_x, base_y):
    surrounding_tiles = []
    for x in range(base_x - 1, base_x + 2):
        for y in range(base_y - 1, base_y + 2):
            if x == base_x and y == base_y:
                continue
            if x < 0 or y < 0:
                continue
            try: 
                surrounding_tiles.append(grid[x][y])
            except IndexError:
                continue
    return surrounding_tiles

# Main
if __name__ == '__main__':
    grid = make_grid()
    for year in range(END_YEAR):
        for row in range(GRID_ROWS):
            for column in range(GRID_COLUMNS):
                if grid[row][column] == GRASS:
                    surrounding_tiles = check_surrounding_tiles(grid, row, column)
                    
                    natural = 0
                    for tile in surrounding_tiles:
                        if tile['natural']:
                            natural += 1
                    
                    if natural >= GRASS_GROWTH_MIN_NATURAL and GRASS_GROWTH_CHANCE <= random.random():
                        if random.random() <= FLOWER_CHANCE:
                            grid[row][column] = FLOWER
                        else:
                            grid[row][column] = TREE

                        

        # Print out results
        print('year:', year)
        print_grid_symbols(grid)
        print('')
