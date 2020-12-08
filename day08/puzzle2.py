#!/usr/bin/env python3
import sys
import logging
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.DEBUG

def reset_program(program):
    for instruction in program:
        instruction[2] = False

def run_program(program):
    reset_program(program)
    accumulator = 0
    ip = 0
    programLoops = True
    while True:
        if ip >= len(program):
            # The program finished
            programLoops = False
            break

        instruction = program[ip]

        if instruction[2] == True:
            programLoops = True
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

    return programLoops, accumulator

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

    programLoops, accumulator = True, 0
    last_flipped_instruction = 0

    while programLoops:

        to_flip = last_flipped_instruction
        flipped = False

        instruction = program[to_flip]
        if instruction[0] == "nop":
            flipped = True
            instruction[0] = "jmp"
        elif instruction[0] == "jmp":
            flipped = True
            instruction[0] = "nop"

        if flipped:
            logging.debug("Flipped instruction {} to {}".format(to_flip, instruction[0]))
            programLoops, accumulator = run_program(program)

            if not programLoops:
                logging.debug("Program Finished Successfully")

            # Flip the instruction back
            instruction[0] = "nop" if instruction[0] == "jmp" else "jmp"
        else:
            logging.debug("Ignoring instruction {}".format(to_flip))

        last_flipped_instruction = to_flip + 1

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
