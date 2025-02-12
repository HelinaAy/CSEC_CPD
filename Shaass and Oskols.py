n = int(input())
b = list(map(int, input().split()))
m = int(input())
 
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1  
    y -= 1  
    
    left_birds = y
    right_birds = b[x] - (y + 1)
    
    if x > 0:  
        b[x - 1] += left_birds
    if x < n - 1:  
        b[x + 1] += right_birds
    
    b[x] = 0  
 
for count in b:
    print(count)
