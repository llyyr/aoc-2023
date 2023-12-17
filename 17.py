#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '17.txt'
G = [list(map(int, l)) for l in open(filename).read().splitlines()]
R, C = len(G), len(G[0])

def solve(part):
    DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    Q = [(0, ((0, 0), 0, 0)), (0, ((0, 0), 1, 0))]
    seen = set()
    while Q:
        dist, state = heapq.heappop(Q)
        if state in seen:
            continue
        (r, c), dir, in_dir = state
        if r == R-1 and c == C-1:
            return dist
        dirs = []
        if (in_dir <= 2 and part == 1) or (in_dir <= 9 and part == 2):
            dirs.append(dir)
        if part == 1 or (in_dir >= 4 and part == 2):
            dirs.extend([(dir + 1) % 4, (dir + 3) % 4])
        for new_dir in dirs:
            dr, dc = DIRS[new_dir]
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C:
                new_in_dir = in_dir + 1 if dir == new_dir else 1
                new_dist = dist + G[rr][cc]
                heapq.heappush(Q, (new_dist, ((rr, cc), new_dir, new_in_dir)))
        seen.add(state)

print(solve(1), solve(2))
