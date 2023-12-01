#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else sys.argv[0].replace('py', 'txt')
inp = open(filename).read().splitlines()
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def solve(part2=False):
    ans = 0
    for line in inp:
        digit = ''
        for i in range(len(line)):
            if not ('0' <= line[i] <= '9'):
                if not part2: continue
                for j, num in enumerate(words):
                    if line[i:].startswith(num):
                        digit += str(j+1)
            else:
                digit += line[i]
        if digit:
            ans += int(digit[0] + digit[-1])
    return ans

print(solve(), solve(True))
