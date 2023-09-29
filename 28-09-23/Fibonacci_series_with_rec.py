def fibo(a,b,n):
    if n<=0:
        return 
    print(a+b,end=' ')
    fibo(b,a+b,n-1)
n=int(input("Enter the length of series:"))
if(n<=0):
    print("Enter valid length")
elif(n==1):
    print("Series is: 0")
else:
    print("0 1",end=' ')
    fibo(0,1,n)