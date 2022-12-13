
l1=1024
l2=512
l3=256

dz1=[]
dz2=[]
la=[]

la.append(l1)
la.append(l2)
la.append(l3)
la.sort()
la.reverse()
n=la[0]


for i in range(1,l1+1):
    if(l1%i==0):
        dz1.append(i)


for i in range(1,l2+1):
    if(l2%i==0):
        dz1.append(i)

for i in range(1,l3+1):
    if(l3%i==0):
      dz1.append(i)



for i in range(1,n+1):
    if dz1.count(i)==3:
        dz2.append(i)


dz2.sort()
dz2.reverse()
print(dz2[0])





