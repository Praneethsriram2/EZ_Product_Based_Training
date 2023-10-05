'''print the count of how many comparisions satisfy the below condition
    i<j =>right side[9,6,8,4]
    a[i]>a[j]'''
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            c+=1
print(c)