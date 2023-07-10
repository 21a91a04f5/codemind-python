n=int(input())
l=list(map(int,input().split()))
b=[]
c=0
for i in l:
    if l.count(i)==i:
        b.append(i)
        c+=1
d=[]
for i in b:
    if i not in d:
        d.append(i)
if c==0:
    print(-1)
else:
    print(*d)