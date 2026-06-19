def lst(x,n) :
    a = [0] * n
    a[x] = 1
    print(*a)
    if x == n - 1:
        return 0
    return lst(x + 1,n)
n = int(input())
lst(0,n)