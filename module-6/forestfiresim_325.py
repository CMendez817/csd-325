"""Forest Fire Sim with Lake Firebreak, modified by Sue Sampson, based on Al Sweigart's code.
Adds a central lake that fire cannot cross. Lake uses '~' character and is blue in color.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # New constant to represent lake

# Simulation settings (try adjusting these!):
INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)

        # Prepare next forest state:
        nextForest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                current_cell = forest[(x, y)]

                # Don't modify water—it acts as a firebreak.
                if current_cell == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if current_cell == EMPTY and random.random() <= GROW_CHANCE:
                    nextForest[(x, y)] = TREE
                elif current_cell == TREE and random.random() <= FIRE_CHANCE:
                    nextForest[(x, y)] = FIRE
                elif current_cell == FIRE:
                    # Spread fire to neighbors (but not into water).
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            neighbor = forest.get((x + ix, y + iy))
                            if neighbor == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # Tree burns out:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Carry over the existing cell state
                    nextForest[(x, y)] = current_cell

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Creates a forest with a central water feature (lake) that cannot burn or change."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    lake_width = WIDTH // 4
    lake_height = HEIGHT // 4
    lake_x_start = (WIDTH - lake_width) // 2
    lake_y_start = (HEIGHT - lake_height) // 2

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Check if (x, y) falls within lake area:
            if lake_x_start <= x < lake_x_start + lake_width and lake_y_start <= y < lake_y_start + lake_height:
                forest[(x, y)] = WATER  # Place water
            else:
                # Randomly plant trees or leave empty:
                if random.random() <= INITIAL_TREE_DENSITY:
                    forest[(x, y)] = TREE
                else:
                    forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    """Displays the forest on screen using color based on element type."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg('blue')
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('Press Ctrl-C to quit.')


# Program entry point
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
