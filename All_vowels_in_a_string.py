a=input()
b=['a','e','i','o','u']
for i in a:
    if i in b:
        b.remove(i)
if len(b)==0:
    print(True)
else:
    print(False)