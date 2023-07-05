n=int(input())
l=list(map(int,input().split()))
b = l[:len(l)//2]
c = l[len(l)//2:]
c.reverse()
print(*c,*b)