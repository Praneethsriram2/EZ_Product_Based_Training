#Check wether the given string of paranthesis is balanced or not without functions
s=input()
n=len(s)
stack=[]
flag=1
if n%2==0:
    for i in range(n):
        if s[i]=='(' or s[i]=='[' or s[i]=='{':
            stack.append(s[i])
        elif s[i]==')' or s[i]==']' or s[i]=='}':
            if stack:
                if (stack[-1]=='(' and s[i]==')') or (stack[-1]=='[' and s[i]==']') or (stack[-1]=='{' and s[i]=='}'):
                    stack.pop()
                else:
                    flag=0
                    break
            else:
                flag=0
                break
        else:
            flag=0
            break
else:
    flag=0
if flag==0 or stack:
    print(False)
else:
    print(True)