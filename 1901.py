def num(i,n) :
    if i == n:
        print(n)
        return 0
    print(i)
    i += 1
    num(i,n)
n = int(input())
num(1,n)