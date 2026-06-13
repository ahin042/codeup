a,b =  map(int,input().split())
m = {}
n = []
for x in range(a) :
    i,j = input().split()
    j = int(j)
    if i not in m :
        m[i] = j
    else :
        m[i] = max(m[i],j)
for i in m.keys():
    n.append([m[i], i])
n.sort()
n.reverse()
n = n[:b]
for i in range(len(n)):
    print(n[i][1])
