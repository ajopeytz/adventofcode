# Useful imports
import pyaoc
import math
from functools import cache
from collections import defaultdict

def remove_smaller(l):
    i = 0
    for e in l[:-1]:
        if int(e)<int(l[i+1]):
            break
        i += 1
    return l[0:i] + l[i+1:]


# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [line.strip() for line in f.readlines()]
    ans = 0
    for b in s:
        r = 0
        i = 0
        j = ""
        l = list(b)
        while len(l) > 12:
            l = remove_smaller(l)
        ans += int("".join(l))


    return ans
