s = input().strip()
t = input().strip()
p = 1
for instruction in t:
    if p <= len(s) and s[p - 1] == instruction:
        p += 1
 
print(p)
