n = int(input()) ; c = 0 ; r = 1
while c < n :
    if c >= n :
        break
    c += r
    r += 1
print(c)