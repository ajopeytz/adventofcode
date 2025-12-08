# Useful imports
import pyaoc
import math
from functools import cache,cmp_to_key
from collections import defaultdict
from itertools import combinations

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    with open(filename) as f:
        s = [tuple(map(int,line.strip().split(','))) for line in f.readlines()]
    
    groups = []
    for p in s:
        groups.append([p])
    pairs = combinations(s,2)
    sorted_pairs = sorted(pairs,key=lambda x: (x[0][0]-x[1][0])*(x[0][0]-x[1][0]) + (x[0][1]-x[1][1])*(x[0][1]-x[1][1]) + (x[0][2]-x[1][2])*(x[0][2]-x[1][2]))
    ans = 0
    j = 0
    connections = 1000 if len(s) == 1000 else 10
    for p in sorted_pairs:
        if j == connections:
            break
        i = 0
        i0=i1=-1
        for g in groups:
            if p[0] in g:
                i0 = i
            if p[1] in g:
                i1 = i
            i += 1
        if i0 != i1:
            gold = groups.copy()
            gnew = groups[i0] + groups[i1]
            groups.remove(gold[i0])
            groups.remove(gold[i1])
            groups.append(gnew)
        j += 1
    S = []
    for g in groups:
        S.append(len(g))
        print(len(g),g)
    S.sort(reverse=True)
    ans = S[0]*S[1]*S[2]
    return ans
