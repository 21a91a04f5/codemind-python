n=input()
l=list(n)
a=[]
c=0
for i in l:
    if l.count(i)==1:
        c=l.index(i)
        a.append(c)
        c+=1
if c==0:
    print(-1)
else:
    print(min(a))