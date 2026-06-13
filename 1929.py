def m(n):
    if n == 1:
        print(1)
        return
    if n % 2 == 0:
        m(n // 2)
    else:
        m(3 * n + 1)
    print(n)
a = int(input())
m(a)
