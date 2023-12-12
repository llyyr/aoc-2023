#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '12.txt'
inp = list(map(str.split, open(filename)))


def solve(copies):
    for line, counts in inp:
        counts = tuple(map(int, counts.split(','))) * copies
        line = "?".join(line for _ in range(copies))

        @cache
        def process_line(line_pos, count_pos, r=0):
            max_line = len(line)
            max_counts = len(counts)
            if line_pos == max_line:
                return count_pos == max_counts
            if line[line_pos] in ".?":
                r += process_line(line_pos + 1, count_pos)
            if line[line_pos] in "#?":
                if count_pos < max_counts:
                    nxt = line_pos + counts[count_pos]
                    if nxt <= max_line and "." not in line[line_pos:nxt]:
                        next_pos = min(nxt + 1, max_line)
                        if nxt == max_line or line[next_pos - 1] != "#":
                            r += process_line(next_pos, count_pos + 1)
            return r

        yield process_line(0, 0)

print(sum(solve(1)), sum(solve(5)))
