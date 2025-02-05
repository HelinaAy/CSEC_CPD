sm = input().strip()
pm = input().strip()
if sm.lower()>pm.lower():
    print("1")
elif sm.lower()<pm.lower():
    print("-1")
else:
    print("0")
