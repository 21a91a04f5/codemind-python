n=input()
a=n.lower()
l=list(a)
c=0
for i in l:
    if l.count(i)==1 and i!=" ":
        c+=1
print(c)