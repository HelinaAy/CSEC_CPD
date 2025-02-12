n = int(input())
cards = list(map(int, input().split()))
 
sereja_points = 0
dima_points = 0
left = 0
right = n - 1
 
for turn in range(n):
    if cards[left] > cards[right]:
        if turn % 2 == 0:
            sereja_points += cards[left]
        else:
            dima_points += cards[left]
        left += 1
    else:
        if turn % 2 == 0:
            sereja_points += cards[right]
        else:
            dima_points += cards[right]
        right -= 1
 
print(sereja_points, dima_points)
