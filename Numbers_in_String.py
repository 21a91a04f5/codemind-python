a=input()
l=list(a)
c=("1234567890")
b=[]
for i in a:
    if i in c:
        b.append(i)
d=0
for i in b:
    d+=int(i)
print(d)