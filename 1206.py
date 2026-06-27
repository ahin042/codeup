a,b = map(int,input().split())
if a > b :
    a,b = b,a
c = 0
for i in range(1, b + 1) :
    if a * i == b :
        c = i
        break
if c == 0 :
    print("none")
else :
    print(f"{a}*{c}={b}")