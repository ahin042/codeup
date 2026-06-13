f = int(input())
n = {} ; nn = []
for i in range(f) :
    a,b = map(int,input().split())
    n[a] = b
for i in n.keys() :
    nn.append(i)
nn.sort()
for i in nn :
    print(i,n[i])