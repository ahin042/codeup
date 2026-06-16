a = input()
c1 = 0 ; c2 = 0
for i in a:
    if i == '(':
        c1 += 1
    else :
        c2 += 1
print(c1,c2)