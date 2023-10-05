##Check wether the given string of paranthesis is balanced or not with function
def valid_paranthesis(s):
    stack=[]
    n=len(s)
    flag=1
    if n%2==0:
        for i in range(n):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            elif s[i]==')' or s[i]=='}' or s[i]==']':
                if not stack:
                    flag=0
                    break
                elif (s[i]==')' and stack[-1]=='(') or (s[i]=='}' and stack[-1]=='{') or (s[i]==']' and stack[-1]=='['):
                    stack.pop()
                else:
                    flag=0
                    break
            else:
                flag=0
                break
    else:
        flag=0
    if flag==0 or stack:
        return False
    else:
        return True
s=input()
print(valid_paranthesis(s))