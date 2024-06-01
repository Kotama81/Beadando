import random #importaltam a random modult
import kezek #importaltam a kezek.py-t hogy elerjem a main.py-bol

korok_szama = int(input("Hány körből álljon a játék?\nÍrj be egy számot egytől ötig! ")) #bekerem a usertol a játék korok számát 1-5ig
if korok_szama > 5 or korok_szama < 0 :  #ha nem 1-5 ig irja a szamot akkor figyelmeztetem es ujra bekerem 
    print("Nem jó számot írtál ,írd be újra!") 
    korok_szama = int(input("Hány körből álljon a játék?\nÍrj be egy számot egytől ötig! ")) 


alakzatok = ["ko", "papir", "ollo"]
kor = 0
jatekos_pontszam = 0
gep_pontszam = 0
nyertes = ""
while korok_szama > kor:
    jatekos_valasztas = int(input("Melyiket választod?\n1-es gomb kő\n2-es gomb papír\n3-as gomb olló\n")) #bekerem a jatekostol, hogy melyik format valasztja
    if jatekos_valasztas != 1 and jatekos_valasztas !=2 and jatekos_valasztas != 3: #ha nem 1-3ig valaszt akkor ujra megkerem, hogy valasszon
        print("Nem jó számot választottál, válassz újra!")
        jatekos_valasztas = int(input("Melyiket választod?\n1-es gomb kő\n2-es gomb papír\n3-as gomb olló\n"))
    
    print("Játékos választása:") #valasztastol fuggoen kiprintelem a kepernyore a valasztott alakzatot
    if jatekos_valasztas == 1:
        jatekos_valasztas = "ko"  
        print(kezek.ko)
    elif jatekos_valasztas == 2:
        jatekos_valasztas = "papir"
        print(kezek.papir)
    else:
        jatekos_valasztas = "ollo"
        print(kezek.ollo)
      
    
    print("Számítógép választása:")  # a szamitogep random valaszt a harom lehetosegbol, majd kiprinteli azt
    gep_valasztasa = random.choice(alakzatok)
    if gep_valasztasa == "ko":
        print(kezek.ko)
    elif gep_valasztasa == "papir":
        print(kezek.papir)
    else:
        print(kezek.ollo)
      

    if jatekos_valasztas == "ko" and gep_valasztasa == "ollo" or jatekos_valasztas == "papir" and gep_valasztasa == "ko" or jatekos_valasztas == "ollo" and gep_valasztasa == "papir": #az esetek amikor a jatekos nyer es kap egy pontot, plusz hozzaadok egyet a kor-hoz
        print("A játékos nyerte ezt a kört!")
        jatekos_pontszam += 1
        kor += 1

    elif jatekos_valasztas == "ko" and gep_valasztasa == "papir" or jatekos_valasztas == "ollo" and gep_valasztasa == "ko" or jatekos_valasztas == "papir" and gep_valasztasa == "ollo": #az esetek amikor a szamitogep nyer es kap egy pontot, plusz hozzaadok egyet a kor-hoz
        print("A számítógép nyerte ezt a kört!")
        gep_pontszam += 1
        kor += 1
    
    elif jatekos_valasztas == "ko" and gep_valasztasa == "ko" or jatekos_valasztas == "papir" and gep_valasztasa == "papir" or jatekos_valasztas == "ollo" and gep_valasztasa == "ollo": #az esetek amikor dontetlen, plusz hozzaadok egyet a kor-hoz
        print("Ez a kör döntetlen!")
        kor += 1

    print(f"A játék állása: játékos pontszáma: {jatekos_pontszam}, a számítógép pontszáma: {gep_pontszam}.\nHátralévő körök száma: {korok_szama - kor}\n") #kiiratom a jatek eddigi allasat es a hatralevo korok szamat

    if jatekos_pontszam > gep_pontszam: #
        nyertes = "a játékos nyert"
    elif jatekos_pontszam < gep_pontszam:
        nyertes = "a számítógép nyert"
    else:
        nyertes = "döntetlen"


print(f"A játék eredménye: {nyertes}!")