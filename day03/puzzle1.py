#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def get_grid_value(baseGrid, x, y):
    # Y doesn't loop so return None if outside of map
    if y >= len(baseGrid):
        return None
    xMapped = x % len(baseGrid[0])
    return baseGrid[y][xMapped]

def main(input_file):

    baseGrid = []

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            baseGrid.append([char for char in line])
    logging.debug(util.pretty_grid(baseGrid))

    slope = (3, 1) # Slope for x and y
    start = (0, 0) # Starting point as x, y

    trees_encountered = 0
    while True:
        next_point_x = start[0] + slope[0]
        next_point_y = start[1] + slope[1]
        value = get_grid_value(baseGrid, next_point_x, next_point_y)

        logging.debug("Checking point ({},{}): {}".format(next_point_x, next_point_y, value))

        if value is None:
            break
        elif value == '#':
            trees_encountered += 1

        start = (next_point_x, next_point_y)

    logging.info("Answer: Encountered {} trees.".format(trees_encountered))

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
