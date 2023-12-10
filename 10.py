#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '10.txt'
N, S, E, W  = DIRS
joints = {'|': (N, S), '-': (W, E), 'L': (N, E),
          'J': (N, W), 'F': (E, S), '7': (W, S), 'S': 'S', '.': ()}
G = [[joints[c] for c in l.strip()] for l in open(filename)]
R, C = len(G), len(G[0])

def solve():
    sr, sc = next((r, l.index('S')) for r, l in enumerate(G) if 'S' in l)
    Q = []
    seen = {(sr, sc)}
    for dr, dc in DIRS:
        if (dr, dc) in G[sr + dr][sc + dc]:
            Q.append(((sr + dr, sc + dc), 1))
            seen.add((sr + dr, sc + dc))

    while Q:
        (r, c), cost = Q.pop()
        for dr, dc in G[r][c]:
            pos = (r + dr, c + dc)
            if pos not in seen:
                Q.append((pos, cost + 1))
                seen.add(pos)
    ret = 0
    down = {(N, S), (E, S), (W, S), 'S'}
    for r, l in enumerate(G):
        inside = False
        for c, ch in enumerate(l):
            if ch in down and (r, c) in seen:
                inside = not inside
            if inside and (r, c) not in seen:
                ret += 1
    return len(seen) // 2, ret

print(*solve())
