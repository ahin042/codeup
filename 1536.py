def small(n) :
    a = 0
    m = list(map(int,input().split()))
    for i in range(len(m)) :
        if m[a] > m[i] and m[a] != m[i] :
            a = i
    return m[a]
number = int(input())
print(small(number))