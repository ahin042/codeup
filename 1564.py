def number(a,b):
	m = 0
	for i in range(1,a + 1) :
		if a % i == 0 and b % i == 0:
			m = i
	return m
a,b = map(int,input().split())
print(number(a,b))