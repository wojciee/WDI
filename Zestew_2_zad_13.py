


"""Zad 13 Napisz funkcję, która w napisie znajduje jego fragment,
który stanowi anagram do innego fragmentu tego napisu.
Funkcja powinna znajdować wszystkie takie anagramy,
które są dłuższe niż 2 (bez znaków niedrukowalnych)
 i zwracać je w liście uporządkowane długością."""




zdanie=""
zdanie=zdanie.lower()
lista=zdanie.split(" ")
podobne=[]
p1=False
p2=False

petla=len(lista)
petla2=1

for l in range(0,len(lista)):
    for k in range(petla2,petla):
        for znak in lista[l]:            
            if(znak in lista[k])&(len(lista[l])==len(lista[k]))&(len(lista[l])>2)&(lista[l]!=lista[k]):
                p1=True
               
            else:
                p1=False
                break

        for znak2 in lista[k]:            
            if(znak2 in lista[l])&(len(lista[l])==len(lista[k]))&(len(lista[k])>2)&(lista[l]!=lista[k]):
                p2=True      
            else:
                p2=False
                break
            
                                                          
        if(p1==True)&(p2==True):
            podobne.append(lista[l])
            podobne.append(lista[k])
            p1=False
            p2=False 
        
    petla2=petla2+1
    


print(podobne) 

podobne2=[]


for ele in podobne:
    if(ele not in podobne2):
        podobne2.append(ele)


print("-----------------------przed sortowaniem --------------------------")
print(podobne2)


n = len(podobne2)
while n > 1:
    zamien = False
    for l in range(0, n-1):
        if len(podobne2[l]) > len(podobne2[l+1]):
            podobne2[l], podobne2[l+1] = podobne2[l+1], podobne2[l]
            zamien = True
            
    n -= 1
    if zamien == False: break

        
    


print("-----------------------po sortowaniu --------------------------")
print(podobne2)


"""krasa Arska raska sarka askar kasar Raksa sakra Arkas Araks Karsa rakas Karas Sakar Skara Askra"""
