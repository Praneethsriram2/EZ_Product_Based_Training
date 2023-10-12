s=input("Enter a string")
l=[0,]
c=0
for i in s:
    if i=='B' and c>0:
        c-=1
    elif i=='F':
        c+=2
    if c not in l:
        l.append(c)
print(l)