n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    if (i>=0):
        s=list(str(i))
        s=len(s)
        c.append(s)
    else:
        s=list(str(i))
        s=len(s)-1
        c.append(s)
print(*c)