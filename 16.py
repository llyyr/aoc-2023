#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '16.txt'
inp = open(filename).read().splitlines()
R, C = len(inp), len(inp[0])

TILES = {
    '.': {'N': 'N', 'W': 'W', 'S': 'S', 'E': 'E'},
    '/': {'N': 'E', 'W': 'S', 'S': 'W', 'E': 'N'},
    '\\': {'N': 'W', 'W': 'N', 'S': 'E', 'E': 'S'},
    '-': {'N': 'EW', 'W': 'W', 'S': 'EW', 'E': 'E'},
    '|': {'N': 'N', 'W': 'NS', 'S': 'S', 'E': 'NS'}
}

DIRMAP = {'N': (1, 0), 'W': (0, 1), 'S': (-1, 0), 'E': (0, -1)}

def part1(inp, r, c, start):
    stack = [(r, c, start)]
    seen = defaultdict(set)
    seen[(r, c)].add(start)
    while stack:
        r, c, dir = stack.pop()
        for dir in TILES[inp[r][c]][dir]:
            rr, cc = r + DIRMAP[dir][0], c + DIRMAP[dir][1]
            if 0 <= rr < R and 0 <= cc < C and dir not in seen[(rr, cc)]:
                seen[(rr, cc)].add(dir)
                stack.append((rr, cc, dir))
    return len(seen)

def part2():
    ret = 0
    for r in range(R):
        ret = max(max(part1(inp, r, 0, 'W'), part1(inp, r, C-1, 'E')), ret)
    for c in range(C):
        ret = max(max(part1(inp, 0, c, 'N'), part1(inp, R-1, c, 'S')), ret)
    return ret

print(part1(inp, 0, 0, 'W'), part2())
