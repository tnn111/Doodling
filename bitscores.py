#!/usr/bin/env python

import itertools

blosum62_scores = {'A': 4, 'R': 5, 'N': 6, 'D': 6, 'C': 9, 'Q': 5, 'E': 5, 'G': 6, 'H': 8, 'I': 4,
                   'L': 4, 'K': 5, 'M': 5, 'F': 6, 'P': 7, 'S': 4, 'T': 5, 'W': 11, 'Y': 7, 'V': 4,
                   'B': 4, 'J': 3, 'Z': 4, 'X': -1, '*': 1}

def fasta_as_tuples(file):

    """A generator function to go through a fasta formatted file and return each
       pair of defline/sequence as a tuple"""

    for defline, group in itertools.groupby(file, lambda x: x[0] == '>'):
        if defline:
            line = next(group)
            id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield (id, sequence)


with open('Tara.faa') as fd:
    for key in fasta_as_tuples(fd):
        raw_score = sum(blosum62_scores[key[1][i]] for i in range(len(key[1])))
        print(key[0], raw_score, sep = '\t')