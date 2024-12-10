s = get_input(DAY).strip() # the daily input is stored in s

scores = dict()
def find_trailhead(grid,x,y):
    if (x,y) in scores.keys():
        return scores[(x,y)]
    score = 0
    tops = []
    if grid[y][x] == '9':
        score = 1
        tops.append((x,y))
    else:
        height = int(grid[y][x])
        if x>0 and grid[y][x-1] == str(height+1):
            s,t = find_trailhead(grid,x-1,y)
            tops.extend(t)
        if x<len(grid[y])-1 and grid[y][x+1] == str(height+1):
            s,t = find_trailhead(grid,x+1,y)
            tops.extend(t)
        if y>0 and grid[y-1][x] == str(height+1):
            s,t = find_trailhead(grid,x,y-1)
            tops.extend(t)
        if y<len(grid)-1 and grid[y+1][x] == str(height+1):
            s,t = find_trailhead(grid,x,y+1)
            tops.extend(t)
        scores[(x,y)] = (len(set(tops)),list(set(tops)))
        score = len(set(tops))
    return score,tops

ans = 0

grid = []
import time
t0 = time.time()
for l in s.split("\n"):
    grid.append(list(l))

for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if grid[i][j] == "0":
            score,t = find_trailhead(grid,j,i)
            ans += score
print((time.time()-t0)*1000)
print(ans)
