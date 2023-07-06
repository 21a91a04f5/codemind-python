n=int(input())
t=n
c=0
while n:
    r=n % 10
    c=c*10+r
    n=n // 10
if(c == t):
    print("True")
else:
    print("False")