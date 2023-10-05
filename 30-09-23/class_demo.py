class Praneeth():
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def oper(self,a,b):
        print("Reverse of string:",a[::-1])
        print("Square is:",b**2)
    def display_results(self):
        print("Length is",len(self.c))
        print("Modulus is:",(self.a)%(self.b))
a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=input("Enter a string:")
obj=Praneeth(a,b,c)
obj.oper(input("Enter a string:"),int(input("Enter a number:")))
#or use a and b directly in the above line
obj.display_results()