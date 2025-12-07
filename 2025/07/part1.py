# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [line.strip() for line in f.readlines()]
    ans = 0
    beams = [s[0].find('S')]
    debug = [s[0]]
    for l in s[1:]:
        d = list(l)
        new_beams = []
        for b in beams:
            if d[b] == ".":
                d[b] = "|"
                new_beams.append(b)
            if l[b] == "^":
                if (b+1) < len(l) and l[b+1] != "^":
                    new_beams.append(b+1)
                    d[b+1] = "|"
                if (b-1) >= 0 and l[b-1] != "^":
                    d[b-1] = "|"
                    new_beams.append(b-1)
                ans += 1
        beams = new_beams
        debug.append(d)


    return ans
