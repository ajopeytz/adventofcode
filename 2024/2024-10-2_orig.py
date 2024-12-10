'''
Advent of Code automation template - @MathisHammel

This template provides functions to download inputs and submit answers on AoC.

You need to paste your adventofcode.com session cookie below.
If you don't know how to get this cookie, here's a quick tutorial:
- Open your browser and go to adventofcode.com, make sure you are logged in
- Open the developer console (Ctrl+Shift+I on Firefox/Chrome)
- Get the value of your session cookie:
      - Chrome : 'Application' tab > Cookies
      - Firefox : 'Storage' tab > Cookies
- The cookie is a string of 96 hexadecimal characters, paste it in the AOC_COOKIE below.

Your cookie is similar to a password, >>> DO NOT SHARE/PUBLISH IT <<<
If you intend to share your solutions, store it in an env variable or a file.
'''

import requests

AOC_COOKIE = '53616c7465645f5f9ac1d9ccd039ba519f922e8003cee50bb154c39ff637a373b06662115919b41921305df0031c14ca0eae06584e03be11b1461ed3838f9651'
YEAR = '2024'

def get_input(day):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}/input', 
                       headers={'cookie':'session='+AOC_COOKIE})
    return req.text

def get_example(day,offset=0):
    req = requests.get(f'https://adventofcode.com/{YEAR}/day/{day}',
                       headers={'cookie':'session='+AOC_COOKIE})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]

def submit(day, level, answer):
    print(f'You are about to submit the follwing answer:')
    print(f'>>>>>>>>>>>>>>>>> {answer}')
    input('Press enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{YEAR}/day/{day}/answer',
                             headers={'cookie':'session='+AOC_COOKIE}, data=data)
    if 'You gave an answer too recently' in response.text:
        # You will get this if you submitted a wrong answer less than 60s ago.
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        # You will get this if you submit on a level you already solved.
        # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
        print('VERDICT : ALREADY SOLVED')
    else:
        print('VERDICT : OK !')

DAY = 10
PART = 2
s = get_input(DAY).strip() # the daily input is stored in s

#s = "89010123\n78121874\n87430965\n96549874\n45678903\n32019012\n01329801\n10456732"
#s = "...0...\n...1...\n...2...\n6543456\n7.....7\n8.....8\n9.....9"
#s = "..90..9\n...1.98\n...2..7\n6543456\n765.987\n876....\n987...."

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
            score += s
        if x<len(grid[y])-1 and grid[y][x+1] == str(height+1):
            s,t = find_trailhead(grid,x+1,y)
            tops.extend(t)
            score += s
        if y>0 and grid[y-1][x] == str(height+1):
            s,t = find_trailhead(grid,x,y-1)
            tops.extend(t)
            score += s
        if y<len(grid)-1 and grid[y+1][x] == str(height+1):
            s,t = find_trailhead(grid,x,y+1)
            tops.extend(t)
            score += s
        scores[(x,y)] = (score,list(set(tops)))
    return score,tops

ans = 0

grid = []
import time

t0= time.time()
for l in s.split("\n"):
    grid.append(list(l))

for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if grid[i][j] == "0":
            score,t = find_trailhead(grid,j,i)
            ans += score

print(ans)
print((time.time()-t0)*1000)
submit(DAY, PART, ans)
