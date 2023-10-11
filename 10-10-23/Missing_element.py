#brute force approach
'''def missing_ele(l):
    for i in range(len(l)):
        if l[i]!=i:
            return i
l=list(map(int,input().split()))
l.sort()
print(missing_ele(l))'''
#using dict
'''n=int(input())
l=list(map(int,input().split()))
d={}
for i in range(len(l)):
    if l[i] not in d:
        d[l[i]]=1
print(d)
for i in range(1,n+1):
    if i not in d:
        print(i)'''
#using bitwise operators
n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    s^=l[i]
for i in range(n+1):
    s^=i
print(s)