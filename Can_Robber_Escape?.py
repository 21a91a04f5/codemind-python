n=input()
l=list(map(int,input().split()))
a,b=0,0
for i in l:
    if i%2!=0:
        a+=1
if a>2:
    print("NO")
else:
    print("YES")