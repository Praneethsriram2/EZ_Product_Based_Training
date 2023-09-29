#Get one number as input, find sum of the digits of the given number with both for loop and while loop.
num=(input("Enter Number: "))
if num[0]=='-':
    num=num[1:]
n=int(num)
s=0
while(n>0):
    s+=(n%10)
    n=n//10
print(f"Sum using while loop:- {s}")
s=0
n=int(num)
for i in range(1,n,n//10):
    s+=n%10
    n=n//10
print(f"Sum using for loop:- {s}")