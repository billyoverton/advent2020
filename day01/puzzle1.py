#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer

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

            for other in values:
                if 2020 - (other + val) == 0:
                    logging.info("Number 1: " + str(other))
                    logging.info("Number 2: " + str(val))
                    logging.info("Answer: " + str(other * val))
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
