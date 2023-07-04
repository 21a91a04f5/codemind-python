n=int(input())
p=n
i=0
while n:
    i=i+1
    n=n//10
n=p*p
k=n%(10**i)
if (p==k):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")