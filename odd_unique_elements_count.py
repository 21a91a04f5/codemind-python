n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in l:
    if i not in a:
        a.append(i)
for i in a:
    if (i%2)!=0:
        c+=1
print(c)