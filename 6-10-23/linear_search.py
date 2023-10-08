def linear_search(l,se):
    h=0
    for i in range(len(l)):
        if l[i]==se:
            h=1
            print(f"{se} element found at index {i}")
    if (h==1):
        return True
    else:
        print("Element not found")
        return False
l=list(map(int,input("Enter the elements:").split()))
se=int(input("Enter the search element:"))
print(linear_search(l,se))