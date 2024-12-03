s = get_input(DAY).strip() # the daily input is stored in s
ans=0
import re
for instruction in s.split("\n"):
    matches = re.findall(r"(mul\(\d+,\d+\))",instruction)
    for mul in matches:
        digits = re.findall(r"(\d+)",mul)
        ans += int(digits[0])*int(digits[1])

    
print(ans)
