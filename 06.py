#!/usr/bin/env python3

from aochelper import *

filename = sys.argv[1] if len(sys.argv) > 1 else '06.txt'
inp = open(filename).read().splitlines()
times, distances = [list(map(int, line.split()[1:])) for line in inp]

def solve(part, times=times, distances=distances):
    if part == 2:
        times = [int(''.join(map(str, times)))]
        distances = [int(''.join(map(str, distances)))]
    for time, distance in zip(times, distances):
        # Quadratic formula using only integer arithmetic
        # Let t = travel time, 
        #     T = race time, 
        #     B = button press duration, and
        #     D = travelled distance. Then,
        # (1) t = T - B
        # (2) D = t * B
        # Then combining (1) and (2):
        # D = (T - B) * B
        # => D = T*B - B^2;
        # => B^2 - T*B - D = 0
        # So, B = (T +/- sqrt(T^2 + 4D)) / 2
        # We can solve for B using purely integer arithmetic
        delta = math.isqrt(pow(time, 2) - 4 * distance - 1) + 1
        lo = (time - delta) // 2 + 1
        hi = abs((time + delta) // -2)
        yield hi - lo
        # Original bruteforce solution:
        # yield sum((time - speed) * speed > distance for speed in range(1, time))

print(math.prod(solve(1)), math.prod(solve(2)))
