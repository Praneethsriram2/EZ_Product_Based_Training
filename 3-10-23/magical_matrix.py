n=int(input("Enter the row size:"))
mat=[]
num=1
for i in range(n):
    l=[]
    for j in range(n):
        l.append(-1)
    mat.append(l)
for i in mat:
    print(i)
i=0
j=(n-1)//2
while(num<=n*n):
    if (i==-1 and j==n):
        i+=2
        j-=1
    elif i==-1:
        i=n-1
    elif j==n:
        j=0
    elif mat[i][j]!=-1:
        i+=2
        j-=1
    mat[i][j]=num
    num+=1
    i-=1
    j+=1
for i in mat:
    print(i)    