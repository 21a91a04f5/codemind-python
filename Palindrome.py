n=int(input())
n=str(n)
l=list(n)
l.reverse()
a=(''.join(l))
if n==a:
    print(True)
else:
    print(False)