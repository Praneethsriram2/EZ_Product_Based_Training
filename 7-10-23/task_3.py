n=list(map(int,input().split()))
m=n[0]
k=n[1]
l=list(map(int,input().split()))[:m]
c=0
for i in range(len(l)):
    if l[i]==k:
        c+=1
if(c<=k):
    print(c)
else:
    print(k)