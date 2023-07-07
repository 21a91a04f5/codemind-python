a=int(input())
l=list(map(int,input().split()))
c=[]
d=0
for i in l:
    i=str(i)
    l1=list(i)
    l1.reverse()
    e=(''.join(l1))
    c.append(e)
for i in range(a):
    if l[i]==int(c[i]):
        d+=1
print(d)
