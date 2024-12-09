s = get_input(DAY).strip() # the daily input is stored in s

ans = 0

file = True
i=0
fs = []
for c in s:
    for l in range(0,int(c)):
        if file:
            fs.append(i)
        else:
            fs.append(".")
    if file:
        file = False
        i += 1
    else:
        file = True

dontmove = []
for p in reversed(range(0,len(fs))):
    l = 0
    file = False
    Q = fs[p]
    while fs[p] not in ["."]:
        if fs[p] != Q:
            break
        p -= 1
        l += 1
    if p+1 not in dontmove:
        m = 0
        valid = False
        for s in range(0,len(fs)):
            if fs[s] == ".":
                m += 1
            else:
                m = 0
            if m == l:
                valid = True
                break
        if valid and (s-l)<p:
            for q in range(s-l+1,s+1):
                fs[q] = Q
                dontmove.append(q)
            for q in range(p+1,p+l+1):
                fs[q] = "#"
                dontmove.append(q)
        else:
            for q in range(p+1,p+l+1):
                dontmove.append(q)

i = 0
for c in fs:
    if c not in ['.','#']:
        ans += i*int(c)
    i += 1

print(ans)
