# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

cache = dict()

def count_solutions(m,beams):
    if str((m,beams)) in cache.keys():
        return cache[str((m,beams))]
    if len(m)>0:
        l = m[0]
        c = 0
        for b in beams:
            if l[b] == "^":
                if (b+1) < len(l) and l[b+1] != "^":
                    new_beams = beams.copy()
                    new_beams.remove(b)
                    new_beams.append(b+1)
                    c += count_solutions(m[1:],new_beams)
                if (b-1) >= 0 and l[b-1] != "^":
                    new_beams = beams.copy()
                    new_beams.remove(b)
                    new_beams.append(b-1)
                    c += count_solutions(m[1:],new_beams)
            else:
                c += count_solutions(m[1:],beams)
    else:
        c = len(beams)

    cache[str((m,beams))] = c
    return c



# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [line.strip() for line in f.readlines()]
    ans = 0
    beams = [s[0].find('S')]
    ans = count_solutions(s[1:],beams)
    return ans
