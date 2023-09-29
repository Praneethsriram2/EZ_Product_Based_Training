'''l=list(map(int,input().split()))
k=[]
f=0
for i in range(len(l)):
    if l[i]>=0:
        k.append(l[i])
for i in range(len(k)):
    for j in range(len(k)-1-i):
        if(k[j]>k[j+1]):
            temp=k[j]
            k[j]=k[j+1]
            k[j+1]=temp
# above u can also use o(1)...
for i in range(len(k)):
    if i!=k[i]:
        print(i)
        f=1
        break
if(f==0):
    print(k[-1]+1)'''
l=list(map(int,input("Enter the elements:").split()))
d=dict()
flag=0
for i in l:
    if i>=0 and i not in d:
        d[i]=1
for i in range(len(l)):
    if i not in d:
        print(i)
        flag=1
        break
mx=-1
for i in l:
    if mx<i:
        mx=i
# or use max() function...
if flag==0:
    print(mx+1)