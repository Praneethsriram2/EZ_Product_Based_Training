n=input("Enter the input:")
k=0
for i in range(len(n)):
    if not ((n[i]>='A' and n[i]<='Z') or (n[i]>='a' and n[i]<='z') or (n[i]>='0' and n[i]<='9')):
        k+=i
temp=n
print(temp)
print(k)
temp=temp[:k]+temp[k+1:]
print(temp)
temp=temp[::-1]
temp=temp[:k]+n[k]+temp[k:]
print(temp)