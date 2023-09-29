'''r=int(input("Enter the size of row:"))
mat=[]
res=[]
print("Enter the elements:")
for i in range(r):
    l=list(map(int,input().split()))
    mat.append(l)
for i in range(r):
    print(mat[i])
for i in range(r):
    temp=[]
    for j in range(r):
        temp.append(mat[j][i])
    res.append(temp)
print(res)
for i in range(r):
    print(res[i])
for i in range(r):
    res[i]=res[i][::-1]
print("Matrix after rotating 90 deg is:")
for i in range(r):
    print(res[i]) '''
r=int(input("Enter the row size:"))
c=int(input("Enter col size:"))
mat=[]
print("Enter the elements:")
for i in range(r):
    a=[]
    for j in range(c):
        x=int(input())
        a.append(x)
    mat.append(a)
print("The matrix is:")
for i in range(r):
    for j in range(c):
        print(mat[i][j],end=" ")
    print()
for i in range(r):
    for j in range(c-1,-1,-1):
        
        