arr=list(map(int,input().split()))
n=int(input())
queries=[]
for i in range(n):
    queries.append(list(map(int,input().split())))
print(queries)
#Brute Force Method:- O(n^2)
print("Method - 1:- \n")
for i in range(n):
    s=sum(arr[queries[i][0]:queries[i][1]+1])
    print(f"Query {i+1} Sum is:- {s}")
#Store the sum till that index in an array(Method - 2):- O(n)
print("\nMethod - 2:- \n")
prifix_sum=[]
for i in range(len(arr)):
    if i==0:
        prifix_sum.append(arr[i])
    else:
        prifix_sum.append(prifix_sum[i-1]+arr[i])
for i in range(n):
    if queries[i][0]==0:
        ini_sum=0
    else:
        ini_sum=prifix_sum[queries[i][0]-1]
    final_sum=prifix_sum[queries[i][1]]
    print(f"Query {i+1} Sum is:- {final_sum-ini_sum}")