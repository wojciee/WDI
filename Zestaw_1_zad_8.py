"""
Zad 8
Wykorzystując wzór , proszę wyznaczyć liczbę 
e z dokładnością do wpisanej przez użytkownika liczby miejsc dziesiętnych. Różnice pomiędzy kolejnymi przybliżeniami a przybliżeniem ostatnim należy przechować w liście i na sam koniec wypisać 
10 początkowych, 
10 środkowych i 10 końcowych elementów listy.
"""



e=1
s=1



for i in range (2,50):
    for j in range (1,i):
        s=s*j
        
    
    e=e+1/s
    s=1





i=int(input("zaokr: "))
print(round(e,i))

licznik=0
stre=list(str(e))
stre.pop(0)
stre.pop(0)
for znak in stre:
    licznik+=1

przy_ost=round(e,licznik)

roznica_prz=[]

for k in range(1,licznik+1):
    roznica_prz.append(round(e,k)-przy_ost)
    


print("--------10 poczatkowych--------------")
for l in range(0,10):
    print(roznica_prz[l])

print("-------10 koncowych---------------")
roznica_prz.reverse()
for l in range(0,10):
    print(roznica_prz[l])
roznica_prz.reverse()
print("---------10 srodkowych-------------")
if(licznik%2==0):
    for m in range(1,11):
        print(roznica_prz[(int(licznik/2-6)+m)])
        
print("----------------------")


       
    