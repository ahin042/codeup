n = int(input())
a = [] ; aa = []
for i in range(1, n * n + 1):
    aa.append(0)
    if i % n == 0:
        a.append(aa)
        aa = []
num = 1
for i in range(n):
    for j in range(n - 1, - 1, - 1):
        a[j][i] = num
        num += 1
for i in range(n) :
    print(*a[i][0:])