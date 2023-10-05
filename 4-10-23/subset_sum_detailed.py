res=[]
def a(arr,n,target,l):
    if target == 0:
        if l not in res:
            res.append(l)
        return 
    if n>=len(arr) and target!=0:
        return
    if arr[n]>target:
        a(arr,n+1,target,l)
    a(arr,n+1,target,l)
    a(arr,n+1,target-arr[n],l+" "+str(arr[n]))
    return res
arr = list(map(int,input().split(" ")))
target= int(input())
n = len(arr)
if a(arr, 0, target,''):
    if not res:
        print("No Subset")
    for i in res:
        print(i.strip())
else:
    print("No Subset")