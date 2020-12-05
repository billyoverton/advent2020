#!/usr/bin/env python3
import sys
import logging
import math
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def binary_partition_search(directions, min=0, max=127):
    for direction in directions:
        if direction in ['F', 'L']:
            max = math.floor( (max+min) / 2)
        elif direction in ['B', 'R']:
            min = math.ceil( (max+min) / 2)
        else:
            raise Exception("Unknown direction", direction)

        logging.debug("Direction: {}, Max: {}, Min: {}".format(direction,max,min))

    assert min == max
    return min

def position_to_row_col(position_string):
    row_string = position_string[:7]
    col_string = position_string[-3:]
    logging.debug("Position: {}  Row Position: {} Col Position: {}".format(position_string, row_string, col_string))

    logging.debug("Finding row")
    row = binary_partition_search(row_string, 0, 127)

    logging.debug("Finding col")
    col = binary_partition_search(col_string, 0, 7)

    return row, col

def position_to_seat_id(position_string):
    row, col = position_to_row_col(position_string)
    id = 8 * row + col

    logging.debug("{} => ID# {}".format(position_string, id))
    return id

def main(input_file):

    max_seat_id=0

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            id = position_to_seat_id(line)

            if id > max_seat_id:
                logging.debug("New Max Seat ID Found: {}:{}".format(line, id))
                max_seat_id = id

    logging.info("Answer: Max seat ID founnd: {}".format(max_seat_id))

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
