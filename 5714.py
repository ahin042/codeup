a = list(map(int, input().split()))
for i in range(0, len(a), 2):
    if i + 1 < len(a):
        key = a[i]
        val = a[i + 1]
        if key >= 15 and val >= 100:
            print("특", end=" ")
        elif key >= 10 and val >= 70:
            print("상", end=" ")
        else:
            print("보통", end=" ")