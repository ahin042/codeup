a = int(input())
n = list(map(int, input().split()))
find = int(input())
try :
    print(n.index(find) + 1)
except ValueError :
    print(-1)