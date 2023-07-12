a=input()
b=("AEIOUaeiou")
c=0
d=[]
for i in a:
    if i in b and i not in d:
        c+=1
        d.append(i)
if c==0:
    print(-1)
else:
    print(*d)
        