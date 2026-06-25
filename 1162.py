a,b,c = map(int,input().split())
n = (a + b + c)
n -= (n // 1000) * 1000
n = n // 100
if n % 2 == 0 :
    print("대박")
else :
    print("그럭저럭")