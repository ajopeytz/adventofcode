ans=0

def check_order(pages,before):
    i = 0
    for p in pages: 
        if p in before.keys():
            for b in before[p]:
                if b in pages and pages.index(b) < i:
                    return False,(pages.index(b),i)
                    break
        i+=1
    return True,0


inputs = s.split("\n\n")
rules = inputs[0].split("\n")
updates = inputs[1].split("\n")

before = dict()
for rule in rules:
    r = rule.split("|")
    if r[0] in before.keys():
        before[r[0]].append(r[1])
    else:
        before[r[0]] = [r[1]]

for u in updates:
    pages = u.split(",")
    valid,violation = check_order(pages,before)
    if not valid:
        while not valid:
            pages[violation[0]], pages[violation[1]] = pages[violation[1]], pages[violation[0]]
            valid,violation = check_order(pages,before)
        middle = int(pages[len(pages)//2])
        ans += middle

print(ans)
