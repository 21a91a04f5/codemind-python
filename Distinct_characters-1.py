n=input()
a=n.lower()
l=list(a)
b=[]
for i in l:
    if l.count(i)==1 and i!=" ":
        b.append(i)
b.sort()
print(''.join(b))