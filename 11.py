#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '11.txt'
inp = open(filename).read().splitlines()
coords = hash2coords(inp)
empty_rows = {i for i, l in enumerate(inp) if '#' not in l}
empty_cols = {i for i in range(len(inp[0])) if '#' not in {c[i] for c in inp}}

def solve():
    p1, p2 = 0, 0
    for (r, c), (rr, cc) in combinations(coords, 2):
        min_r, max_r = min(r, rr), max(r, rr)
        min_c, max_c = min(c, cc), max(c, cc)
        dist = abs(max_r - min_r) + abs(max_c - min_c)
        p1 += dist
        p2 += dist
        for r in empty_rows:
            if min_r < r < max_r:
                p1 += 2 - 1
                p2 += 1000000 - 1
        for c in empty_cols:
            if min_c < c < max_c:
                p1 += 2 - 1
                p2 += 1000000 - 1

    return p1, p2

print(*solve())
