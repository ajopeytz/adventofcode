s = get_input(DAY).strip() # the daily input is stored in s

ans = 0
import time
t0 = time.time()

cache = dict()
bcache = dict()
def blink(n,i):
    if (n,i) not in bcache.keys():
        if n not in cache.keys():
            if n == '0':
                cache[n] = ['1']
            elif len(n)%2==0:
                cache[n] = [str(int(n[:len(n)//2])),str(int(n[len(n)//2:]))]
            else:
                cache[n] = [str(int(n)*2024)]
        if i > 0:
            if len(cache[n])==2:
                r = blink(cache[n][0],i-1) + blink(cache[n][1],i-1)
            else:
                r = blink(cache[n][0],i-1)
        else:
            r = 1
        bcache[(n,i)] = r
    return bcache[(n,i)]

numbers = []
for n in s.split(" "):
    numbers.append(n)

for n in numbers:
    ans += blink(n,75)
    
print((time.time()-t0)*1000)
print(ans)
