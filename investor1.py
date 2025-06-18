import random

pozemok_list = ["2",'3','5','7','8','9','10','13','14','15','17','18','20','21','22','23','25','26','27','29','30','32']
firma_list = ['6','12','16','31']
paragraf_list = ['4','11','19','24','28']
súkromné_pozemky = []
obsadené_políčka = []

pozemky = [{'cislo': 1,'farba': 'ruzova','cena': 50000,'poplatok': 10000},
           {'cislo': 2,'farba': 'ruzova','cena': 45000,'poplatok': 9000},
           
           {'cislo': 3,'farba': 'siva','cena': 19000,'poplatok': 3800},
           {'cislo': 4,'farba': 'siva','cena': 23000,'poplatok': 4600},
           {'cislo': 5,'farba': 'siva','cena': 32000,'poplatok': 6400},

           {'cislo': 6,'farba': 'oranzova','cena': 50000,'poplatok': 10000},
           {'cislo': 7,'farba': 'oranzova','cena': 60000,'poplatok': 12000},

           {'cislo': 8,'farba': 'fialova','cena': 10000,'poplatok': 2000},
           {'cislo': 9,'farba': 'fialova','cena': 15000,'poplatok': 3000},
           {'cislo': 10,'farba': 'fialova','cena': 20000,'poplatok': 4000},

           {'cislo': 11,'farba': 'hneda','cena': 16000,'poplatok': 3200},
           {'cislo': 12,'farba': 'hneda','cena': 22000,'poplatok': 4400},
           {'cislo': 13,'farba': 'hneda','cena': 28000,'poplatok': 5600},

           {'cislo': 14,'farba': 'zlta','cena': 6000,'poplatok': 1200},
           {'cislo': 15,'farba': 'zlta','cena': 14000,'poplatok': 2800},
           {'cislo': 16,'farba': 'zlta','cena': 22000,'poplatok': 4400},
           {'cislo': 17,'farba': 'zlta','cena': 33000,'poplatok': 6600},

           {'cislo': 18,'farba': 'modra','cena': 24000,'poplatok': 4800},
           {'cislo': 19,'farba': 'modra','cena': 32000,'poplatok': 6400},
           {'cislo': 20,'farba': 'modra','cena': 36000,'poplatok': 7200},
           {'cislo': 21,'farba': 'modra','cena': 40000,'poplatok': 8000},

           {'cislo': 22,'farba': 'zelena','cena': 10000,'poplatok': 2000},
           {'cislo': 23,'farba': 'zelena','cena': 20000,'poplatok': 4000},
           {'cislo': 24,'farba': 'zelena','cena': 25000,'poplatok': 5000},
           {'cislo': 25,'farba': 'zelena','cena': 30000,'poplatok': 6000},
]

stav = 200000
hodnota_majetku = 0

policko = 1
print(f"Začínaš na políčku {policko}.")

def pohyb():
    kocka = random.randint(1,6)

    while kocka == 6:
        kocka = kocka + random.randint(1,6)

    global policko
    policko_a_kocka = policko + kocka
    if policko_a_kocka > 32:
        a32 = 32 - policko
        policko = kocka - a32
        print(f"Teraz si na políčku {policko}.")
        if policko > 1:
            stav = stav + 15000
            
    else:
        policko = policko + kocka
        print(f"Teraz si na políčku {policko}.")

def zistenie_typu_policka(policko):
    if str(policko) in pozemok_list:
        return "pozemok"
    elif str(policko) in firma_list:
        return 'firma'
    elif str(policko) in paragraf_list:
        return 'paragraf'
    elif str(policko) == "1":
        return "zebrak"

def vyber_pozemku():
    global random_index
    random_index = random.randrange(len(pozemky)-1)
    print(f'Cena: {pozemky[random_index]["cena"]} kčs')
    print(f'Poplatok za vstup: {pozemky[random_index]["poplatok"]} kčs')
    print(f'Farba: {pozemky[random_index]["farba"]}')

#def farbahod(farbahod):
    #return sum(1 for p in pozemky if p["farba"] == farbahod)

while True:
    vstup = input("> ")

    if vstup.lower() == "stav":
        print(f"Na účte máš {stav} kčs a tvoj majetok má hodnotu {hodnota_majetku} kčs.")
        #print(f"Ružových pozemkov máte {farbahod('ruzova')}, sivých {farbahod('siva')}, oranžových {farbahod('oranzova')}, fialových {farbahod('fialova')}, hnedých {farbahod('hneda')}, žltých {farbahod('zlta')}, modrých {farbahod('modra')} a zelených {farbahod('zelena')}")

    elif vstup.lower() == "kupit":
        typ_policka = (zistenie_typu_policka(policko))
        if typ_policka == "pozemok":
            vyber_pozemku()
            vstup_kupit = input("Kúpiť? ")

            if vstup_kupit.lower() == 'y':
                stav = stav - (pozemky[random_index]["cena"])
                hodnota_majetku = hodnota_majetku + (pozemky[random_index]["cena"])
                print(f"Na účte Vám zostalo {stav} kčs.")
                súkromné_pozemky.append(pozemky[random_index]["cislo"])
                obsadené_políčka.append(policko)

            else:
                print("Pozemok nebol zakúpený.")

        #elif typ_policka == "firma":


        else:
            print("Toto sa nedá zakúpiť.")

    else:
        pohyb()
        typ_policka = (zistenie_typu_policka(policko))
        print(f"Si na políčku {typ_policka}.")

#este treba pridat firmy a paragrafy. taktiez aj sefa a jednotku. a spojazdnit riadky 85 a 93