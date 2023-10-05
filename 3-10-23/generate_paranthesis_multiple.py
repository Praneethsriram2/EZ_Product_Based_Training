#Generate all type of n paired brackets of all types i.e., '(),{},[]'
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

def generate_paranthesis(n):
    result=[]
    def generate(partial,left,right):
        if left>0:
            generate(partial+'(',left-1,right)
        if right>left:
            generate(partial+')',left,right-1)
        if left>0:
            generate(partial+'{',left-1,right)
        if right>left:
            generate(partial+'}',left,right-1)
        if left>0:
            generate(partial+'[',left-1,right)
        if right>left:
            generate(partial+']',left,right-1)
        if left==0 and right==0:
            result.append(partial)
        return result
    return generate('',n,n)
n=int(input())
result=generate_paranthesis(n)
final_result=[]
for i in result:
    print(i)
print()
for i in result:
    if valid_paranthesis(i):
        if n==2:
            if ('(' in i and '{' in i) or ('(' in i and '[' in i) or ('[' in i and '(' in i) or ('[' in i and '{' in i) or ('{' in i and '[' in i) or ('{' in i and '(' in i):
                final_result.append(i)
        else:
            if '{' in i and '(' in i and '[' in i:
                final_result.append(i)
for i in final_result:
    print(i)