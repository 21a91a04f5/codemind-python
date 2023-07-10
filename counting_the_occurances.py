n=input()
b=input()
l=list(n)
c=0
if b in l:
    c=l.count(b)
    print(c)
else:
    print(-1)