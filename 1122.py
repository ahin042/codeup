n = int(input())
print(n // 60,end = " ")
n -= (n // 60) * 60
print(n)