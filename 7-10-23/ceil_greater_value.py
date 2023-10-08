#printion the ceil(greater value) if element not found
l=list(map(int,input().split()))
l.sort()
key=int(input())
high=len(l)-1
low=0
c=0
ceil=-1
while(low<=high):
    mid=low+(high-low)//2
    if(l[mid]==key):
        c+=1
        print("element found",mid+1)
        break
    elif(key>l[mid]):
        
        low=mid+1
    elif(key<l[mid]):
        ceil=l[mid]
        high=mid-1
print(ceil)