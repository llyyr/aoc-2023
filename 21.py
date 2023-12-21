#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '21.txt'
G = open(filename).read().splitlines()
R, C = len(G), len(G[0])
sr, sc = next((r, l.index('S')) for r, l in enumerate(G) if 'S' in l)

def solve():
    queue = []
    queue.append((sr, sc, 0))
    seen = set()
    possible = defaultdict(set)
    while queue:
        r, c, step = queue.pop()
        if (r, c, step) in seen:
            continue
        seen.add((r, c, step))
        if G[r % R][c % C] in '.S':
            possible[step].add((r, c))
        else:
            continue
        if step == C * 2 + sc:
            continue
        for dr, dc in DIRS:
            queue.append((r+dr, c+dc, step+1))

    steps = C * 2 + sc
    score = len(possible[steps])
    increment = len(possible[steps]) - len(possible[steps - C])
    amount = increment - (len(possible[steps - C]) - len(possible[sc]))
    while steps != C * 202300 + sc:
        increment += amount
        score += increment
        steps += C
    return len(possible[64]), score
print(*solve())
