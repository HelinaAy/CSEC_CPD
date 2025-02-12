n = int(input())
o = 0
teams = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j and teams[i][0] == teams[j][1]:
            o+=1
print(o)
