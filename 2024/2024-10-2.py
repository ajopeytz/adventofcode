s = get_input(DAY).strip() # the daily input is stored in s

scores = dict()
def find_trailhead(grid,x,y):
    if (x,y) in scores.keys():
        return scores[(x,y)]
    score = 0
    if grid[y][x] == '9':
        score = 1
    else:
        height = int(grid[y][x])
        if x>0 and grid[y][x-1] == str(height+1):
            s = find_trailhead(grid,x-1,y)
            score += s
        if x<len(grid[y])-1 and grid[y][x+1] == str(height+1):
            s = find_trailhead(grid,x+1,y)
            score += s
        if y>0 and grid[y-1][x] == str(height+1):
            s = find_trailhead(grid,x,y-1)
            score += s
        if y<len(grid)-1 and grid[y+1][x] == str(height+1):
            s = find_trailhead(grid,x,y+1)
            score += s
        scores[(x,y)] = score
    return score

ans = 0

grid = []
import time

t0= time.time()
for l in s.split("\n"):
    grid.append(list(l))

for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if grid[i][j] == "0":
            score = find_trailhead(grid,j,i)
            ans += score

print(ans)
print((time.time()-t0)*1000)
