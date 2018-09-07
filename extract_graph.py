#!/usr/bin/env python

import argparse

def extract_graph(base_file, bitscore_file):

    bitscores = {}
    with open(bitscore_file) as fd:
        for line in fd:
            fields = line.strip().split('\t')
            if len(fields) >= 2:
                bitscores[fields[0]] = int(fields[1])

    with open(base_file) as fd:
        for line in fd:
            line = line.strip().split('\t')
            bitscore1 = bitscores[line[0]]; bitscore2 = bitscores[line[1]]
            normalized_score = float(line[11])/max(bitscore1, bitscore2)
            print(line[0], line[1], '{0:.2f}'.format(normalized_score), sep = '\t')


if __name__ == '__main__':
    try:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("base", type = str, help = "the output of a LAST alignment run")
        arg_parser.add_argument("bitscores", type = str, help = "the bit scores")
        arguments = arg_parser.parse_args()

        extract_graph(arguments.base, arguments.bitscores)

    except (KeyboardInterrupt, BrokenPipeError):
        pass
