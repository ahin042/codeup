n,nn = map(int,input().split())
a = [] ; aa = []
for i in range(1, n * nn + 1):
    aa.append(0)
    if i % nn == 0:
        a.append(aa)
        aa = []
num = 1
for i in range(n - 1, - 1, - 1):
    for j in range(nn - 1, - 1, - 1):
        a[i][j] = num
        num += 1
for i in range(n) :
    print(*a[i][0:])