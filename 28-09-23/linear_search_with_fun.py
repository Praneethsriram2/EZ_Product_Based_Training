def linear_se(l,se):
    for i in l:
        if i==se:
            return True
    return False
l=list(map(int,input("Enter elements:").split()))
se=int(input("Enter search element:"))
print(linear_se(l,se))