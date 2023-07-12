a=input()
b=input()
c=a.lower()
d=b.lower()
e=[]
for i in c:
    if i not in d and i not in e and i!=" ":
        e.append(i)
for i in d:
    if i not in c and i not in e and i!=" ":
        e.append(i)
e.sort()
print(''.join(e))