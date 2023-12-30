#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '17.txt'
G = [list(map(int, l)) for l in open(filename).read().splitlines()]
R, C = len(G), len(G[0])

def solve(min_steps, max_steps):
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    Q = [(0, ((0, 0), 0, 0)), (0, ((0, 0), 1, 0))]
    seen = set(Q)
    while Q:
        dist, state = heapq.heappop(Q)
        (r, c), dir, in_dir = state
        if r == R - 1 and c == C - 1:
            return dist
        dirs = []
        if in_dir >= min_steps:
            dirs.extend([(dir + 1) % 4, (dir + 3) % 4])
        if in_dir <= max_steps:
            dirs.append(dir)
        for new_dir in dirs:
            dr, dc = DIRS[new_dir]
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C:
                new_in_dir = in_dir + 1 if dir == new_dir else 1
                new_dist = dist + G[rr][cc]
                new_state = ((rr, cc), new_dir, new_in_dir)
                if new_state not in seen:
                    heapq.heappush(Q, (new_dist, new_state))
                    seen.add(new_state)

print(solve(0, 2), solve(4, 9))
