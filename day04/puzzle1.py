#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def is_passport_valid(passport, required_fields, optional_fields):
    logging.debug(passport)
    for key in required_fields:
        if key not in passport:
            logging.debug("Did not find key: {}".format(key))
            return False
    return True

def main(input_file):

    passports = []

    with open(input_file) as f:
        previous_blank = True
        passport = None
        while True:
            line = f.readline().strip()

            if not line and previous_blank:
                break
            elif not line:
                previous_blank = True
                passports.append(passport) # Add the passport record we last encounterd
                continue

            if previous_blank == True:
                # We are starting a new passport
                logging.debug("Starting new passport record.")
                passport = {}

            parts = line.split()
            for part in parts:
                key, value = part.strip().split(":")
                logging.debug("Adding passport item {}: {}".format(key, value))
                passport[key] = value

            previous_blank = False

    required_fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
    ]

    optional_fields = [
        "cid"
    ]

    valid_passports = 0
    for passport in passports:
        if is_passport_valid(passport, required_fields, optional_fields):
            valid_passports += 1

    logging.info("Answer: Valid passport count: {}".format(valid_passports))

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
