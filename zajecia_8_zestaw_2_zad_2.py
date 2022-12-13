"""
Zad 2
Napisz funkcję create_3d(int N), która tworzy tablicę trójwymiarową o rozmiarze 
N×N×N, gdzie Njest pobierane od użytkownika.
Funkcja powinna zwracać tablicę trójwymiarową wypełnioną liczbami losowymi,
które następnie należy odpowiednio uszeregować w funkcji arrange_3d(argumentem jest tablica).
Porządkowanie powinno być przeprowadzone względem trzeciego wymiaru – na wyznaczonej
przez niego płaszczyźnie należy uporządkować elementy rosnąco po spirali.
Wykorzystując funkcję save_positions(argumentem jest tablica) należy wpisać do 
pliku stare i nowe pozycje elementu w danej płaszczyźnie.

"""
import random

r=[]

def create_3d(N):

  

    p=[]
    

    for i in range(0,N):
        p.append([])
        for j in range(0,N):
            p[i].append([])
            for k in range(0,N):
                p[i][j].append(random.randint(0,9))
                r.append(p[i][j][k])
 
    return p

    

def arrange_3d(r):
    n = len(r)
        
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if r[l] > r[l+1]:
                r[l], r[l+1] = r[l+1], r[l]
                zamien = True
                
        n -= 1
        if zamien == False: break
    return r
    
def save_positions(p, r):
    filepath="p.txt"
    f = open(filepath, "w")
    f.write(str(p))
    f.write("Po ulozeniu: ")
    f.write(str(r))


print(create_3d(3))

print(arrange_3d(r))

save_positions(create_3d(3),r)