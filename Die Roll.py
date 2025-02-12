from math import gcd
Y, W = map(int, input().split())
 
max_roll = max(Y, W)
 
successful_outcomes = 6 - max_roll + 1
 
numerator = successful_outcomes
denominator = 6
common_divisor = gcd(numerator, denominator)
 
 
numerator //= common_divisor
denominator //= common_divisor
 
print(f"{numerator}/{denominator}")
