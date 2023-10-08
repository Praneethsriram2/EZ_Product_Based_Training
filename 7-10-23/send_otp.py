'''n=input()
k=[]
l=[]
for i in range(len(n)):
    if i%2!=0:
        k.append(n[i])
for i in k:
    l.append(int(i)**2)
print("OTP")
for i in range(len(l)-1):
    print(l[i],end='')'''
n=input()
op=''
for i in range(1,len(n),2):
    op+=str(int(n[i])**2)
print(op[:4])