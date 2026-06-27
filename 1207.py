n = list(map(int,input().split()))
c = 0
for i in n:
    if i == 1:
        c += 1
if c == 0 :
    print("모")
elif c == 1 :
    print("도")
elif c == 2 :
    print("개")
elif c == 3 :
    print("걸")
elif c == 4 :
    print("윷")