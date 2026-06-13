a,b,c = map(int,input().split())
for i in range(a, - 1, - 1) :
    if b % i == 0 and a % i == 0 and c % i == 0 :
        print(i)
        break