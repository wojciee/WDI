"""
Zadanie 14.
Napisz program, który rekurencyjnie i iteracyjnie szuka w napisie (w zależności od tego,
czego chce użytkownik): spółgłosek, samogłosek, cyfr i znaków specjalnych.
Na końcu zwróć ich ilość oraz czas potrzebny do wyznaczenia.
Wygeneruj losowe napisy o długości zadanej przez użytkownika.
"""


import time
import random




samogl=["a","ą","e","ę","i","o","u","y"]
spolgl=["b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","w","z","ź","ż"]
cyfry=["1","2","3","4","5","6","7","8","9","0"]
zspe=["!","@","#","$","%","^","&","*","(",")","?","/",":","-","+","=","_",]



dl=10000
nowy=""
znak=0
for q in range(0,dl):

    wybor=random.randint(1,4)
    if (wybor==1):
        znak=random.randint(0,len(samogl)-1)
        nowy=nowy+samogl[znak]
    elif (wybor==2):
        znak=random.randint(0,len(spolgl)-1)
        nowy=nowy+spolgl[znak]
    elif (wybor==3):
        znak=random.randint(0,len(cyfry)-1)
        nowy=nowy+cyfry[znak]
    elif (wybor==4):
        znak=random.randint(0,len(zspe)-1)
        nowy=nowy+zspe[znak]



sp=0
sa=0
cy=0
zs=0

start_time=time.time()

for i in nowy:
    for j in spolgl:
        if(i==j):
            sp+=1
    for k in samogl:
        if(k==i):
            sa+=1 
    for l in cyfry:
        if(i==l):
            cy+=1
    for m in zspe:
        if(i==m):
            zs+=1  

end_time = time.time()

t1=end_time-start_time

print(sp,sa,cy,zs)

sp2=0
sa2=0
cy2=0
zs2=0

start_time2=time.time()


for m in nowy:
    if m in spolgl:
        sp2+=1
    if m in samogl:
        sa2+=1
    if m in cyfry:
        cy2+=1
    if m in zspe:
        zs2+=1

end_time2 = time.time()

t2=end_time2-start_time2



print(sp2,sa2,cy2,zs2)



print(nowy)
print(t1,t2)