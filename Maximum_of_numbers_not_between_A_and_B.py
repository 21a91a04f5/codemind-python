n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in l:
    if (i<a or i>b ) and i not in c:
        c.append(i)
if len(c)>0:
    print(max(c))
else:
    print(-1)