a,b,c = map(int, input().split())
m = {}
for i in range(1,a + 1) :
    m[i] = 0
for i in range(2) :
    n = list(map(int, input().split()))
    for j in n :
        m[j] += 1
c = 0 ; r = 0
for i in m.values():
    if i == 0:
        c += 1
    elif i == 2:
        r += 1
print(c,r)