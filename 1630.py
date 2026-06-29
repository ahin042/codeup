a = []
n = int(input())
for i in range(n) :
    m = input()
    a.append(m)
for i in range(len(a)) :
    print(a[i])
    if i != len(a) - 1 :
        print("AMOLED")