n=input()
l=list(n)
a=[]
c=0
for i in l:
    if l.count(i)==1:
        a.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(a[0])