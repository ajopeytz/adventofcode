f = open('2024-02-2_jj.txt','r')

s = f.read().strip() # the daily input is stored in s
f.close()
ans=0
for level in s.split("\n"):
    di = ""
    l = level.split(" ")
    n = int(l[0])
    unsafecount = 0
    for m in l[1:]:
        m = int(m)
        if m > n:
            d = "up"
        elif m < n:
            d = "down"
        else:
            unsafecount+=1
        if di=="":
            di=d
        if d != di:
            unsafecount+=1
        if abs(m-n) > 3:
            unsafecount+=1
        n = m

    if unsafecount<2:
        ans += 1
#    else:
#        print(level,"unsafe",unsafecount)

    
print(ans)
