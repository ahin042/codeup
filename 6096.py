a = []
for i in range(19) :
    aa = list(map(int, input().split()))
    a.append(aa)
n = int(input())
for i in range(n) :
    x,y = map(int, input().split())
    for j in range(19) :
        if a[x - 1][j] == 1:
            a[x - 1][j] = 0
        else :
            a[x - 1][j] = 1
        if a[j][y - 1] == 1:
            a[j][y - 1] = 0
        else :
            a[j][y - 1] = 1
for i in a:
    print(*i)