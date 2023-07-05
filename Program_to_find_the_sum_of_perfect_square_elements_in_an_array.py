n=int(input())
l=list(map(int,input().split()))
b=[]
for i in range(len(l)):
    a=l[i]**0.5
    if a==int(a):
        b.append(l[i])
print(sum(b))