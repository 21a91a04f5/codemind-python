n=input()
a=int(input())
b=int(input())
l=list(n)
c=[]
for i in range(a,b+1):
    c.append(l[i])
print(''.join(c))