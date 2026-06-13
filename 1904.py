def num(n,nn) :
    if n == nn:
        if nn % 2 == 1:
            print(nn)
        return 0
    if n % 2 == 1:
        print(n)
    num(n + 1 , nn)
n,nn = map(int,input().split())
num(n,nn)