a=int(input())
n=input().split()
b=[]
for i in n:
    l=len(i)
    b.append(l)
print(b.count(max(b)))