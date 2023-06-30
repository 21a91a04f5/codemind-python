n=int(input())
a=list(map(int,input().split()))
p=[]
for i in a:
    if a.count(i)==2:
        p.append(i)
        break
print(*p)