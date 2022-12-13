import random

"""
Zadanie 15.
Utwórz macierz o wymiarach 
(2n−1)×(2n−1)wypełnioną zerami. Napisz funkcje umożliwiające:s
tworzenie obramowania (brzegi marcierzy) wprowadzoną przez użytkownika liczbą,
uzupełnienie przekątnych wprowadzoną przez użytkownika liczbą (osobno dla każdej przekątnej i razem),
tworzenie obramowania wprowadzoną przez użytkownika liczbą na zmianę z 0.
"""

w=11
s=11
l=2
m=[]

for i in range(0,w):
    m.append([])
    for j in range(0,s):
        if(i==0)|(i==(w-1)):
            m[i].append(l)
        else:
            if(j==0)|(j==(s-1)):
                m[i].append(l)
            else:
                m[i].append(0)


for k in range(0,w):
    print(m[k])
print("=================")
p1=5
p2=3
x=0
y=0
while(x<w)&(y<s):
    m[y][x]=p1
    x+=1
    y+=1


x=s-1
y=0

while(x>=0)&(y<s):
    m[y][x]=p2
    x-=1
    y+=1



for k in range(0,w):
    print(m[k])

print("=================")

for r in range (0,w):
    for rr in range (0,s):
        if (r==0)&(rr%2==0):
            m[r][rr]=0
        elif(r==(w-1))&(rr%2==0):
            m[r][rr]=0
        elif(rr==0)&(r%2==0):
            m[r][rr]=0
        elif(rr==(s-1))&(r%2==0):
            m[r][rr]=0


for k in range(0,w):
    print(m[k])
