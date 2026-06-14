a = [] ; c = 0
for i in range(10) :
    m = int(input())
    a.append(m)
for i in a :
    c += i
print(c // 10)
m = {}
for i in a:
    if i in m :
        m[i] += 1
    else :
        m[i] = 1
c = a[0]
for i in m:
    if m[i] > m[c] :
        c = i
print(c)