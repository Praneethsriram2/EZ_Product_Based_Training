n=input()
k=[]
l=[]
for i in range(len(n)):
    if i%2!=0:
        k.append(n[i])
for i in k:
    l.append(int(i)**2)
for i in range(len(l)-1):
    print(l[i],end='')
