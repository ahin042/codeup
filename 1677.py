a,b = map(int,input().split())
print("+",end="")
for i in range(a - 2) :
    print("-",end="")
print("+")
if b > 2 :
    for i in range(b - 2) :
        print("|", end="")
        for j in range(a - 2):
            print(" ", end="")
        print("|")
print("+",end="")
for i in range(a - 2) :
    print("-",end="")
print("+")