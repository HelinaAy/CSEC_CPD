n, h = map(int,input().split())
a = list(map(int,input().split()))
 
mm = 0
for x in a:
    if x > h:
        mm += 2
    else:
        mm += 1
print(mm)
