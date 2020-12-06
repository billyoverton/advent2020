#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def main(input_file):

    groups = []

    with open(input_file) as f:
        previous_blank = True
        group = None # A dictionary of question -> count of yes answers
        people_count = 0
        while True:
            line = f.readline().strip()

            if not line and previous_blank:
                break
            elif not line:
                previous_blank = True
                group_struct = {}
                group_struct["people"] = people_count
                group_struct["yes_answers"] = group
                groups.append(group_struct) # Add the passport record we last encounterd
                continue

            if previous_blank:
                logging.debug("Starting a new group")
                group = {}
                people_count = 0

            person_yes_answers = {x for x in line} # uses a set because a double answer doesn't count more than once

            for yes in person_yes_answers:
                if yes in group:
                    group[yes] = group[yes] + 1
                else:
                    group[yes] = 1

            people_count += 1
            previous_blank = False

    logging.debug(groups)

    sum_of_counts = 0
    for group in groups:
        count = 0
        for question, yes_count in group["yes_answers"].items():
            if yes_count == group["people"]:
                count += 1
        sum_of_counts += count


    logging.info("Answer: Sum of Yes Answers: {}".format(sum_of_counts))
if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
