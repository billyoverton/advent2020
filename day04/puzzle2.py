#!/usr/bin/env python3
import sys
import logging
import re
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def height_validator(value):
    if re.search("^[0-9]{2,3}(cm|in)$", value):
        unit = value[-2:]
        number = int(value[:-2])
        logging.debug("Height Validator: {} {}".format(number, unit))
        if unit == "cm" and (150 <= number <= 193):
            return True
        elif unit == "in" and (59 <= number <= 76):
            return True
        else:
            return False
    else:
        return False

def is_passport_valid(passport, required_field_rules={}):
    logging.debug(passport)
    for key, validator in required_field_rules.items():
        if key not in passport:
            logging.debug("Did not find key: {}".format(key))
            return False

        if not validator(passport[key]):
            logging.debug("Failed validation rule for {}".format(key))
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

    required_field_rules = {
        "byr": (lambda v: 1920 <= int(v) <= 2002),
        "iyr": (lambda v: 2010 <= int(v) <= 2020),
        "eyr": (lambda v: 2020 <= int(v) <= 2030),
        "hgt": height_validator,
        "hcl": (lambda v: re.search("^#[0-9a-f]{6}$", v)),
        "ecl": (lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
        "pid": (lambda v: re.search("^[0-9]{9}$", v))
    }

    valid_passports = 0
    for passport in passports:
        if is_passport_valid(passport, required_field_rules):
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
