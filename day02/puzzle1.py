#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def is_valid_password(min, max, character, password):
    count = password.count(character)
    if min <= count <= max:
        return True
    else:
        return False

def main(input_file):

    valid_count = 0
    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            parts = line.split(":")
            policy_parts = parts[0].strip().split(" ");
            range_parts = policy_parts[0].strip().split("-")

            password = parts[1].strip()
            character = policy_parts[1].strip()
            min = int(range_parts[0])
            max = int(range_parts[1])
            logging.debug("Min: {}, Max: {}, Character: {}, Password {}".format(min,max,character,password))


            if is_valid_password(min,max,character,password):
                valid_count += 1
                logging.debug("Password {} is a valid password".format(password))
            else:
                logging.debug("Password {} is a invalid password".format(password))

    logging.info("Answer: {}".format(valid_count))

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
