#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '03.txt'
G = open(filename).read().splitlines()
C = len(G[0])
R = len(G)

def get_adjacents(r, c):
    out = set()
    for dr, dc in neighbours(r, c, 8):
        if dc < C and dr < R:
            out.add((dr, dc))
    return out

def solve():
    d = defaultdict(list)
    p1 = 0
    for r in range(R):
        c = 0
        while c < C:
            if not G[r][c].isdigit():
                c += 1
                continue
            adjacents = get_adjacents(r, c)
            num = G[r][c]
            for cc in range(c+1, C):
                if not G[r][cc].isdigit():
                    break
                num += G[r][cc]
                adjacents |= get_adjacents(r, cc)
                c += 1
            for dr, dc in adjacents:
                if G[dr][dc] == '*':
                    d[(dr, dc)].append(int(num))
            if any(G[dr][dc] not in '.0123456789' for dr, dc in adjacents):
                p1 += int(num)
            c += 1
    return p1, sum(math.prod(x) for x in d.values() if len(x) == 2)

print(*solve())
