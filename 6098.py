a = []
for i in range(10) :
    aa = list(map(int, input().split()))
    a.append(aa)
x, y = 1, 1
while True:
    if a[x][y] == 2:
        a[x][y] = 9
        break
    a[x][y] = 9
    if a[x][y + 1] != 1:
        y += 1
    elif a[x + 1][y] != 1:
        x += 1
    else:
        break
for i in a:
    print(*i)