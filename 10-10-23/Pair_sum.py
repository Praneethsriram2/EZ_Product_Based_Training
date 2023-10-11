def is_pair_exist(l,target):
    i=0
    j=len(l)-1
    while i<j:
        if l[i]+l[j]==target:
            return True
        elif l[i]+l[j]<target:
            i+=1
        elif l[i]+l[j]>target:
            j-=1
    return False
l=list(map(int,input("Enter the elements:").split()))
l.sort()
target=int(input("Enter target variable:"))
print(is_pair_exist(l,target))