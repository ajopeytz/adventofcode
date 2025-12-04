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
    for b in s:
        l = [int(e) for e in list(b)]
        m = max(l[:-1])
        i = b.find(str(m))
        m2 = max(l[i+1:])
        ans += m*10 + m2


    return ans
