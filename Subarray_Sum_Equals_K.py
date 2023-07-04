a,b=map(int,input().split())
c=list(map(int,input().split()))
e=[]
f=0
for i in range(len(c)):
    for j in range(i,len(c)):
        d=sum(c[i:j+1])
        e.append(d)
for i in e:
    if i==b:
        f+=1
print(f)