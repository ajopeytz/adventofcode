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
        if m[0] == "L":
            d -= int(m[1:])
        else:
            d += int(m[1:])
        d = d%100
        if d == 0:
            ans += 1
    return ans
