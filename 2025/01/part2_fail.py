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
            c = -int(m[1:])
        else:
            c = int(m[1:])
        r = d+c
        d = r%100
        #print(m,'r',r,'d',d,'c',c%100)
        i = 0
        if d == 0:
            i = math.ceil((abs(c)/100))
            print('at',0,'i',i,m)
            ans += i
        elif r != d and d!=(c%100):
            i = math.floor((abs(c)/100))
            print('c',c,'d',d,'p',p,abs(c))
            if c < 0:
                if d>p:
                    i+=1
            else:
                if d<p:
                    i+=1
            print("past",0,'i',i,m)
            print('p',p)
            ans += i
        #print(i,ans)
        print(d)
    return ans
