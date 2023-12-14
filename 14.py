#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '14.txt'
G = [list(l) for l in open(filename).read().splitlines()]
R, C = len(G), len(G[0])

def p1():
    total = 0
    for c in range(C):
        weight = R
        for r in range(R):
            if G[r][c] == '#':
                weight = R - r - 1
            elif G[r][c] == 'O':
                total += weight
                weight -= 1
    return total

def roll():
    for r in range(1, R):
        for c in range(C):
            if G[r][c] == 'O' and G[r-1][c] == '.':
                rr = r - 1
                while rr > 0 and G[rr-1][c] == '.':
                    rr -= 1
                G[rr][c], G[r][c] = 'O', '.'
    for c in range(1, C):
        for r in range(R):
            if G[r][c] == 'O' and G[r][c-1] == '.':
                cc = c - 1
                while cc > 0 and G[r][cc-1] == '.':
                    cc -= 1
                G[r][cc], G[r][c] = 'O', '.'
    for r in range(R-2, -1, -1):
        for c in range(C):
            if G[r][c] == 'O' and G[r+1][c] == '.':
                rr = r + 1
                while rr < R -1 and G[rr+1][c] == '.':
                    rr += 1
                G[rr][c], G[r][c] = 'O', '.'
    for c in range(C-2, -1, -1):
        for r in range(R):
            if G[r][c] == 'O' and G[r][c+1] == '.':
                cc = c + 1
                while cc < C -1 and G[r][cc+1] == '.':
                    cc += 1
                G[r][cc], G[r][c] = 'O', '.'

def p2():
    seen = []
    target = 10**9
    while len(seen) != target:
        state = ([''.join(l) for l in G],)
        if state in seen:
            start = seen.index(state)
            length = len(seen) - start
            target = ((target - start) % length) + start + length
        roll()
        seen.append(state)

    return sum((r + 1) * l.count('O') for r, l in enumerate(G[::-1]))

print(p1())
print(p2())
