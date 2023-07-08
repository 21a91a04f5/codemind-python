n=input().split()
n.reverse()
b=[]
for i in n:
    a=i[::-1]
    b.append(a)
print(*b)
    