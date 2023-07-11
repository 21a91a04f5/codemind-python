n=int(input())
l=list(map(int,input().split()))
c=list(l)
c.sort(reverse=True)
if c==l:
    print("yes")
else:
    print("no")