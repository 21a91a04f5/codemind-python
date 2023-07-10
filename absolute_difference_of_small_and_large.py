n=input().split()
a=[]
for i in n:
    b=ord(max(i))-ord(min(i))
    a.append(b)
print(*a)