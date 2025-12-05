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
    fresh = []
    ranges = True
    for l in s:
        if l == "":
            ranges = False
            continue
        if ranges:
            p = l.split("-")
            print(range(int(p[0]),int(p[1])+1))
            fresh.append(range(int(p[0]),int(p[1])+1))
        else:
            for r in fresh:
                if int(l) in r:
                    ans += 1
                    break

    return ans
