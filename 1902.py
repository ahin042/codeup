def num(n) :
    if n == 1:
        print(n)
        return 0
    print(n)
    num(n - 1)
n = int(input())
num(n)