import math
n=int(input())
l=list(map(int,input().split()))
s1=l[0]
s2=l[1]
lcm=math.lcm(s1,s2)
for i in range(2,len(l)):
    lcm=math.lcm(lcm,l[i])
print(lcm)