'''Print a number which is not repeated twice.
Note:Every number should repeat twice except that one number.'''
l=list(map(int,input().split()))
c=0
for i in l:
    c=c^i
print(c)