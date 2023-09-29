#sum of n naturals
'''n=int(input("Enter a number:"))
s=0
for i in range(n+1):
    s+=i
print(s)'''
#sum of digits in a number
#using while loop
'''n=int(input("Enter a number:"))
s=0
if(n<0):
    n=n*(-1)
while(n>0):
    r=n%10
    s+=r
    n=n//10
print(s)'''
#using for loop by taking as string
'''num=input("Enter a number:")
s=0
if(num[0]=='-'):
    num=num[1:]
#to convert from string to int ==> n=int(num)
for i in num:
    s+=int(i)
print(s)'''
#using for loop by taking as int
n=int(input("Enter a number:"))
temp=n
s=0
for i in range(1,n,n//10):
    s=s+int(temp%10)
    temp=temp//10
print(s)