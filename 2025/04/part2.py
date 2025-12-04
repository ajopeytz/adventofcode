# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

def check_adjecent(x,y,m):
    c = 0
    if m[x][y] == "@":
        for i in range(max(0,x-1),min(x+2,len(m))):
            for j in range(max(0,y-1),min(y+2,len(m[i]))):
                if m[i][j] == "@" and (x!=i or y!=j):
                    c += 1
    else:
        c = 9
    return c

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [list(line.strip()) for line in f.readlines()]

    ans = 0
    c = 1
    while c>0:
        c = 0
        for x in range(0,len(s)):
            for y in range(0,len(s[x])):
                if check_adjecent(x,y,s)<4:
                    c += 1
                    s[x][y] = "x"
        ans += c


    return ans
