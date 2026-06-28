n = int(input())
a = [] ; c = 1
for i in range(n) :
    aa = []
    for j in range(n) :
        aa.append(0)
    a.append(aa)
for i in range(n) :
    for j in range(n) :
        a[i][j] = c
        c += 1
for i in a :
    print(*i)