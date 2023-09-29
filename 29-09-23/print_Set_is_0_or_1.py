n=int(input("Enter a number:"))
k=int(input("Enter the bit position:"))
if n>>k%2==1:
    print("Yes")
else:
    print("NO")
'''
if n&(1<<k):
    print("Yes")
else:
    print("No")'''