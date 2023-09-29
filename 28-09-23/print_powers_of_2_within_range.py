rang=list(map(int,input("Enter the range:").split()))
size=int(input("Enter size of array:"))
l=list(map(int,input("Enter the elements:").split()))
print("Even are:")
if(len(l)>size):
    print("List oversized")
else:
    for i in l:
        if i>=rang[0] and i<=rang[1]:
            if i%2==0:
                print(i)
    print("Powers of of 2 are:")
    for i in l:
        if i>=rang[0] and i<=rang[1]:
            for j in range(i):
                if 2**j==i:
                    print(i)