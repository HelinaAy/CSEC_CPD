s = input().strip()
lower = sum(1 for char in s if char.islower())
upper = len(s)-lower
if upper>lower:
   print(s.upper())
else:
   print(s.lower())
