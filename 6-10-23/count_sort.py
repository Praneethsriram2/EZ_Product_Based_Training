def count_sort(a):
    count_arr=[]
    upd_count=[]
    result=[]
    for i in range(max(a)+1):#or use len(a)->as the element is greater than no.of elements
        count_arr.append(0)
    for i in range(len(a)):
        count_arr[a[i]]+=1
    print("Count array is:",count_arr)
    for i in range(max(a)+1):#or use len(a)->as the element is greater than no.of elements
        if i==0:
            upd_count.append(count_arr[i])
        else:
            upd_count.append(upd_count[i-1]+count_arr[i])
    print("Updated_count array is:",upd_count)
    for i in range(len(a)):
        result.append(0)
    for i in range(len(a)):
        result[upd_count[a[i]]-1]=a[i]
        upd_count[a[i]]-=1
    return result
a=list(map(int,input("enter the elements:").split()))
print("After sorting:",count_sort(a))