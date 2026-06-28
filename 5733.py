k = int(input())
n = list(map(int,input().split()))
r = 0 ; a = []
for i in n :
    if i <= 50 :
        break
    a.append(i)
print(*a)
for i in a :
    r += i
print(r)