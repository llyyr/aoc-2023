#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '20.txt'
inp = open(filename).read().splitlines()

def part1():
    G = {}
    mod_type = {}
    types = {}
    for line in inp:
        lhs, rhs = line.split(' -> ')
        lhs = lhs.strip('%&')
        G[lhs] = rhs.split(', ')
        mod_type[lhs] = line[0]

    for name, t in mod_type.items():
        if t == '%':
            types[name] = 0
        elif t == '&':
            types[name] = {src: 0 for src, dsts in G.items() if name in dsts}

    press, lo, hi = 0, 0, 0
    while press < 1000:
        press += 1
        lo += 1
        Q = deque()
        for ff in G['broadcaster']:
            Q.append((ff, 'broadcast', 0))
            lo += 1
        while Q:
            name, src, pulse_in = Q.popleft()
            if name not in mod_type:
                continue
            match mod_type[name], pulse_in:
                case '', _:
                    pulse_out = pulse_in
                case '%', 0:
                    pulse_out = types[name] = not types[name]
                case '&', _:
                    types[name][src] = pulse_in
                    pulse_out = not all(types[name].values())
                case _: continue
            if pulse_out:
                hi += len(G[name])
            else:
                lo += len(G[name])
            for dst in G[name]:
                Q.append((dst, name, pulse_out))
    return lo * hi

def part2():
    G = {}
    for line in inp:
        lhs, rhs = line.split(' -> ')
        G[lhs] = rhs.split(', ')
    res = []
    for ff in G['broadcaster']:
        bin = ''
        while True:
            bin += '1' if any('%'+g not in G for g in G['%'+ff]) else '0'
            next_ff = [dst for dst in G['%'+ff] if '%'+dst in G]
            if not next_ff:
                break
            ff = next_ff[0]
        res.append(int(bin[::-1], 2))
    return math.lcm(*res)

print(part1(), part2())
