n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    i=str(i)
    x=list(i)
    a.append(len(x))
c=max(a)
for i in l:
    i=str(i)
    e=list(i)
    if len(i)==c:
        b.append(i)
print(*b)