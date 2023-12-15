#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '15.txt'
inp = open(filename).read().strip()

def make_hash(op):
    cur = 0
    for c in op.encode():
        cur = 0xff & ((cur + c)*17)
    return cur

def solve():
    p1 = p2 = 0
    hashmap = defaultdict(dict)
    for op in inp.split(','):
        if '=' in op:
            label, value = op.split('=')
            hashmap[make_hash(label)][label] = int(value)
        else:
            label = op[:-1]
            hashmap[make_hash(label)].pop(label, None)
        p1 += make_hash(op)
    for h, box in hashmap.items():
        for k, v in enumerate(box.values()):
            p2 += (h+1) * (k+1) * v
    print(p1, p2)

solve()
