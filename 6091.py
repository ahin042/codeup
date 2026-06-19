i = 1
a,b,c = map(int,input().split())
while i % a != 0 or i % b != 0 or i % c != 0 :
  i += 1
print(i)