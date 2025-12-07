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
    N = []
    numbers = True
    for l in s:
        i = 0
        for n in l.split(" "):
            if n!="" and n.isnumeric():
                print(N,i)
                if len(N)==i:
                    N.append([int(n)])
                else:
                    N[i].append(int(n))
                i += 1
            elif n!="":
                if n == "+":
                    r = 0
                else:
                    r = 1
                for m in N[i]:
                    if n == "+":
                        r += m
                    else:
                        r *= m
                ans += r
                i += 1


    return ans
