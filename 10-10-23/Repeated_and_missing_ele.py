#Brute force approach
'''n=int(input())
l=list(map(int,input().split()))
l.sort()
print(l)
for i in range(1,n+1):
    if i not in l:
        print("Missing element:",i)
        break
c=[0]*(len(l)+1)
for i in range(n):
    c[l[i]]+=1
print(c)
for i in range(len(c)):
    if c[i]>1:
        print("Repeated element is:",i)'''
#Using dict
'''n=int(input())
arr=list(map(int,input().split()))
hashmap={}
#print(hashmap)
m=len(arr)
for i in range(m):
    if arr[i] not in hashmap:
        hashmap[arr[i]]=1
    else:
        hashmap[arr[i]]+=1
for i in range(1,n+1):
    if i not in hashmap:
        print(f"Missing Element is:- {i}")
    elif hashmap[i]>1:
        print(f"Repeated Element is:- {i}")'''
#Using bitwise operators
n=int(input())
arr=list(map(int,input().split()))
s=set(arr)
r=0
for i in arr:
    r^=i
for i in s:
    r^=i
print("Repeated element is:",r)