n=input()
l=list(n)
v=input()
if v in l:
    print(True)
    print(l.index(v))
else:
    print(False)