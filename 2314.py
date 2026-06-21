n = int(input())
c = 0
if n >= 10 :
    c += n // 10
    n = n % 10
if n >= 5 :
    c += n // 5
    n = n % 5
if n >= 3 :
    c += n // 3
    n = n % 3
if n > 0:
    c += n // 1
print(c)