#!/usr/bin/env python3

from aochelper import *
import numpy as np

filename = sys.argv[1] if len(sys.argv) > 1 else '24.txt'
inp = open(filename).read().splitlines()
eqs = []
hails = []
for line in inp:
    px, py, pz, vx, vy, vz = py_ints(line)
    slope = vy / vx
    intercept = py - (px * slope)
    hails.append(((px, py, pz), (vx, vy, vz)))
    eqs.append([slope, intercept, px, vx > 0])

def part1():
    range_min = 200000000000000
    range_max = 400000000000000
    ret = 0
    for (slope1, intercept1, px1, vx1), (slope2, intercept2, px2, vx2) in combinations(eqs, 2):
        if slope1 == slope2:
            continue
        interceptX = (intercept2 - intercept1) / (slope1 - slope2)
        if any((interceptX < px) if vx else (interceptX > px)
                for px, vx in ((px1, vx1), (px2, vx2))):
            continue
        interceptY = (slope1 * interceptX) + intercept1
        if all(range_min <= v <= range_max for v in (interceptX, interceptY)):
            ret += 1
    return ret

def part2_z3():
    from z3 import Real, Solver, sat
    p = [Real(f'p{i}') for i in range(3)]
    v = [Real(f'v{i}') for i in range(3)]
    s = Solver()
    for i, ((px, py, pz), (vx, vy, vz)) in enumerate(hails[:3]):
        ti = Real(f"t{i}")
        s.add(ti > 0)
        s.add(p[0] + ti * v[0] == px + ti * vx)
        s.add(p[1] + ti * v[1] == py + ti * vy)
        s.add(p[2] + ti * v[2] == pz + ti * vz)
    assert s.check() == sat
    return sum(s.model()[v].as_long() for v in p) # type: ignore

# https://stackoverflow.com/questions/563198/how-do-you-detect-where-two-line-segments-intersect
# (p - q) x (r - s) = 0 because t == u.
# we have 6 equations for 6 unknowns
# Pick the largest 3 because otherwise the answer might be off by one or two

def part2():
    largest_3 = heapq.nlargest(3, hails, key=lambda item: reduce(operator.add, item[0]))
    (px, vx), (py, vy), (pz, vz) = [(np.array(s1), np.array(s2)) for s1, s2 in largest_3]
    unknowns = np.append(
        np.cross(-px, vx) + np.cross(py, vy),
        np.cross(-px, vx) + np.cross(pz, vz)
    )
    skew = lambda arr: np.cross(np.eye(3), arr)
    matrix = np.block([
        [skew(vx - vy), skew(px - py)], 
        [skew(vx - vz), skew(px - pz)]
    ])
    return round(np.linalg.solve(matrix, unknowns)[:3].sum())

print(part1())
# print(part2_z3())
print(part2())
