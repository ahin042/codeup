m, mm = map(int, input().split())
a = [] ; c = 1
for i in range(m) :
    aa = []
    for j in range(mm) :
        aa.append(0)
    a.append(aa)
for i in range(m - 1, - 1, - 1) :
    if (m - 1 - i) % 2 == 1 :
        for j in range(mm - 1, - 1, - 1) :
            a[i][j] = c
            c += 1
    else :
        for j in range(mm) :
            a[i][j] = c
            c += 1
for i in range(m) :
    print(*a[i])