n = [] ; c = 0
for  i in range(5) :
    a,b = map(float,input().split())
    n.append(min(max(0, (b - a) - 1),4))
for i in n :
    c += i
if c >= 15 :
    print(int(c / 0.5 * 5000 - c / 0.5 * 5000 * 0.05))
elif c <= 5 :
    print(int(c / 0.5 * 5000 + c / 0.5 * 5000 * 0.05))
else :
    print(int(c / 0.5 * 5000))