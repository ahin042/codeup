a = []
q = int(input())
m = list(map(int, input().split()))
for i in range(0,len(m),2) :
    if m[i] < m[i + 1] :
        a.append(m[i])
    else :
        a.append(m[i + 1])
print(*a)