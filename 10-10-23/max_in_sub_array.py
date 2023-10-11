l=list(map(int,input().split()))
k=int(input())
mx=-9999
for i in range(len(l)-(k-1)):
    if sum(l[i:i+k])>mx:
        mx=sum(l[i:i+k])
print("Maximum sum is:",mx)