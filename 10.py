#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '10.txt'
inp = open(filename).read().splitlines()

NORTH, SOUTH, EAST, WEST  = map(tuple, DIRS)
joints = {
    'S': 'S',
    '.': {},
    '|': {NORTH, SOUTH},
    '-': {WEST, EAST},
    'L': {NORTH, EAST},
    'J': {NORTH, WEST},
    'F': {EAST, SOUTH},
    '7': {WEST, SOUTH},
}
G = [[joints[c] for c in l.strip()] for l in inp]
R, C = len(G), len(G[0])
sr, sc = next((r, c) for r, l in enumerate(G) for c, ch in enumerate(l) if ch == 'S')
G2 = set()
for add, (c_r, c_c) in ((EAST, WEST), (WEST, EAST), (SOUTH, NORTH), (NORTH, SOUTH)): 
    if (c_r, c_c) in G[sr + c_r][sc + c_c]:
        G2.add(add)

def solve():
    path = set((sr, sc))
    er, ec = G2.pop()
    dr, dc = (G2 - {(er, ec)}).pop()
    r, c = sr + dr, sc + dc
    while (r, c) != (sr, sc):
        path |= {(r, c)}
        dr, dc = (G[r][c] - {(-dr, -dc)}).pop()
        r, c = r + dr, c + dc
    assert (dr, dc) == (er, ec)

    ret = 0
    for r, l in enumerate(G):
        inside = set()
        for c, ch in enumerate(l):
            if (r, c) in path:
                inside = inside ^ set(ch)
            elif inside >= {NORTH, SOUTH}:
                ret += 1
    return len(path) // 2, ret

print(*solve())
