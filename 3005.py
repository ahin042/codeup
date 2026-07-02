import math as m
a = int(input())
n = list(map(int, input().split()))
print(m.lcm(*n))