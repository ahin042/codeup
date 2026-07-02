n = [int(input()) for i in range(9)]
r = sum(n)
ex = r - 100
n.sort()
m = False
for i in range(9):
    if m:
        break
    for j in range(i+1, 9):
        if n[i] + n[j] == ex:
            del n[j]
            del n[i]
            m = True
            break
for x in n:
    print(x)