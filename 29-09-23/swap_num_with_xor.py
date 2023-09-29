a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
a=a^b #a=100^200
b=a^b #b=100^200^200 ans 200 200 cancelled b=100
a=a^b #a=100^200^100 ans 100 gets cancelled a=200
print("a=",a,"b=",b)