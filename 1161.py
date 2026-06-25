a,b = map(int,input().split())
if a % 2 == 1:
    a = "홀수"
else :
    a = "짝수"
if b % 2 == 1:
    b = "홀수"
else :
    b = "짝수"
if a == b:
    print(f"{a}+{b}=짝수")
else :
    print(f"{a}+{b}=홀수")
