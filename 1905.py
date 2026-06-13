def add(n):
    if n == 1:
        return 1
    return n + add(n - 1)
n = int(input())
print(add(n))
