m = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 0,
    7 : 0,
    8 : 0,
    9 : 0,
    10 : 0,
    11 : 0,
    12 : 0,
    13 : 0,
    14 : 0,
    15 : 0,
    16 : 0,
    17 : 0,
    18 : 0,
    19 : 0,
    20 : 0,
    21 : 0,
    22 : 0,
}
n1 = list(map(int, input().split()))
n2 = list(map(int, input().split()))
for i in n1 :
    m[i] += 1
for i in n2 :
    m[i] += 1
c = 0 ; r = 0
for i in m.values():
    if i == 0:
        c += 1
    elif i == 2:
        r += 1
print(c,r)