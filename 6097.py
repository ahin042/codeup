n,nn = map(int,input().split())
a = []
for i in range(n) :
    aa = []
    for j in range(nn) :
        aa.append(0)
    a.append(aa)
n = int(input())
for i in range(n) :
    l,d,x,y = map(int,input().split())
    for j in range(l):
        if d == 0:
            a[x - 1][y - 1 + j] = 1
        else:
            a[x - 1 + j][y - 1] = 1
for i in a :
    print(*i)