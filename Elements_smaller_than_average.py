n=int(input())
a=list(map(int,input().split()))
c=(sum(a)//len(a))
d=0
for i in a:
    if i<=c:
        d+=1
print(d)