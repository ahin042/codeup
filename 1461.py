n = int(input())
a = [] ; aa = []
for i in range(1, n * n + 1):
    aa.append(i)
    if i % n == 0:
        aa.reverse()
        a.append(aa)
        aa = []
for i in range(n) :
    print(*a[i][0:])