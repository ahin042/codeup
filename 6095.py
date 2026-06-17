a = [] ; length = []
for i in range(19) :
    aa = []
    for j in range(19) :
        aa.append(0)
    a.append(aa)
n = int(input())
for i in range(n) :
    x,y = map(int,input().split())
    a[x - 1][y - 1] = 1
for i in range(19) :
    for j in range(19) :
        print(a[i][j],end=" ")
    print()