def sum_of_array(n):
    s=0
    for i in n:
       s+=i
    return s
def sum_rec(n):
    if n:
        return n[0]+sum_rec(n[1:])
    else:
        return 0
n=list(map(int,input("Enter elements:").split()))
print(sum_of_array(n))
print(sum_rec(n))