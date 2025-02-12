n = int(input())
m = [input().strip() for _ in range(n)]
group = 1
for i in range(1, n):
   if m[i] != m[i-1]:
      group += 1
print(group)
        
