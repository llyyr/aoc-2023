#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '05.txt'
seeds, *maps = open(filename).read().strip().split('\n\n')
seeds = [int(s) for s in seeds.split()[1:]]

def solve(part, seeds=seeds):
    if part == 1:
        seeds = [[seeds[i], seeds[i]] for i in range(len(seeds))]
    else:
        seeds = [[seeds[i], seeds[i] + seeds[i+1]] for i in range(0, len(seeds), 2)]
    for section in maps:
        lines = [tuple(map(int, line.split())) for line in section.split('\n')[1:]]
        lines.sort(key=lambda x: x[1])
        tmp = []
        while seeds:
            start, end = seeds.pop()
            for dst, src, length in lines:
                new_end = src + length
                offset = dst - src
                if src <= start < new_end:
                    tmp.append([start + offset, min(end, new_end) + offset])
                    if new_end > end:
                        break
                    start = new_end
            else:
                tmp.append([start, end])
        seeds = tmp
    return min(seeds, key=lambda x: x[0])[0]

print(solve(1), solve(2))

