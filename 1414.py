n = input()
n = n.lower()
a = 0 ; b = 0 ; m = []
for i in n :
    m.append(i)
    if i == "c" :
        a += 1
print(a)
for i in range(len(m)) :
    try :
        if m[i] + m[i + 1] == "cc" :
            b += 1
    except IndexError :
        pass
print(b)