a=int(input())
b=list(map(int,input().split()))
l=[]
c=0
for i in b:
    if i not in l:
        l.append(i)
for i in range(len(l)):
    x=b.count(l[i])
    if x%2==0:
        c+=(x//2)
    else:
        c+=(x//2)
print(c)
        