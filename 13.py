#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '13.txt'
inp = open(filename).read().split('\n\n')
grids = [[row for row in grid.split('\n') if row] for grid in inp]

def horizontal_value(grid, req):
    res = 0
    for i in range(len(grid) - 1):
        total = 0
        for r1, r2 in zip(grid[i+1:], grid[i::-1]):
            total += sum(0 if c1 == c2 else 1 for (c1, c2) in zip(r1, r2))
        if total == req:
            res += i + 1
    return res

p1 = p2 = 0
for grid in grids:
    p1 += horizontal_value(grid, 0) * 100 + horizontal_value(list(zip(*grid)), 0)
    p2 += horizontal_value(grid, 1) * 100 + horizontal_value(list(zip(*grid)), 1)
print(p1, p2)


