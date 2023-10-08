def binary_search(a,first,last,se):
    mid=(first+last)//2
    if se==a[mid]:
        return f"Element found at index {mid}"
    elif first==last:
        return False
    elif se<a[mid]:
        return binary_search(a,first,mid-1,se)
    elif se>a[mid]:
        return binary_search(a,mid+1,last,se)
a=list(map(int,input("Enter the elements:").split()))
a.sort()
print(a)
se=int(input("Enter the element to search:"))
print(binary_search(a,0,len(a),se))