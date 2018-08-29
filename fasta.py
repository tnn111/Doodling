#!/usr/bin/env python

import itertools

def fasta_as_tuples(file):
    for defline, group in itertools.groupby(file, lambda x: x[0] == '>'):
        if defline:
            line = next(group)
            id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            if sequence[-1] == '*': yield (id, sequence[:-1])
            else: yield (id, sequence)


with open('Tara.faa') as fd:
    for key in fasta_as_tuples(fd):
        print(key[0], key[1])