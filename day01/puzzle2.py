#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer
from itertools import combinations
from functools import reduce
import operator

import util

LOG_LEVEL = logging.INFO

def main(input_file):

    values = []

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            val = int(line)

            for others in combinations(values, 2):
                others = list(others)
                others.append(val)
                if 2020 - sum(others) == 0:
                    logging.info(others)
                    logging.info("Answer: " + str(reduce(operator.mul, others, 1)))
                    break

            values.append(val)

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
