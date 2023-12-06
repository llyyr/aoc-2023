#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '02.txt'
inp = open(filename).read().splitlines()

def solve(inp):
    target = {'red': 12, 'green': 13, 'blue': 14}
    p1 = p2 = 0
    for line in inp:
        vals = {'red': 0, 'green': 0, 'blue': 0}
        id = line.split(': ')[0].split(' ')[-1]
        subsets = line.split(': ')[1].split('; ')
        game = [subset.split(', ') for subset in subsets]
        ok = True
        for subset in game:
            for cube in subset:
                n, color = cube.split()
                n = int(n)
                vals[color] = max(vals[color], n)
                if n > target[color]:
                    ok = False
        if ok:
            p1 += int(id)
        p2 += math.prod(vals.values())

    return p1, p2

print(*solve(inp))
