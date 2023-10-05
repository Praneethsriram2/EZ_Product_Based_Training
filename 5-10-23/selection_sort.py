'''l=list(map(int,input("Enter the elements:").split()))
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("Sorted array is:")
for i in range(len(l)):
    print(l[i],end=' ')'''
l=list(map(int,input("Enter the elements:").split()))
for i in range(len(l)-1):
    mini_ind=i
    for j in range(i+1,len(l)):
        if(l[j]<l[mini_ind]):
            mini_ind=j
    l[i],l[mini_ind]=l[mini_ind],l[i]
print("Array after sorting:")
for i in range(len(l)):
    print(l[i],end=' ')