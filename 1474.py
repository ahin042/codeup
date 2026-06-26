m, mm = map(int, input().split())
a = [] ; c = m * mm
for i in range(m) :
    aa = []
    for j in range(mm) :
        aa.append(0)
    a.append(aa)
for i in range(mm) :
    if i % 2 == 0:
        for j in range(m) :
            a[j][i] = c
            c -= 1
    else :
        for j in range(m - 1, - 1, - 1) :
            a[j][i] = c
            c -= 1
for i in range(m) :
    print(*a[i])