# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [line.strip() for line in f.readlines()]
    d = 50
    ans = 0
    for m in s:
        p = d
        if m[0] == "L":
            o = -1
        else:
            o = 1
        r = range(0,int(m[1:]))
        for m in r:
            d += o
            if (d%100)==0:
                ans += 1
                d = 0

    return ans
