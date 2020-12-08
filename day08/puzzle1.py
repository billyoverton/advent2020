#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def main(input_file):

    program = []

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            parts = line.split(" ")
            program.append([parts[0], int(parts[1]), False])
    logging.debug(program)

    accumulator = 0
    ip = 0

    while True:
        instruction = program[ip]
        logging.debug("Running instruction: {} Value: {} Seen: {}".format(instruction[0], instruction[1], instruction[2]))
        if instruction[2] == True:
            # We have returned to an instruction. Infinite loop found
            break
        elif instruction[0] == "jmp":
            ip += instruction[1]
        elif instruction[0] == "acc":
            accumulator += instruction[1]
            ip += 1
        elif instruction[0] == "nop":
            ip += 1
        else:
            logging.error("Unknown operation")
            sys.exit(1)

        instruction[2] = True # Flag the command as seen before

    logging.info("Answer: Accumulator Value {}".format(accumulator))

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
