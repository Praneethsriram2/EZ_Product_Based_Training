#Generate all type of n paired brackets of one type i.e., '()'
def generate_paranthesis(n):
    result=[]
    def generate(partial,left,right):
        if left>0:
            generate(partial+'(',left-1,right)
        if right>left:
            generate(partial+')',left,right-1)
        if left==0 and right==0:
            result.append(partial)
        return result
    return generate('',n,n)
n=int(input())
result=generate_paranthesis(n)
#print(generate_paranthesis(n))
for i in result:
    print(i)