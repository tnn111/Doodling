#!/usr/bin/env python

import itertools

def hit_list(file):

    for id, list in itertools.groupby(file, lambda x: x.split()[0]):
        yield (id, list)

try:
    with open('sorted.tbl') as fd:
        for group in hit_list(fd):
            id = group[0]
            y = [x for x in group[1]]
            z0 = y[0].split()
            if len(y) == 2:
                z1 = y[1].split()
                if "UniRef100" in z1[1]:
                    z0, z1 = z1, z0
            else:
                if "UniRef100" in z0[1]:
                    z1 = ['', 'IMG_XXXXXXXXXXXXXXXXXXXXXXXXXXX', '0.00']
                else:
                    z1 = z0
                    z0 = ['', 'UniRef100_XXXXXXXXXX', '0.00']
            print(id, z0[1], z0[2], z1[1], z1[2], sep = '\t')
except (KeyboardInterrupt, BrokenPipeError):
    print('Interruption')