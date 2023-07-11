n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
d=0
for i in l:
    if i>=a and i<=b:
        c.append(i)
        d+=1
if d==0:
    print(-1)
else:
    print(*c)