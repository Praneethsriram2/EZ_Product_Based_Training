def xor(n):
    if n%4==0:
        return(n)
    elif n%4==1:
        return(1)
    elif n%4==2:
        return(n+1)
    else:
        return 0
n1=int(input("Enter starting value:"))
n2=int(input("Enter ending value:"))
print(xor(n2)^xor(n1-1))
s=0
for i in range(n1,n2+1):
    s^=i
print(s)