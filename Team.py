n = int(input())
sum = 0
for _ in range (n):
    a ,b ,c = map(int,input().split())
    if a + b + c >= 2:
        sum+=1
print(sum)
