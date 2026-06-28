a = [] ; r = 0
for i in range(7) :
    a.append(int(input()))
for i in a :
    r += i
print("%.2f" % (r / 7))