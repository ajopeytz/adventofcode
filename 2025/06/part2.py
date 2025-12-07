# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

def list2num(l):
    r = 0
    for i in l:
        r = r*10 + i
    return r

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [line for line in f.readlines()]
    ans = 0
    N = dict()
    numbers = True
    for l in s:
        i = 0
        j = 0
        for n in l:
            if n!=" " and n.isnumeric():
                if j not in N.keys():
                    N[j] = [int(n)]
                else:
                    N[j].append(int(n))
                i += 1
            elif n!=" ":
                if n == "+":
                    r = 0
                elif n == "*":
                    r = 1
                else:
                    break
                m = j
                while True:
                    if m in N.keys():
                        if n == "+":
                            r += list2num(N[m])
                        else:
                            r *= list2num(N[m])
                    else:
                        break
                    m += 1
                ans += r
                i += 1
            j+=1


    return ans
