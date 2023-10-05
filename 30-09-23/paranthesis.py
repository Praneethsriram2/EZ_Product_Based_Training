k=input("Enter the input:")
s=[]
n=len(k)
c=0
flag=1
if n%2!=0:
    print("Invalid input")
else:
    if k[0]==']' or k[0]=='}' or k[0]==')':
        print(False)
    for i in range(n):
        if k[i]=='{' or k[i]=='(' or k[i]=='[':
            s.append(k[i])
            c+=1
        elif k[i]=='}' or k[i]==']' or k[i]==')':
            if s==[]:
                flag=0
                break
            if(s[-1]=='{' and k[i]=='}') or (s[-1]=='(' and k[i]==')') or (s[-1]=='[' and k[i]==']'):
                s.pop()
                c-=1
            else:
                flag=0
                break
        else:
            flag=-1
            break
    if c!=0 and flag==0:
        print("Not matching")
    elif flag==-1:
        print("Invalid input")
    else:
        print("Matching")