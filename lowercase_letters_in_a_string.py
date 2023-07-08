n=input()
l=list(n)
a=("abcdefghijklmnopqrstuvwxyz")
c=0
for i in l:
    if i in a:
        c+=1
print(c)