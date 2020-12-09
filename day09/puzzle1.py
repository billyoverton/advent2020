#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def sum_of_two(value, numbers):
    is_sum = False

    while len(numbers) > 0:
        num1 = numbers.pop(0)
        for num2 in numbers:
            if num1 + num2 == value:
                is_sum = True
                logging.debug("{} is the sum of {} and {}".format(value, num1, num2))
                break
        if is_sum:
            break

    return is_sum

def main(input_file):

    PREAMBLE_LENGTH = 25
    numbers = []

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            number_under_test = int(line)

            if len(numbers) >= PREAMBLE_LENGTH:
                # We have enough numbers to start testing
                window = numbers[(-1*PREAMBLE_LENGTH):].copy()
                logging.debug("Number under test: {}".format(number_under_test))
                logging.debug(window)

                if not sum_of_two(number_under_test, window):
                    logging.info("Answer: {} first to not be a sum of two.".format(number_under_test))
                    break

            numbers.append(number_under_test)


if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
