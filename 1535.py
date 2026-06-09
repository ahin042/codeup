def big(n) :
    a = 0
    m = list(map(int,input().split()))
    for i in range(len(m)) :
        if m[a] < m[i] and m[a] != m[i] :
            a = i
    return a + 1
number = int(input())
print(big(number))