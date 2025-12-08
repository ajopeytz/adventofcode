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
    
    connected = []
    not_connected = s
    groups = []
    pairs = combinations(not_connected,2)
    sorted_pairs = sorted(pairs,key=lambda x: (x[0][0]-x[1][0])*(x[0][0]-x[1][0]) + (x[0][1]-x[1][1])*(x[0][1]-x[1][1]) + (x[0][2]-x[1][2])*(x[0][2]-x[1][2]))
    ans = 0
    j = 0
    c = 0
    connections = 1000 if len(s) == 1000 else 10
    for p in sorted_pairs:
        if j == connections:
            break
        found = False
        i = 0
        G = [0,0]
        for g in groups:
            if (p[0] in g and p[1] in g):# or (p[0] in connected and p[1] in connected):
                found = True
                c = 1
                break
            elif p[0] in g and p[1] not in connected:
                found = True
                g.append(p[1])
                connected.append(p[1])
                groups[i] = g
                c = 2
                break
            elif p[1] in g and p[0] not in connected:
                found = True
                g.append(p[0])
                connected.append(p[0])
                groups[i] = g
                c = 3
                break
            elif p[0] in g:
                G[0] = i
            elif p[1] in g:
                G[1] = i
            i += 1
#       print(found,p[1] in connected,p[0] in connected)
        if G != [0,0]:
            print("merge groups",G,p,groups[G[0]],groups[G[1]])
            gnew = groups[G[0]] + groups[G[1]]
            gfull = groups.copy()
            groups.remove(gfull[G[0]])
            groups.remove(gfull[G[1]])
            groups.append(gnew)
            connected.append(p[0])
            connected.append(p[1])
            c = 4
        elif not found:
            groups.append([p[0],p[1]])
            connected.append(p[0])
            connected.append(p[1])
            c = 5
        print(p,c,len(connected),groups)
        j += 1
    sizes = []
    for g in groups:
        print(len(g),g)
        sizes.append(len(g))
#    print(connected)
    S = sorted(sizes,reverse=True)
    ans = S[0]*S[1]*S[2]
    return ans
