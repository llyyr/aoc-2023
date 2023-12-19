#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '19.txt'
inp = open(filename).read()

def parse():
    rules = {}
    parts = []
    rule_str, parts_str = inp.split('\n\n')
    for line in rule_str.splitlines():
        key, rule_str = line.strip('}').split('{')
        rules_list = []
        for rule in rule_str.split(','):
            if ':' not in rule:
                rules_list.append(list([rule]))
            else:
                rule, dest = rule.split(':')
                p, op, val = rule.partition('<' if '<' in rule else '>')
                rules_list.append((p, op, int(val), dest))
        rules[key] = rules_list

    for line in parts_str.splitlines():
        part = {}
        ps = line.strip('{}').split(',')
        for p in ps:
            key, val = p.split('=')
            part[key] = int(val)
        parts.append(part)
    return rules, parts

def part1():
    ans = 0
    for part in parts:
        flow = 'in'
        while True:
            for rule in workflows[flow]:
                if len(rule) == 1:
                    flow = rule[0]
                    break
                else:
                    p, op, val, dest = rule
                if {'<': int.__lt__, '>': int.__gt__}[op](part[p], val):
                    flow = dest
                    break
            if flow in 'AR':
                accept = flow == 'A'
                break
        if accept:
            ans += sum(part.values())
    return ans

def split_ranges(workflows, flow, ranges):
    res = {}
    for rule in workflows[flow]:
        if len(rule) == 1:
            if rule[0] in 'AR':
                res[ranges] = rule[0]
            else:
                res.update(split_ranges(workflows, rule[0], ranges))
            break
        else:
            p, op, val, dest = rule
        p_idx = 'xmas'.index(p)
        if op == '<':
            remap  = tuple((r1, r2) if i != p_idx else (r1, val - 1) for i, (r1, r2) in enumerate(ranges))
            ranges = tuple((r1, r2) if i != p_idx else (val, r2) for i, (r1, r2) in enumerate(ranges))
        else:
            remap  = tuple((r1, r2) if i != p_idx else (val + 1, r2) for i, (r1, r2) in enumerate(ranges))
            ranges = tuple((r1, r2) if i != p_idx else (r1, val) for i, (r1, r2) in enumerate(ranges))
        if dest in 'AR':
            res[remap] = dest
        else:
            res.update(split_ranges(workflows, dest, remap))
    return res

def part2():
    ranges = split_ranges(workflows, 'in', ((1, 4000),) * 4)
    ans = 0
    for rng, result in ranges.items():
        if result == 'A':
            ans += reduce(int.__mul__, [r2 - r1 + 1 for r1, r2 in rng])
    return ans

workflows, parts = parse()
print(part1(), part2())
