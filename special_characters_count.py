n=input()
l=list(n)
a=("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ")
c=0
for i in l:
    if i not in a:
        c+=1
print(c)