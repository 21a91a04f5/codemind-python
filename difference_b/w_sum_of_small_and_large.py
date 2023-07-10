n=input().split()
a=[]
b=[]
for i in n:
    a.append(ord(min(i)))
    b.append(ord(max(i)))
print(sum(b)-sum(a))