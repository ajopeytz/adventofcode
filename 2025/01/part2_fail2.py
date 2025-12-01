# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [line.strip() for line in f.readlines()]
    print(s)
    d = 50
    ans = 0
    for m in s:
        if m[0] == "L":
            c = -int(m[1:])
        else:
            c = int(m[1:])
        r = d+c    
        d = r%100
        print('d',d,'c',c,'r',r)
        ans += abs(r)//100
        if r<0:
            ans += 1
        print(ans)


    return ans
