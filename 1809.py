a,b = map(int,input().split())
if a > b:
    a,b = b,a
n = b -a ; c = 0
print(n, end=" ")
while n != 1:
    if n == 1:
        break
    c += 1
    if n % 2 == 0:
        n /= 2
    else :
        n *= 3
        n+= 1
print(c + 1)