n = [] ; c = 0
for i in range(7) :
    a = int(input())
    if a % 2 == 1 :
        n.append(a)
if n == [] :
    print(-1)
else :
    for i in n :
        c += i
    print(c)
    print(min(n))