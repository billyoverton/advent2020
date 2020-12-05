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

    seat_ids = []

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            seat_ids.append(position_to_seat_id(line))

    seat_ids.sort()

    for i in range(len(seat_ids)):
        if seat_ids[i]+2 == seat_ids[i+1]:
            logging.info("Answer: Seat ID is {}".format((seat_ids[i]+1)))
            break

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
