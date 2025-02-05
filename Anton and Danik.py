n = int(input())
s = input()
antonwin = s.count('A')
danikwin = s.count('D')
if antonwin>danikwin:
    print("Anton")
elif antonwin<danikwin:
    print("Danik")
else:
    print("Friendship")
