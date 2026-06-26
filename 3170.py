a,b = map(int,input().split())
m = {} ; n = []
for i in range(a) :
    x,xx = map(str,input().split())
    if x in m :
        m[x] += int(xx)
    else :
        m[x] = int(xx)
for i in range(b) :
    x = input()
    if x not in m :
        n.append(0)
    else :
        n.append(m[x])
for i in n :
    print(i)