#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '22.txt'
inp = open(filename)

def drop(settled, brick):
    while True:
        step = {(x, y, z - 1) for x, y, z in brick}
        if any(z == 0 for _, _, z in step) or step & settled:
            return brick
        brick = step

def solve():
    bricks = []
    for l in inp:
        a, b = [list(map(int, r.split(','))) for r in l.split('~')]
        ranges = [range(x, y + 1) if x < y else range(y, x + 1) for x, y in zip(a, b)]
        bricks.append(set(product(*ranges)))
    bricks.sort(key=lambda p: min(p, key=lambda x: x[2])[2])

    settled = set()
    for i, b in enumerate(bricks):
        b = drop(settled, b)
        bricks[i] = b
        settled |= b

    p1, p2 = 0, 0
    for b1 in bricks:
        safe = True
        settled -= b1
        for b2 in bricks:
            if b1 == b2:
                continue
            settled -= b2
            if drop(settled, b2) != b2:
                p2 += 1
                safe = False
            else:
                settled |= b2
        p1 += safe
    return p1, p2

print(*solve())
