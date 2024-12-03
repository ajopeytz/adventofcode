s = get_input(DAY).strip() # the daily input is stored in s
ans=0
import re
do = True
for instruction in s.split("\n"):
    matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))",instruction)
    for ins in matches:
        if ins == "do()":
            do = True
        elif ins == "don't()":
            do = False
        elif do:
            digits = re.findall(r"(\d+)",ins)
            ans += int(digits[0])*int(digits[1])

    
print(ans)
