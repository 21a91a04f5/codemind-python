n=int(input())
l=list(map(int,input().split()))
x=sum(l)
while n:
    if x%n==0:
        print(n)
        break
    n=n-1
    