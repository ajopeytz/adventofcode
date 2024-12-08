s = get_input(DAY).strip() # the daily input is stored in s

ans = 0

def relative_position(x,y,antenna):
    return int(antenna[0])-x,int(antenna[1])-y,antenna[2]

def is_antinode(x,y,antennas):
    for antenna in antennas:
        other_antennas = antennas.copy()
        other_antennas.remove(antenna)
        for other in other_antennas:
            if other[2] == antenna[2]:
                rx,ry,c = relative_position(antenna[0],antenna[1],other)
                for i in range(0,50):
                    if antenna[0]+rx*i == x and antenna[1]+ry*i == y:
                        return True
    return False

grid = []

antennas = []

y = 0
for l in s.split("\n"):
    grid.append(list(l))
    x = 0
    for p in l:
        if p != ".":
            antennas.append([x,y,p])
        x+=1
    y += 1

y = 0
for l in grid:
    x = 0
    for p in l:
        if is_antinode(x,y,antennas):
            ans += 1
        x+=1
    y+=1

print(ans)
