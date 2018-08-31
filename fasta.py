#!/usr/bin/env python

import itertools
import math

def hit_list(file):

    for id, list in itertools.groupby(file, lambda x: x[0]):
        yield (id, list)


with open('sorted.tbl') as fd:
    for key in hit_list(fd):
        print(key)