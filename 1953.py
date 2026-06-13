def star(i,j):
    print("*" * i)
    if i == j:
        return
    star(i + 1,j)
n = int(input())
star(1,n)