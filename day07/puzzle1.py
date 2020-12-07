#!/usr/bin/env python3
import sys
import logging
import re
import math
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def main(input_file):

    bag_graph = util.Graph()
    source_bag = "shiny gold"
    bag_regex = re.compile('^([0-9]+) (.*) bag(s)?$')

    with open(input_file) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            container, content_list = line.split(" contain ")

            # Strip the bags off the container for consistency
            container = container[:-5]

            logging.debug("Looking at rule for container bag: {}".format(container))
            logging.debug(content_list)

            if content_list == "no other bags.":
                # This is a ending bag which can contain no other bags
                bag_graph.add_vertex(container)
            else:
                content_list = content_list[:-1] # strip  the period at the end
                content_bag_strings = content_list.split(',')

                for bag_type in content_bag_strings:
                    match = bag_regex.match(bag_type.strip())
                    count = int(match.group(1))
                    bag = match.group(2)
                    logging.debug("\tCan contain {} {}".format(count, bag))

                    edge = (bag, container)
                    bag_graph.add_edge(edge, count, False)

    distances, previous_bags = bag_graph.dijkstra(source_bag)
    logging.debug(distances)

    containing_count = 0
    for bag, distance in distances.items():
        if distance != math.inf and distance != 0:
            # this is a bag that can contain our source bag but isn't our source
            containing_count += 1

    logging.info("Answer: Containing bag count {}".format(containing_count))

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
