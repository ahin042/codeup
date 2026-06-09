def number(a,b) :
	return a - b
a,b = map(int,input().split())
if a < b:
	a,b=b,a
print(number(a,b))