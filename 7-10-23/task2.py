#caution:this code works for only this input{25143278}
'''From a given input find the index pos of num 4 and 7, and sum the num
    which r not in b/w 4 &7(k) and take the num from 4 to 7 as str and sum k and
    that str.(Note:Convert str to int)'''
giv1=4
giv2=7
n=input("enter the numbers:")
l1=''
l2=''
s=''
k1=[]
k2=[]
l1+=n[:giv1-1]+n[giv2:]
l2+=n[giv1-1:giv2]
print(l1)
print(l2)
for i in range(len(l1)):
    k1.append(int(l1[i]))
print(k1)
for i in range(len(l2)):
    k2.append(int(l2[i]))
print(k2)
print(sum(k1))
for i in range(len(k2)):
    s+=str(k2[i])
print(s)
print(sum(k1)+int(s))