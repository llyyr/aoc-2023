#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '09.txt'
inp = [list(map(int, line.split())) for line in open(filename)]

def solve(line):
    last = line[-1]
    while any(line):
        line = list(map(operator.sub, line[1:], line))
        last += line[-1]
    return last

print(sum(solve(line) for line in inp), sum(solve(line[::-1]) for line in inp))
