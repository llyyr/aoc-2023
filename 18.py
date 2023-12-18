#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '18.txt'
inp = open(filename).read().splitlines()

def solve(part):
    edges = []
    perim, x, y = 0, 0, 0
    for line in inp:
        d, n, color = line.split()
        color = color.strip('()#')
        n = int(n) if part == 1 else int(color[:-1], 16)
        dx, dy = DIRMAP[d] if part == 1 else (RIGHT, DOWN, LEFT, UP)[int(color[-1])]
        perim += n
        x += n * dx
        y += n * dy
        edges.append((x, y))
    shoelace = abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in pairwise(edges))) // 2
    return shoelace + (perim // 2) + 1

print(solve(1), solve(2))
