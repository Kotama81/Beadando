import random #importaltam a random modult
import kezek #importaltam a kezek.py-t hogy elerjem a main.py-bol

korok_szama = int(input("Hány körből álljon a játék?\nÍrj be egy számot egytől ötig! ")) #bekerem a usertol a játék korok számát 1-5ig
if korok_szama > 5 or korok_szama < 0 :  #ha nem 1-5 ig irja a szamot akkor figyelmeztetem es ujra bekerem 
    print("Nem jó számot írtál ,írd be újra!") 
    korok_szama = int(input("Hány körből álljon a játék?\nÍrj be egy számot egytől ötig! ")) 

kor = 0
while korok_szama > kor:
    jatekos_valasztas = int(input("Melyiket választod?\n1-es gomb kő\n2-es gomb papír\n3-as gomb olló\n")) #bekerem a jatekostol, hogy melyik format valasztja
    if jatekos_valasztas != 1 and jatekos_valasztas !=2 and jatekos_valasztas != 3: #ha nem 1-3ig valaszt akkor ujra megkerem, hogy valasszon
        print("Nem jó számot választottál, válassz újra!")
        jatekos_valasztas = int(input("Melyiket választod?\n1-es gomb kő\n2-es gomb papír\n3-as gomb olló\n"))
    
    if jatekos_valasztas == 1:  #valasztastol fuggoen kiprintelem a kepernyore a valasztott alakzatot
        print(kezek.ko)
    elif jatekos_valasztas == 2:
        print(kezek.papir)
    else:
        print(kezek.ollo)
    