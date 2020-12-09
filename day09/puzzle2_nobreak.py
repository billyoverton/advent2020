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

    invalid_number = None

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            number_under_test = int(line)

            if invalid_number is None and len(numbers) >= PREAMBLE_LENGTH:
                # We have enough numbers to start testing
                window = numbers[(-1*PREAMBLE_LENGTH):].copy()
                logging.debug("Number under test: {}".format(number_under_test))
                logging.debug(window)

                if not sum_of_two(number_under_test, window):
                    invalid_number = number_under_test
                    logging.debug("Invalid number {} found.".format(invalid_number))

            numbers.append(number_under_test)

    logging.debug(numbers)

    found_range = None
    for i in range(len(numbers)):
        range_sum = 0
        end = i + 2
        while range_sum < invalid_number and end < len(numbers):
            checking = numbers[i:end]
            range_sum = sum(checking)
            logging.debug("Checking {} Sum: {}".format(checking, range_sum))

            if range_sum == invalid_number:
                found_range = checking
                logging.debug("Weakness range found: {}".format(found_range))
                break

            end += 1

        if found_range is not None:
            break

    smallest, largest  = util.min_max(found_range)
    logging.debug("Smallest: {} Largest: {}".format(smallest, largest))
    answer = smallest + largest
    logging.info("Answer: {}".format(answer))


if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
