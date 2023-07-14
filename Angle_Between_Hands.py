a,b=map(int,input().split(":"))
o=abs(5.5*b-30*a)
if o>180:
    print(360-o)
else:
    print(o)