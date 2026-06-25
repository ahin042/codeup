n = list(map(int, input().split())) ; m = 0
for i in n :
    if i <= 170 :
        m = 1
        print("CRASH")
        break
if m != 1 :
    print("PASS")