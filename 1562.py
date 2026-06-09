def small(a,b):
	if a < b:
		return a
	else :
		return b
a,b = map(int,input().split())
print(small(a,b))