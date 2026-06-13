a = int(input())
aa = list(map(int, input().split()))

sa = sorted(set(aa))

m = {}
for i in range(len(sa)):
    m[sa[i]] = i

for i in aa:
    print(m[i], end=" ")
