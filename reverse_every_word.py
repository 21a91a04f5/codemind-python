n=input().split()
a=[]
for i in n:
    l=list(i)
    l.reverse()
    b=(''.join(l))
    a.append(b)
print(*a)