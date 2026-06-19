a,b = map(int,input().split())
if a > b :
    a,b = b,a
n = a + 1 ; r = 0 ; c = 0
while n != b - 1 :
    if  n == b - 1 :
        break
    r = n
    while r != 1 :
        if r == 1:
            break
        c += 1
        if r % 2 == 0:
            r /= 2
        else:
            r *= 3
            r += 1
    c = r
print(r,c) # 진짜 뭔 문제가 더럽네