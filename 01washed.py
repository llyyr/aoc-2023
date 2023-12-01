inp = open('01.txt').read().splitlines()
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def p1(inp):
    d = [c for c in inp if c.isdigit()]
    return int(d[0] + d[-1])

def p2(inp):
    for i, n in enumerate(words, 1):
        inp = inp.replace(n, n[0] + str(i) + n[-1])
    return p1(inp)

print(sum(map(p1, inp)), sum(map(p2, inp)))
