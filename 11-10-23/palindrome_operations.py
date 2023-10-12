s=input("Enter a string:")
l=[]
pal=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        l.append(s[i:j])
for i in l:
    if i==i[::-1] and i not in pal:
        pal.append(i)
print(len(pal))
print(f"All possible palindromes are:\n{pal}")
mx=-1
for i in pal:
    if len(i)>mx:
        mx=len(i)
print(f"Max length of a pal string is:{mx}")
for i in pal:
    if len(i)==mx:
        print(f"Pal string with max length is:{i}")
print("Shortest pal strings are:")
for i in pal:
    if len(i)==1:
        print(i,end=' ')