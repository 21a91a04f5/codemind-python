n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(n):
    if l[i]<a or l[i]>b:
        c.append(l[i])
print(sum(c))