#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '10.txt'
N, S, E, W  = map(tuple, DIRS)
joints = {'|': {N, S}, '-': {W, E}, 'L': {N, E},
          'J': {N, W}, 'F': {E, S}, '7': {W, S}, 'S': 'S', '.': {}}
G = [[joints[c] for c in l.strip()] for l in open(filename)]

def solve():
    sr, sc = next((r, l.index('S')) for r, l in enumerate(G) if 'S' in l)
    G2 = {(dr, dc) for (dr, dc) in DIRS if (dr, dc) in G[sr + dr][sc + dc]}
    path = {(sr, sc)}
    er, ec = G2.pop()
    dr, dc = (G2 - {(er, ec)}).pop()
    r, c = sr, sc
    while (r := r + dr, c := c + dc) != (sr, sc):
        path.add((r, c))
        dr, dc = (G[r][c] - {(-dr, -dc)}).pop()

    ret = 0
    for r, l in enumerate(G):
        inside = set()
        for c, ch in enumerate(l):
            if (r, c) in path:
                inside = inside ^ set(ch)
            elif inside >= {N, S}:
                ret += 1
    return len(path) // 2, ret

print(*solve())
