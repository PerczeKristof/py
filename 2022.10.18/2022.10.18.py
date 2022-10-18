"""

import random
szam=int(input(f"Kérlek add meg a számot, amire gondoltál(1-től 100-ig)"))
tipp=random.randint(1,100)
lepes=1
if szam<1 or szam>100:
    print(f"Kérlek 1-től 100-ig adj meg számot.")
print(f"a gép erre gondolt:",tipp)
while tipp!=szam:
    if tipp>szam:
        tipp=random.randint(1,tipp)
        lepes+=1
    elif tipp<szam:
        lepes+=1
        tipp=random.randint(tipp,100)
    elif tipp==szam:
        lepes+=1
        print(f"{lepes} -ből találtad ki")
    else:
        print(f"Nem nyert :D") 
    
a=int (input(f"Adj meg egy számot! "))
b=int (input(f"Adj meg egy számot! "))

print(f"{a+2 *b}") 


szam=int(input(f"add meg a számot! "))
db=0
while szam!=0:
    if szam>5:
        db+=1
    szam=int(input(f"add meg a számot!: "))
print(f"Kiléptem a ciklusból!: {db}") 

import math
homerseklet=int(input(f"Add meg a hőmérsékletet: "))
osszeg=0
db=0
atlag=0
while homerseklet>0:
    osszeg+=homerseklet #osszeg=osszeg+homerseklet
    db+=1
    homerseklet=int(input(f"Add meg a hőmérsékletet: "))
atlag=round((osszeg/db),1)
print(f"átlag:{atlag} ") 

homerseklet=int(input(f"Add meg a hőmérsékletet: "))
db=1

while homerseklet>-5:
    homerseklet=int(input(f"Add meg a hőmérsékletet: "))
    if homerseklet>10:
        db+=1
print(f"{db} db 10 foknál magasabb hőmérsékletet adott meg! ") 

szam=int(input(f"Add meg a számot! "))

paros=0
paratlan=0

while szam!=0:
    if szam%2:
        szam=int(input(f"Add meg a számot! "))
        paratlan+=1
    else:
        szam=int(input(f"Add meg a számot! "))
        paros+=1
print(f"{paros} db páros számot és {paratlan} db páratlan számot adtál meg! ") 

szam=int(input(f"Add meg a számot! "))
osszeg=szam


while szam!=0:
    szam=int(input(f"Add meg a számot! "))
    osszeg+=szam
print(f"bekért számok összege= {osszeg} ") 

szam=int(input(f"Add meg a számot! "))
osszeg=szam

while szam!=0:
    szam=int(input(f"Add meg a számot! "))

print(f" az összege= {osszeg}") 

n=int(input(f"Sorok száma! "))
m=int(input(f"Oszlopok száma! "))

i=1
while i<11:
    j=0
    while j<11:
        print(i*j, end="\t")
        j+=1
    print()
    i+=1 """





