"""
Zadanie 10.
Na szachownicy o wymiarach 100 na 100 umieszczamy N gońców (N<100). Położenie gońców jest opisywane przez tablicę
dane = [(w1, k1), (w2, k2), (w3, k3), ..., (wN, kN)] 
Proszę napisać funkcję, która zwróci położenie gońców wzajemnie się szachujących.
Do funkcji należy przekazać położenie gońców. Należy zwizualizować rozkład gońców na szachownicy.
Testy powinny uwzględniać między innymi:

Przypadek, w którym nie występuje szachowanie.
Przypadek, w którym szachują się dwa gońce.
Przypadek, w którym szachują się więcej niż dwa gońce.
"""


class Szachowanie:


    s=10
    w=10

    def czy_sie_szachuja(self, dane):
        
        li=0
        x=0
        y=0
        macierz=[]
        szach=[]
        szach2=[]
        for i in range(0,self.w):
            macierz.append([])
            for j in range (0,self.s):
                macierz[i].append(0)



        
        ldane=len(dane) 

        for e in range (0,ldane):
            macierz[dane[e][1]-1][dane[e][0]-1]=1





        for i in range(0,self.w):
                print(macierz[i])

        for q in range(0,ldane-1): 

            


            wg=dane[q][1]-1
            sg=dane[q][0]-1

        
            x=sg
            y=wg


            #od prawa dol
            while 1>0:
                
                if(x==sg)&(y==wg):
                    y+=1
                    x+=1
                    
                elif (y<self.w)&(x<self.s):
                        
                    
                    for wl in range(1,ldane):
                    
                        if (x==dane[wl][0]-1)&(y==dane[wl][1]-1):
                            szach.append([])
                            szach[li].append(dane[q][0])
                            szach[li].append(dane[q][1])
                            szach[li].append(dane[wl][0])
                            szach[li].append(dane[wl][1])
                            
                            li+=1
                        if (x==dane[wl][0]-1)&(y==dane[wl][1]-1):
                            szach.append([])
                            szach[li].append(dane[wl][0])
                            szach[li].append(dane[wl][1])
                            szach[li].append(dane[q][0])
                            szach[li].append(dane[q][1])
                            li+=1

                    y+=1
                    x+=1
                    
                    
                else:
                    x=sg
                    y=wg
                    break

            #lewo dol



            while 1>0:
                if(x==sg)&(y==wg):
                    y+=1
                    x-=1
                    
                elif (y<self.w)&(x<self.s)&(x>=0)&(y>=0):
                    
                    for wl in range(1,ldane):  
                        if (x==dane[wl][0]-1)&(y==dane[wl][1]-1):
                            szach.append([])
                            szach[li].append(dane[q][0])
                            szach[li].append(dane[q][1])                   
                            szach[li].append(dane[wl][0])
                            szach[li].append(dane[wl][1])                    
                            li+=1
                        if (x==dane[wl][0]-1)&(y==dane[wl][1]-1):
                            szach.append([])
                            szach[li].append(dane[wl][0])
                            szach[li].append(dane[wl][1])
                            szach[li].append(dane[q][0])
                            szach[li].append(dane[q][1])
                            li+=1
                    y+=1
                    x-=1
                    
                else:
                    x=sg
                    y=wg
                    break
            

            #prawo gora
            while 1>0:
                if(x==sg)&(y==wg):
                    y-=1
                    x+=1
                    
                elif (y<self.w)&(x<self.s)&(y>=0):
                    

                    for wl in range(1,ldane):  
                        if (x==dane[wl][0]-1)&(y==dane[wl][1]-1):
                            szach.append([])
                            szach[li].append(dane[q][0])
                            szach[li].append(dane[q][1])
                            szach[li].append(dane[wl][0])
                            szach[li].append(dane[wl][1])
                            li+=1
                        if (x==dane[wl][0]-1)&(y==dane[wl][1]-1):
                            szach.append([])
                            szach[li].append(dane[wl][0])
                            szach[li].append(dane[wl][1])
                            szach[li].append(dane[q][0])
                            szach[li].append(dane[q][1])
                            li+=1

                    y-=1
                    x+=1
                        
            
                else:
                    x=sg
                    y=wg
                    break
            
            #lewo gora
            while 1>0:
                if(x==sg)&(y==wg):
                    y-=1
                    x-=1
                    
                elif (y<self.w)&(x<self.s)&(x>=0)&(y>=0):
                    
                    
                    
                    for wl in range(1,ldane):  
                        if (x==dane[wl][0]-1)&(y==dane[wl][1]-1):
                            szach.append([])
                            szach[li].append(dane[q][0])
                            szach[li].append(dane[q][1])
                            szach[li].append(dane[wl][0])
                            szach[li].append(dane[wl][1])
                            li+=1
                        if (x==dane[wl][0]-1)&(y==dane[wl][1]-1):
                            szach.append([])
                            szach[li].append(dane[wl][0])
                            szach[li].append(dane[wl][1])
                            szach[li].append(dane[q][0])
                            szach[li].append(dane[q][1])
                            li+=1
                    y-=1
                    x-=1
                    
                else:
                    x=sg
                    y=wg
                    break
        print("Polozenie goncow wzajemnie sie szachujacych: ")
        
        for aa in szach:
            if aa not in szach2:
                szach2.append(aa)
        print(szach2)
    
    
    
               
szach=Szachowanie()
szach.czy_sie_szachuja([[1,2],[2,1]])


print("===")

class Wymiary(Szachowanie):
    def wyy(self,a,b):
        self.w=a
        self.s=b

w1=Wymiary()
w1.wyy(10,30)
w1.czy_sie_szachuja([[1,2],[3,1]])




