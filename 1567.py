def add(a,b,c):
    j = 0
    for i in range(m[0] - 1, m[1]) :
        j += b[i]
    return j
a = int(input())
n = list(map(int,input().split()))
m = list(map(int,input().split()))
print(add(a,n,m))