#the below code time com is O(n^2).
'''def two_pointer(l,target):
    for i in range(len(l)):
        for j in range(len(l)-1,-1,-1):
            if l[i]+l[j]==target:
                return i+1,j+1
l=list(map(int,input("Enter the elements:").split()))
l.sort()
target=int(input("Enter the target:"))
print(two_pointer(l,target))'''
#the below code time com is O(n).
l=list(map(int,input("Enter the elements:").split()))
l.sort()
target=int(input("Enter the target:"))
i=0
j=len(l)-1
while(i<j):
    if l[i]+l[j]==target:
        print(i+1,j+1)
        break
    elif l[i]+l[j]>target:
        j-=1
    else:
        i+=1