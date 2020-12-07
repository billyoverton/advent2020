#!/usr/bin/env python3
import sys
import logging
import re
import math
from timeit import default_timer as timer

import util

LOG_LEVEL = logging.INFO

def count_child_bags(bag, bag_graph):
    count = 0

    edges = bag_graph.vertices[bag]
    for edge in edges:
        logging.debug("{} bag must contain {} {} bags".format(bag, edge[1], edge[0]))
        count += edge[1] + (count_child_bags(edge[0], bag_graph) * edge[1])

    logging.debug("{} bags contain {} child bags".format(bag,count))
    return count


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

                    edge = (container, bag)
                    bag_graph.add_edge(edge, count, False)
    logging.debug("------------------------------------------------------------")

    logging.debug(bag_graph)
    number_of_bags = count_child_bags(source_bag, bag_graph)

    logging.info("Answer: Total number of bags {}".format(number_of_bags))

if __name__ == "__main__":

    logging.basicConfig(format='%(levelname)s:%(module)s: %(message)s', level=LOG_LEVEL)

    if len(sys.argv) < 2:
        logging.critical("Missing input file")
    else:
        start = timer()
        main(sys.argv[1])
        end = timer()

        logging.info(f'Executed in {(end-start):.5f} seconds')
