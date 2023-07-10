n=input()
a=n.lower()
l=list(a)
b=[]
for i in l:
    if i not in b:
        b.append(i)
b.sort()
for i in b:
    if i==" ":
        b.remove(i)
print(''.join(b))