import random

def check(niz, val):                    #Funkcija vraca true ako su svi el. niz-a 
    return(all(x != val for x in niz))  #razliciti od random vrednosti val
def rand_num():
    return random.randrange(1, 39)      #Funkcija vraca random broj od 1 do 39
    
niz = [0] * 7 
val = rand_num()
x = 0 
while True:
    if(check(niz, val)):
      niz[x] = val
      x += 1
    else: 
      val = rand_num()
    if x > 6:
      break
niz.sort()   #Dodata funkcija za sortiranje liste
print ("Vasa loto kombinacija je: ", niz)
