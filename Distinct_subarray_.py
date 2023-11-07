a=int(input())
b=int(input())
c=[]
d=[]
for i in range(a,b+1):
    c.append(i)
for i in range(len(c)):
    for j in range(i,len(c)+1):
        d.append(c[i:j])
e=0
for i in d:
    if sum(i)%2!=0 and len(i)!=0:
        e+=1
print(e)