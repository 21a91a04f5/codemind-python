n=input().split()
a=("AEIOUaeiou")
c=0
for i in n:
    l=list(i)
    if l[0] in a and l[len(l)-1] not in a:
        c+=1
print(c)