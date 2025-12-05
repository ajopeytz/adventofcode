# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

def reduce_ranges(r,ranges):
    if len(ranges) == 0:
        return [r]
    fresh = []
    overlap = False
    for x in ranges:
        o = range(max(r[0],x[0]),min(r[1],x[1])+1)
        if len(o) > 0 and not overlap:
            overlap = True
            fresh.append([min(r[0],x[0]),max(r[1],x[1])])
        else:
            fresh.append(x)
    if not overlap:
        return [r] + reduce_ranges(fresh[0],fresh[1:])
    else:
        return reduce_ranges(fresh[0],fresh[1:])
# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [line.strip() for line in f.readlines()]
    ans = 0
    fresh = []
    ranges = True
    ids = []
    for l in s:
        if l == "":
            ranges = False
            break
        p = l.split("-")
        fresh.append([int(p[0]),int(p[1])])

    f = reduce_ranges(fresh[0],fresh[1:])
    for r in f:
        ans += len(range(r[0],r[1]+1))

    return ans
