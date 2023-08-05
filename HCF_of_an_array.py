import math
n=int(input())
l=list(map(int,input().split()))
s1=l[0]
s2=l[1]
hcf=math.gcd(s1,s2)
for i in range(2,len(l)):
    hcf=math.gcd(hcf,l[i])
print(hcf)