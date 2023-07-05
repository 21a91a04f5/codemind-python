n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(len(l)):
    for j in range(i,len(l)):
        x=sum(l[i:j+1])
        a.append(x)
print(max(a))