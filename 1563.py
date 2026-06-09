def m(a,b,c):
	n = [a,b,c]
	n.sort()
	return n[1]
a,b,c = map(int,input().split())
print(m(a,b,c))