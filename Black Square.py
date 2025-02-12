a1, a2, a3, a4 = map(int, input().split())
s = input()
calories = [0, a1, a2, a3, a4]
total_calories = sum(calories[int(char)] for char in s)
print(total_calories)
