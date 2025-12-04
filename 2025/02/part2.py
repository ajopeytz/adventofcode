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

    ans = 0
    for r in s:
        pt = r.split('-')
        ids = []
        for n in range(int(pt[0]),int(pt[1])+1):
            x = str(n)
            for i in range(1,len(x)//2+1):
                if len(x)%i == 0 and (x[:i]*(len(x)//i)) ==x :
                    ids.append(x)
        for x in set(ids):
            ans += int(x)

            
    
    return ans
