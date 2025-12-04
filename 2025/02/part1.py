# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        l = [line.strip() for line in f.readlines()]
        s = []
        for r in l[0].split(","):
            s.append(r)
    print(s)

    ans = 0
    for r in s:
        pt = r.split('-')
        print(r)
        for n in range(int(pt[0]),int(pt[1])+1):
            x = str(n)
            if len(x)%2 == 0 and x[:len(x)//2] == x[len(x)//2:]:
                print(n)
                ans += n
    
    return ans
