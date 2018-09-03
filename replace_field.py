#!/usr/bin/env python

import argparse

def replace_field(base, field, replacement):

    replacements = {}
    with open(replacement) as fd:
        for line in fd:
            fields = line.split()
            if len(fields) >= 2:
                replacements[fields[0]] = str(fields[1])

    with open(base) as fd:
        for line in fd:
            line = line.strip().split()
            print(*line[0:field], line[field], replacements.get(line[field]), *line[field + 1:], sep = '\t')


if __name__ == '__main__':
    try:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("base", type = str, help = "the input file to be modified")
        arg_parser.add_argument("field", type = int, help = "the field to be modified; 0-based")
        arg_parser.add_argument("replacement", type = str, help = "the file containing the modifications")
        arguments = arg_parser.parse_args()

        replace_field(arguments.base, arguments.field, arguments.replacement)

    except (KeyboardInterrupt, BrokenPipeError):
        pass
