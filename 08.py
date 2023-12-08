#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '08.txt'
inp = open(filename).read().splitlines()

def solve(part):
    steps = list(map(int, list(inp[0].replace('L', '0').replace('R', '1'))))
    graph = {}
    for line in inp[2:]:
        node, eles = line.split(' = ')
        graph[node] = tuple(eles.strip('( )').split(', '))
    starts = [k for k in graph.keys() if k.endswith('A')] if part == 2 else ['AAA']
    cycles = []
    for cur in starts:
        i = 0
        while not cur.endswith('Z'):
            cur = graph[cur][steps[i % len(steps)]]
            i += 1
        cycles.append(i)
    return math.lcm(*cycles)

print(solve(1), solve(2))
