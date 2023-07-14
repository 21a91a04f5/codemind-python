n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
c=0
for i in l:
    if i==l.count(i) and i not in a:
        a.append(i)
c=sum(a)
if c==0:
    print(-1)
else:
    avg=c/len(a)
    print("%.2f"%avg)