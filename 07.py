#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '07.txt'
inp = {h: int(b) for h, b in [l.split() for l in open(filename).read().splitlines()]}

def p1(hand):
    match sorted(Counter(hand).values()):
        case [5]: return 10
        case [1, 4]: return 9
        case [2, 3]: return 8
        case [1, 1, 3]: return 7
        case [1, 2, 2]: return 6
        case [1, 1, 1, 2]: return 5
        case _: return 4

def p2(hand):
    if hand == 'JJJJJ':
        return p1(hand)
    joker = max(set(hand.replace('J', '')), key=hand.count)
    return p1(hand.replace('J', joker))

def solve(part):
    cards = ('AKQJT98765432', 'AKQT98765432J')[part-1][::-1]
    sorter = lambda h: ((p1, p2)[part-1](h), [cards.index(c) for c in h])
    ans = sorted(inp, key=sorter)
    return sum(i*inp[k] for i, k in enumerate(ans, 1))

print(solve(1), solve(2))

