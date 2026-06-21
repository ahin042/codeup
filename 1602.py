def change(a) :
    if a < 0 :
        if a % 1 != 0:
            return a * -1
        else :
            a = int(a)
            return a * -1
    else :
        if a % 1 != 0:
            return a
        else:
            a = int(a)
            return a
a = float(input())
print(change(a))