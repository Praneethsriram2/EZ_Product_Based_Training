def divide(arr,n):
    c=0
    if len(arr)==1:
        return 0
    left=arr[:len(arr)//2]
    right=arr[len(arr)//2:]
    c+=divide(left,n)
    c+=divide(right,n)
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            k+=1
            i+=1
        else:
            arr[k]=right[j]
            k+=1
            c+=(len(left)-i)
            j+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    return c

arr=list(map(int,input().split()))
count=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            count+=1
print(count)
print(divide(arr,len(arr)))