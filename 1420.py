n = int(input())
m = []
for x in range(n):
    i,j = map(str,input().split())
    j = int(j)
    m.append([j,i])
m.sort()
m.reverse()
print(m[2][1])