#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '04.txt'
inp = open(filename).readlines()

def solve():
    score = 0
    copies = [1] * len(inp)

    for i, line in enumerate(inp, 1):
        winning, scratch = map(str.split, line.split(': ')[-1].split(' | '))
        c = len(set(winning) & set(scratch))
        if c > 0:
            score += pow(2, c-1)
        for j in range(c):
            copies[i+j] += copies[i-1]
    return score, sum(copies)

print(*solve())
