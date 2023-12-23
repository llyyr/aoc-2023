#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '23.txt'
G = open(filename).read().splitlines()
R, C = len(G), len(G[0])
DIRMAP = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}
start = (0, 1)
end = (R - 1, C - 2)

def solve():
    sections = set()
    for r in range(R - 1):
        for c in range(C - 1):
            if G[r][c] == '.' and sum(G[r + dr][c + dc] == '#' for (dr, dc) in DIRS) < 2:
                sections.add((r, c))
    sections.update({start, end})

    Q = [(0, start, start)]
    seen = set()
    edges = {}
    rev_edges = {}
    while Q:
        steps, (r, c), (pr, pc) = Q.pop()
        if (r, c) != (pr, pc) and (r, c) in sections:
            Q += [(0, (r, c), (r, c))]
            edges.setdefault((pr, pc), set()).add(((r, c), steps))
            rev_edges.setdefault((r, c), set()).add(((pr, pc), steps))
        else:
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                if not (0 <= rr < R and 0 <= cc < C) or G[rr][cc] == '#':
                    continue
                if G[rr][cc] in DIRMAP and (dr, dc) != DIRMAP[G[rr][cc]]:
                    continue
                if (rr, cc) in sections or (rr, cc) not in seen:
                    seen.add((rr, cc))
                    Q += [(steps + 1, (rr, cc), (pr, pc))]

    def calc_max(p2):
        Q = [(0, start, {start})]
        ret = 0
        while Q:
            steps, (r, c), path = Q.pop()
            if (r, c) == end:
                ret = max(steps, ret)
            else:
                adjs = edges.get((r, c), set())
                if p2:
                    adjs.update(rev_edges.get((r, c), set()))
                for adj, weight in adjs:
                    if adj not in path:
                        Q.append((steps + weight, adj, path.union({adj})))
        return ret

    print(calc_max(False))
    print(calc_max(True))

solve()
