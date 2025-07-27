import random

from colorama import init, Fore, Style
init()  # Initialize colorama

print('Loading sklearn module...')
from sklearn.tree import DecisionTreeClassifier
print('sklearn module loaded.')

import os
os.system('cls')


sef_ruzova = False
sef_siva = False
sef_oranzova = False
sef_fialova = False
sef_hneda = False
sef_zlta = False
sef_modra = False
sef_zelena = False

aisef_ruzova = False
aisef_siva = False
aisef_oranzova = False
aisef_fialova = False
aisef_hneda = False
aisef_zlta = False
aisef_modra = False
aisef_zelena = False

stav = 200000
hodnota_majetku = 0

aistav = 200000
aihodnota_majetku = 0

aipolicko = 1

policko = 1

pozemok_list = ["2",'3','5','7','8','9','10','13','14','15','17','18','20','21','22','23','25','26','27','29','30','32']
firma_list = ['6','12','16','31']
paragraf_list = ['4','11','19','24','28']
súkromné_pozemky = []
obsadené_políčka = []
súkromné_firmy = []
policko_info = []

hracove_pozemky = []
hracove_políčka = []
hracove_firmy = []

ai_pozemky = []
ai_políčka = []
ai_firmy = []

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
skupiny_firiem = [{'skupina': '1','priplatok': 9000},
                  {'skupina': '2','priplatok': 9000},
                  {'skupina': '3','priplatok': 3000},
                  {'skupina': '4','priplatok': 3000},
                  {'skupina': '5','priplatok': 9000},
                  {'skupina': '6','priplatok': 0},
                  {'skupina': '7','priplatok': 0},
                  {'skupina': '8','priplatok': 3000},
                  {'skupina': '9','priplatok': 9000},
                  {'skupina': '10','priplatok': 3000},
                  {'skupina': '11','priplatok': 9000},
                  {'skupina': '12','priplatok': 9000},
                  {'skupina': '13','priplatok': 0},
                  {'skupina': '14','priplatok': 9000},
                  {'skupina': '15','priplatok': 3000}     
]
firmy = [{'skupina': '1','nazov': 'reštaurácia','cena': 15000,'poplatok': 7500},
         {'skupina': '1','nazov': 'kaviareň','cena': 25000,'poplatok': 12500},
         {'skupina': '1','nazov': 'bar','cena': 5000,'poplatok': 2500},

         {'skupina': '2','nazov': 'čerpacia stanica 1','cena': 15000,'poplatok': 7500},
         {'skupina': '2','nazov': 'čerpacia stanica 2','cena': 15000,'poplatok': 7500},
         {'skupina': '2','nazov': 'čerpacia stanica 3','cena': 15000,'poplatok': 7500},

         {'skupina': '3','nazov': 'tlačiareň','cena': 5000,'poplatok': 2500},       
         {'skupina': '3','nazov': 'vydavateľstvo','cena': 5000,'poplatok': 2500}, 

         {'skupina': '4','nazov': 'letisko 1','cena': 60000,'poplatok': 30000},
         {'skupina': '4','nazov': 'letisko 2','cena': 50000,'poplatok': 25000},   

         {'skupina': '5','nazov': 'autoservis','cena': 10000,'poplatok': 5000},  
         {'skupina': '5','nazov': 'mototechna','cena': 20000,'poplatok': 10000},
         {'skupina': '5','nazov': 'automobilka','cena': 90000,'poplatok': 45000},

         {'skupina': '6','nazov': 'obchodný dom','cena': 50000,'poplatok': 25000},

         {'skupina': '7','nazov': 'elektráreň','cena': 25000,'poplatok': 12500},

         {'skupina': '8','nazov': 'mlyn','cena': 10000,'poplatok': 5000},
         {'skupina': '8','nazov': 'pekáreň','cena': 50000,'poplatok': 25000},

         {'skupina': '9','nazov': 'diaľnica','cena': 15000,'poplatok': 7500},  
         {'skupina': '9','nazov': 'doprava','cena': 20000,'poplatok': 10000},
         {'skupina': '9','nazov': 'metro','cena': 30000,'poplatok': 15000},     

         {'skupina': '10','nazov': 'kasíno','cena': 40000,'poplatok': 20000},
         {'skupina': '10','nazov': 'zlatníctvo','cena': 90000,'poplatok': 45000},      

         {'skupina': '11','nazov': 'kaderníctvo','cena': 20000,'poplatok': 10000},      
         {'skupina': '11','nazov': 'kozmetický salón','cena': 30000,'poplatok': 15000},      
         {'skupina': '11','nazov': 'módny salón','cena': 35000,'poplatok': 17500},

         {'skupina': '12','nazov': 'stajňa 1','cena': 20000,'poplatok': 10000},
         {'skupina': '12','nazov': 'stajňa 2','cena': 30000,'poplatok': 15000},      
         {'skupina': '12','nazov': 'dostihová dráha','cena': 60000,'poplatok': 30000},            

         {'skupina': '13','nazov': 'lunapark','cena': 30000,'poplatok': 15000},

         {'skupina': '14','nazov': 'hotel C','cena': 10000,'poplatok': 5000},
         {'skupina': '14','nazov': 'hotel A','cena': 15000,'poplatok': 7500},
         {'skupina': '14','nazov': 'hotel B','cena': 20000,'poplatok': 10000},

         {'skupina': '15','nazov': 'lekáreň','cena': 25000,'poplatok': 12500},
         {'skupina': '15','nazov': 'nemocnica','cena': 50000,'poplatok': 25000},
         
]
policka_detaily = [
    {'cislo': '1', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '2', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '3', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '4', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '5', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '6', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '7', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '8', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '9', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '10', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '11', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '12', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '13', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '14', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '15', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '16', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '17', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '18', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '19', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '20', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '21', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '22', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '23', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '24', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '25', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '26', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '27', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '28', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '29', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '30', 'vlastnik': '', 'pozemok': '', 'firma': ''},
    {'cislo': '31', 'vlastnik': 'banka', 'pozemok': '', 'firma': ''},
    {'cislo': '32', 'vlastnik': '', 'pozemok': '', 'firma': ''},]

def multiply_money(kolko):
    global stav
    stav = stav * kolko
def add_money(kolko):
    global stav
    stav = stav + kolko
def zivel(kolko):
    global stav

    sukrpoz = {p["cislo"] for p in súkromné_pozemky}

    global cenyzivel1
    cenyzivel1 = [p["cena"] for p in pozemky if p["cislo"] in sukrpoz]
    #################################################################
    sukrfir = {p["cislo"] for p in súkromné_pozemky}

    global cenyzivel2
    cenyzivel2 = [p["cena"] for p in firmy if p["cislo"] in sukrfir]
        
    stav = stav - ((cenyzivel1 * kolko) + (cenyzivel2 * kolko))
def vrat_sa_o_policko_spat(kolko):
    global policko
    if policko - kolko >= 1:
        policko = policko - kolko
    else:
        policko = policko - kolko + 32

def o_sedem_policok_dopredu():
    global policko
    if policko + 7 <= 32:
        policko = policko + 7
    else:
        policko = policko + 7 - 32
    
    if policko in ai_políčka:
        print(f"Na políčku {policko} je obsadené políčko AI. Daruje ti ho.")
        ai_políčka.remove(policko)
        ai_pozemky.remove(policko)

        policka_detaily[policko - 1]["vlastnik"] = "hrac"
        hracove_políčka.append(policko)
        hracove_pozemky.append(policko)
        print(f"Si teraz vlastníkom políčka {policko}")

    else:
        print("Ten pozemok už vlastníš alebo ho nikto ešte nevlastní.")
def vyplatia():
    global stav
    global aistav
    stav = stav + 5000
    aistav -= 5000
    print(f"Na účte máš teraz {stav} kčs.")

def unos_alebo():
    odpoved = input("Čo si teda vyberieš? 1/2 ")
    if odpoved == "1":
        global stav
        stav = stav - 15000
        print(f"Na účte máš teraz {stav} kčs.")
    elif odpoved == "2":
        global statie
        statie = 3

paragrafy = [{'cislo': '1','text': 'Obchod sa ti nedarí. Vyplať banke 20000.', 'akcia': lambda: add_money(-20000)},
            {'cislo': '2','text': 'Daňové priznanie - zaplať banke 10% z hotovosti.', 'akcia': lambda: multiply_money(0.9)},
            {'cislo': '3','text': 'Zaplať banke 20000.', 'akcia': lambda: add_money(-20000)},
            {'cislo': '4','text': 'Zaplať banke 25000.', 'akcia': lambda: add_money(-25000)},
            {'cislo': '5','text': 'Platíš banke clo 1500.', 'akcia': lambda: add_money(-1500)},
            {'cislo': '6','text': 'Zaplať banke 30000.', 'akcia': lambda: add_money(30000)},
            {'cislo': '7','text': 'V lotérii si vyhral 100000. Vyplatí ti banka.', 'akcia': lambda: add_money(100000)},
            {'cislo': '8','text': 'V lotérii si vyhral 50000. Vyplatí ti banka.', 'akcia': lambda: add_money(50000)},
            {'cislo': '9','text': 'Banka ti vyplatí prémiu 15000.', 'akcia': lambda: add_money(15000)},
            {'cislo': '10','text': 'V lotérii si vyhral 75000. Vyplatí ti banka.', 'akcia': lambda: add_money(75000)},
            {'cislo': '11','text': 'V lotérii si vyhral 25000. Vyplatí ti banka.', 'akcia': lambda: add_money(25000)},
            {'cislo': '12','text': 'Dedíš 20000. Vyplatí ti banka.', 'akcia': lambda: add_money(20000)},
            {'cislo': '13','text': '- Škoda pri živelnej pohrome. Zaplať bake 20% z ceny pozemkov a firiem.', 'akcia': lambda: zivel(0.2)},
            {'cislo': '14','text': 'Vráť sa o 3 políčka späť.', 'akcia': vrat_sa_o_policko_spat(3)},
            {'cislo': '15','text': 'Choď o 7 políčok dopredu. Ak tento pozemok niekto vlastní, daruje ti ho.', 'akcia': lambda: o_sedem_policok_dopredu()},
            {'cislo': '16','text': 'Spoluhráči - obchodníci ti vyplatia dlžobu po 5000 kčs', 'akcia': lambda: vyplatia()},
            {'cislo': '17','text': 'Únos. Výkupné 15000 alebo 3 kolá stoj.', 'akcia': lambda: unos_alebo()},
            #{'cislo': '18','text': '', 'akcia': lambda: add_money(1)}
]

def aimultiply_money(kolko):
    global aistav
    aistav = stav * kolko
def aiadd_money(kolko):
    global aistav
    aistav = stav + kolko
def aizivel(kolko):
    global aistav

    sukrpoz = {p["cislo"] for p in ai_pozemky}

    global cenyzivel1
    cenyzivel1 = [p["cena"] for p in pozemky if p["cislo"] in sukrpoz]
    #################################################################
    sukrfir = {p["cislo"] for p in ai_firmy}

    global cenyzivel2
    cenyzivel2 = [p["cena"] for p in firmy if p["cislo"] in sukrfir]
        
    stav = stav - ((cenyzivel1 * kolko) + (cenyzivel2 * kolko))

def aivrat_sa_o_policko_spat(kolko):
    global aipolicko
    if aipolicko - kolko >= 1:
        aipolicko = aipolicko - kolko
    else:
        aipolicko = aipolicko - kolko + 32

def aio_sedem_policok_dopredu():
    global aipolicko
    if aipolicko + 7 <= 32:
        aipolicko = aipolicko + 7
    else:
        aipolicko = aipolicko + 7 - 32
    
    if aipolicko in obsadené_políčka:
        print(f"Na políčku {policko} je obsadené políčko hráč. Daruje ti ho.")
        obsadené_políčka.remove(policko)
        súkromné_pozemky.remove(policko)

        policka_detaily[aipolicko - 1]["vlastnik"] = "ai"
        ai_políčka.append(aipolicko)
        ai_pozemky.append(aipolicko)
        print(f"Si teraz vlastníkom políčka {aipolicko}")

    else:
        print("Ten pozemok už vlastníš alebo ho nikto ešte nevlastní.")

def aivyplatia():
    global stav
    global aistav
    stav += 5000
    aistav -= 5000
    print(f"Na účte máš teraz {stav} kčs.")
    
def aiunos_alebo():
    odpoved = input("Čo si teda vyberieš? 1/2 ")
    if odpoved == "1":
        global stav
        stav = stav - 15000
        print(f"Na účte máš teraz {stav} kčs.")
    elif odpoved == "2":
        global statie
        statie = 3

aiparagrafy = [{'cislo': '1','text': 'Obchod sa ti nedarí. Vyplať banke 20000.', 'akcia': lambda: aiadd_money(-20000)},
            {'cislo': '2','text': 'Daňové priznanie - zaplať banke 10% z hotovosti.', 'akcia': lambda: aimultiply_money(0.9)},
            {'cislo': '3','text': 'Zaplať banke 20000.', 'akcia': lambda: aiadd_money(-20000)},
            {'cislo': '4','text': 'Zaplať banke 25000.', 'akcia': lambda: aiadd_money(-25000)},
            {'cislo': '5','text': 'Platíš banke clo 1500.', 'akcia': lambda: aiadd_money(-1500)},
            {'cislo': '6','text': 'Zaplať banke 30000.', 'akcia': lambda: aiadd_money(30000)},
            {'cislo': '7','text': 'V lotérii si vyhral 100000. Vyplatí ti banka.', 'akcia': lambda: aiadd_money(100000)},
            {'cislo': '8','text': 'V lotérii si vyhral 50000. Vyplatí ti banka.', 'akcia': lambda: aiadd_money(50000)},
            {'cislo': '9','text': 'Banka ti vyplatí prémiu 15000.', 'akcia': lambda: aiadd_money(15000)},
            {'cislo': '10','text': 'V lotérii si vyhral 75000. Vyplatí ti banka.', 'akcia': lambda: aiadd_money(75000)},
            {'cislo': '11','text': 'V lotérii si vyhral 25000. Vyplatí ti banka.', 'akcia': lambda: aiadd_money(25000)},
            {'cislo': '12','text': 'Dedíš 20000. Vyplatí ti banka.', 'akcia': lambda: aiadd_money(20000)},
            {'cislo': '13','text': '- Škoda pri živelnej pohrome. Zaplať bake 20% z ceny pozemkov a firiem.', 'akcia': lambda: aizivel(0.2)},
            {'cislo': '14','text': 'Vráť sa o 3 políčka späť.', 'akcia': aivrat_sa_o_policko_spat(3)},
            {'cislo': '15','text': 'Choď o 7 políčok dopredu. Ak tento pozemok niekto vlastní, daruje ti ho.', 'akcia': lambda: aio_sedem_policok_dopredu()},
            {'cislo': '16','text': 'Spoluhráči - obchodníci ti vyplatia dlžobu po 5000 kčs', 'akcia': lambda: aivyplatia()},
            {'cislo': '17','text': 'Únos. Výkupné 15000 alebo 3 kolá stoj.', 'akcia': lambda: aiunos_alebo()},
            #{'cislo': '18','text': '', 'akcia': lambda: add_money(1)}
]

def pohyb():
    global policko
    kocka = 0
    while True:
        hod = random.randint(1, 6)
        kocka += hod
        if hod != 6:
            break
        print('Hráč hodil 6')

    policko_a_kocka = int(policko) + kocka
    if policko_a_kocka > 32:
        a32 = 32 - policko
        policko = kocka - a32
        if policko > 1:
            global stav
            stav = stav + 15000
            print(f"Získal si od banky úroky vo výške 15000 kčs. Na účte máš teraz {stav} kčs.")
    else:
        policko = int(policko) + kocka
    print(f"Teraz si na políčku {policko}.")

def aipohyb():
    global aipolicko
    kocka = 0
    while True:
        hod = random.randint(1, 6)
        kocka += hod
        if hod != 6:
            break
        print('AI hodilo 6')

    policko_a_kocka = aipolicko + kocka
    if policko_a_kocka > 32:
        a32 = 32 - aipolicko
        aipolicko = kocka - a32
        print(f"Teraz je na políčku {aipolicko}. 1")
        if aipolicko > 1:
            global aistav
            aistav = aistav + 15000
            print(f"Získal si od banky úroky vo výške 15000 kčs. Na účte máš teraz {aistav} kčs.")
    else:
        aipolicko = aipolicko + kocka
        print(f"Teraz je na políčku {aipolicko}. 2")

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
    while pozemky[random_index]["cislo"] in súkromné_pozemky :
        random_index = random.randrange(len(pozemky)-1)
    print(f'Cena: {pozemky[random_index]["cena"]} kčs')
    print(f'Poplatok za vstup: {pozemky[random_index]["poplatok"]} kčs')
    print(f'Farba: {pozemky[random_index]["farba"]}')

def vyber_firmy():
    global random_index
    random_index = random.randrange(len(firmy))
    while firmy[random_index]["nazov"] in súkromné_firmy :
        random_index = random.randrange(len(firmy))
    print(f'Názov: {firmy[random_index]["nazov"]}')
    print(f'Cena: {firmy[random_index]["cena"]} kčs')
    print(f'Poplatok za vstup: {firmy[random_index]["poplatok"]} kčs')
    
def vyber_paragrafu():
    global random_index
    random_index = random.randrange(len(paragrafy))
    print(f'paragraf je {random_index}')
    print(paragrafy[random_index]["text"])
    paragrafy[random_index]["akcia"]()

def farbahod(farba_filter):
    return [p for p in pozemky if p["farba"] == farba_filter and p["cislo"] in hracove_pozemky]

def kontrola_sefa():
    global sef_ruzova, sef_siva, sef_oranzova, sef_fialova, sef_hneda, sef_zlta, sef_modra, sef_zelena  
    if '1' and '2' in hracove_pozemky:
        sef_ruzova = True
        print("Stal si sa ružovým šéfom!")
    if '3' and '4' and '5' in hracove_pozemky:
        sef_siva = True
        print("Stal si sa sivým šéfom!")
    if '6' and '7' in hracove_pozemky:
        sef_oranzova = True
        print("Stal si sa oranžovým šéfom!")
    if '8' and '9' and '10' in hracove_pozemky:
        sef_fialova = True
        print("Stal si sa fialovým šéfom!")
    if '11' and '12' and '13' in hracove_pozemky:
        sef_hneda = True
        print("Stal si sa hnedým šéfom!")
    if '14' and '15' and '16' and '17' in hracove_pozemky:
        sef_zlta = True
        print("Stal si sa žltým šéfom!")
    if '18' and '19' and '20' and '21' in hracove_pozemky:
        sef_modra = True
        print("Stal si sa modrým šéfom!")
    if '22' and '23' and '24' and '25' in hracove_pozemky:
        sef_zelena = True
        print("Stal si sa zeleným šéfom!")

def AIkontrola_sefa():
    global aisef_fialova, aisef_hneda, aisef_modra, aisef_oranzova, aisef_ruzova, aisef_siva, aisef_zlta, aisef_zelena
    if '1' and '2' in ai_pozemky:
        aisef_ruzova = True
        print("Stal si sa ružovým šéfom!")
    if '3' and '4' and '5' in ai_pozemky:
        aisef_siva = True
        print("Stal si sa sivým šéfom!")
    if '6' and '7' in ai_pozemky:
        aisef_oranzova = True
        print("Stal si sa oranžovým šéfom!")
    if '8' and '9' and '10' in ai_pozemky:
        aisef_fialova = True
        print("Stal si sa fialovým šéfom!")
    if '11' and '12' and '13' in ai_pozemky:
        aisef_hneda = True
        print("Stal si sa hnedým šéfom!")
    if '14' and '15' and '16' and '17' in ai_pozemky:
        aisef_zlta = True
        print("Stal si sa žltým šéfom!")
    if '18' and '19' and '20' and '21' in ai_pozemky:
        aisef_modra = True
        print("Stal si sa modrým šéfom!")
    if '22' and '23' and '24' and '25' in ai_pozemky:
        aisef_zelena = True
        print("Stal si sa zeleným šéfom!")

def farbahodai(farba_filter):
    return [p for p in pozemky if p["farba"] == farba_filter and p["cislo"] in ai_pozemky]

X = [
[84976, 6369, 4],
[46923, 39392, 4],
[185900, 23517, 3],
[69227, 18284, 4],
[20000, 15000, 1],
[1000, 50000, 1],
[20000, 15000, 4],
[4865, 4000, 2],
[34586, 32000, 3],
[75508, 32949, 3],
[30364, 25660, 4],
[45211, 30286, 1],
[49837,43063,3],
[37315,11458,1],
[79647,40967,4],
[25106,24647,4],
[184000,40000,4]
]
# Výstupy: 1 = kúpiť, 0 = nekúpiť
y = [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,0,1,0,0,1]

model1 = DecisionTreeClassifier()
model1.fit(X, y)

def aivyber_paragrafu():
    global random_index
    random_index = random.randrange(len(aiparagrafy))
    print(f'paragraf má {random_index}')
    print(aiparagrafy[random_index]["text"])
    aiparagrafy[random_index]["akcia"]()
#!#!##!#!#!#!#!#!#!###!#!##!#!#!#!#!#!#!###!#!##!#!#!#!#!#!#!###!#!##!#!#!#!#!#!#!###!#!##!#!#!#!#!#!#!###!#!##!#!#!#!#!#!#!###!#!##!#!#!#!#!#!#!###!#!##!#!#!#!#!#!#!###!#!##!#!#!#!#!#!#!##
aipolicko = 1
aipohyb()
os.system('cls')
policko = 1
pohyb()
kvarteto = False

while True:
    print(Fore.WHITE) 
    if kvarteto == True:
        pohyb()
        typ_policka = (zistenie_typu_policka(policko))
    else:
        pass

    print(f'Teraz si na policku {policko} ktoré je {zistenie_typu_policka(policko)}.')
    print(f"Na účte máš {stav} kčs a tvoj majetok má hodnotu {hodnota_majetku} kčs.")

    if policko in ai_políčka:
        hodnoita = int(policka_detaily[policko - 1]['pozemok'])
        hodnotavstupenia = pozemky[hodnoita - 1]['poplatok']
        stav -= hodnotavstupenia
        aistav += hodnotavstupenia

        if [pozemky][policko -1]['farba'] == 'ruzova':
            if aisef_ruzova == True:
                stav -= 2000
                aistav += 2000
                hodnotavstupenia += 2000
        if [pozemky][policko -1]['farba'] == 'oranzova':
            if aisef_oranzova == True:
                stav -= 2000
                aistav += 2000
                hodnotavstupenia += 2000
        if [pozemky][policko -1]['farba'] == 'siva':
            if aisef_siva == True:
                stav -= 5000
                aistav += 5000
                hodnotavstupenia += 5000
        if [pozemky][policko -1]['farba'] == 'fialova':
            if aisef_fialova == True:
                stav -= 5000
                aistav += 5000
                hodnotavstupenia += 5000
        if [pozemky][policko -1]['farba'] == 'hneda':
            if aisef_hneda == True:
                stav -= 5000
                aistav += 5000
                hodnotavstupenia += 5000
        if [pozemky][policko -1]['farba'] == 'zlta':
            if aisef_zlta == True:
                stav -= 8000
                aistav += 8000
                hodnotavstupenia += 8000
        if [pozemky][policko -1]['farba'] == 'modra':
            if aisef_modra == True:
                stav -= 8000
                aistav += 8000
                hodnotavstupenia += 8000
        if [pozemky][policko -1]['farba'] == 'zelena':
            if aisef_zelena == True:
                stav -= 8000
                aistav += 8000
                hodnotavstupenia += 8000
        
        print(f'Platíš AI za vstúpenie na jeho pozemok {hodnotavstupenia} kčs.')
    
    if int(len(farbahod('ruzova'))) > 0:
        print(f"Ružových pozemkov máš {int(len(farbahod('ruzova')))}.")
    if int(len(farbahod('siva'))) > 0:
        print(f"Sivých pozemkov máš {int(len(farbahod('siva')))}.")
    if int(len(farbahod('oranzova'))) > 0:
        print(f"Oranžových pozemkov máš {int(len(farbahod('oranzova')))}.")
    if int(len(farbahod('fialova'))) > 0:
        print(f"Fialových pozemkov máš {int(len(farbahod('fialova')))}.")
    if int(len(farbahod('hneda'))) > 0:
        print(f"Hnedých pozemkov máš {int(len(farbahod('hneda')))}.")
    if int(len(farbahod('zlta'))) > 0:
        print(f"Žltých pozemkov máš {int(len(farbahod('zlta')))}.")
    if int(len(farbahod('modra'))) > 0:
        print(f"Modrých pozemkov máš {int(len(farbahod('modra')))}.")
    if int(len(farbahod('zelena'))) > 0:
        print(f"Zelených pozemkov máš {int(len(farbahod('zelena')))}.")

    if sef_ruzova == True:
        print("Si ružový šéf.")
    if sef_siva == True:
        print("Si sivý šéf.")
    if sef_oranzova == True:
        print("Si oranžový šéf.")
    if sef_fialova == True:
        print("Si fialový šéf.")
    if sef_hneda == True:
        print("Si hnedý šéf.")
    if sef_zlta == True:
        print("Si žltý šéf.")
    if sef_modra == True:
        print("Si modrý šéf.")
    if sef_zelena == True:
        print("Si zelený šéf.")
    kontrola_sefa()
    vstup = input("> ")

    if zistenie_typu_policka(policko) == 'paragraf':
        vyber_paragrafu()
 
    elif vstup.lower() == "kupit":
        if policko not in ai_políčka:
            typ_policka = (zistenie_typu_policka(policko))

            if typ_policka == "pozemok":
                vyber_pozemku()

                vstup_kupit = input("Kúpiť? ")

                if vstup_kupit.lower() == 'y':
                    stav = stav - (pozemky[random_index]["cena"])
                    hodnota_majetku = hodnota_majetku + (pozemky[random_index]["cena"])
                    print(f"Na účte Vám zostalo {stav} kčs a Váš majetok má teraz hodnotu {hodnota_majetku} kčs.")

                    súkromné_pozemky.append(pozemky[random_index]["cislo"])
                    obsadené_políčka.append(policko)

                    for policko_info in policka_detaily:
                        if policko_info["cislo"] == str(policko):
                            policko_info["vlastnik"] = "hráč"
                            policko_info["pozemok"] = pozemky[random_index]["cislo"]


                else:
                    print("Pozemok nebol zakúpený.")

            elif typ_policka == "firma":
                vyber_firmy()

                if vstup_kupit.lower() == 'y':
                    kupit_firma_policko = input('Na aké políčko chceš firmu kúpiť? ')

                    if int(kupit_firma_policko) in obsadené_políčka:
                        print(f'Firma zakúpená na políčko {kupit_firma_policko}.')

                        stav = stav - (firmy[random_index]["cena"])
                        hodnota_majetku = hodnota_majetku + (firmy[random_index]["cena"])
                        
                        print(f"Na účte Vám zostalo {stav} kčs a Váš majetok má teraz hodnotu {hodnota_majetku} kčs.")

                        súkromné_firmy.append(firmy[random_index]["nazov"])

                        for policko_info in policka_detaily:
                            if policko_info["cislo"] == str(policko):
                                policko_info["firma"] = firmy[random_index]["nazov"]


                    else:
                        print("Toto políčko je nedostupné pre Vás.")

                else:
                    print("Firma nebola zakúpená.")

            else:
                print("Toto sa nedá zakúpiť.")
        else:
            print('Toto políčko už vlastní niekto iný.')

    elif vstup.lower() == "sex":
        print(policka_detaily)

    kvarteto = True

    print(Fore.RED)
    aipohyb()
    AIkontrola_sefa()

    if aipolicko in hracove_políčka:
        hodnoita = int(policka_detaily[aipolicko - 1]['pozemok'])
        hodnotavstupenia = pozemky[hodnoita - 1]['poplatok']
        aistav -= hodnotavstupenia
        stav += hodnotavstupenia

        if [pozemky][policko -1]['farba'] == 'ruzova':
            if sef_ruzova == True:
                aistav -= 2000
                stav += 2000
                hodnotavstupenia += 2000
        if [pozemky][policko -1]['farba'] == 'oranzova':
            if sef_oranzova == True:
                aistav -= 2000
                stav += 2000
                hodnotavstupenia += 2000
        if [pozemky][policko -1]['farba'] == 'siva':
            if sef_siva == True:
                aistav -= 5000
                stav += 5000
                hodnotavstupenia += 5000
        if [pozemky][policko -1]['farba'] == 'fialova':
            if sef_fialova == True:
                aistav -= 5000
                stav += 5000
                hodnotavstupenia += 5000
        if [pozemky][policko -1]['farba'] == 'hneda':
            if sef_hneda == True:
                aistav -= 5000
                stav += 5000
                hodnotavstupenia += 5000
        if [pozemky][policko -1]['farba'] == 'zlta':
            if sef_zlta == True:
                aistav -= 8000
                aistav += 8000
                hodnotavstupenia += 8000
        if [pozemky][policko -1]['farba'] == 'modra':
            if sef_modra == True:
                aistav -= 8000
                stav += 8000
                hodnotavstupenia += 8000
        if [pozemky][policko -1]['farba'] == 'zelena':
            if sef_zelena == True:
                aistav -= 8000
                stav += 8000
                hodnotavstupenia += 8000
        
        print(f'Platí hráčovi za vstúpenie na jeho pozemok {hodnotavstupenia} kčs.')

    typ_policka = (zistenie_typu_policka(aipolicko))
    print(f"AI je na políčku {aipolicko} ktoré je {typ_policka}.")
    if typ_policka == "pozemok":
        if aipolicko not in hracove_políčka:
            vyber_pozemku()
            aisituacia = [[aistav, pozemky[random_index]["cena"], sum(1 for p in pozemky if p["farba"] == pozemky[random_index]["farba"]) - int(len(farbahodai(pozemky[random_index]["farba"])))]]
            rozhodnutie = model1.predict(aisituacia)[0]
            print(f'Stav: {aistav}, Cena: {pozemky[random_index]["cena"]}, ešte: {sum(1 for p in pozemky if p["farba"] == pozemky[random_index]["farba"]) - int(len(farbahodai(pozemky[random_index]["farba"])))}')
            print("kupit" if rozhodnutie else "preskocit")

            if rozhodnutie:
                aistav = stav - (pozemky[random_index]["cena"])
                aihodnota_majetku = aihodnota_majetku + (pozemky[random_index]["cena"])
                print(f"Na účte Vám zostalo {aistav} kčs a Váš majetok má teraz hodnotu {aihodnota_majetku} kčs.")

                ai_pozemky.append(pozemky[random_index]["cislo"])
                ai_políčka.append(aipolicko)

                for policko_info in policka_detaily:
                    if policko_info["cislo"] == str(policko):
                        policko_info["vlastnik"] = "ai"
                        policko_info["pozemok"] = pozemky[random_index]["cislo"]


            else:
                print("Pozemok nebol zakúpený.")
        else:
            print('Toto políčko už vlastní niekto iný.')

    elif typ_policka == "firma":
        vyber_firmy()

        aisituacia = [[aistav, pozemky[random_index]["cena"], sum(1 for p in pozemky if p["farba"] == pozemky[random_index]["farba"]) - int(len(farbahodai(pozemky[random_index]["farba"])))]]
        rozhodnutie = model1.predict(aisituacia)[0]
        print(f'Stav: {aistav}, Cena: {pozemky[random_index]["cena"]}, ešte: {sum(1 for p in pozemky if p["farba"] == pozemky[random_index]["farba"]) - int(len(farbahodai(pozemky[random_index]["farba"])))}')
        print("kupit" if rozhodnutie else "preskocit")

        if rozhodnutie:
            kupit_firma_policko_ai = ([p["cislo"] for p in policka_detaily if p["vlastnik"] == "ai" and p["firma"] == ""])
            if kupit_firma_policko_ai == []: 
                pass
            else:
                kupit_firma_policko = random.choice(kupit_firma_policko_ai)

            if int(kupit_firma_policko) in obsadené_políčka and ai_políčka:
                policko = kupit_firma_policko
                print(f'Firma zakúpená na políčko {kupit_firma_policko}.')

                aistav = aistav - (firmy[random_index]["cena"])
                aihodnota_majetku = aihodnota_majetku + (firmy[random_index]["cena"])
                
                print(f"Na účte mu zostalo {aistav} kčs a jeho majetok má teraz hodnotu {aihodnota_majetku} kčs.")

                súkromné_firmy.append(firmy[random_index]["nazov"])

                for policko_info in policka_detaily:
                    if policko_info["cislo"] == str(policko):
                        policko_info["firma"] = firmy[random_index]["nazov"]


            else:
                print("Toto políčko je nedostupné pre Vás.")

        else:
            print("Firma nebola zakúpená.")

    elif typ_policka == "paragraf":
        aivyber_paragrafu()
    else:
        print("Toto sa nedá zakúpiť.")

#pirdat aj sefa a jednotku. STATIE . 
#vykupne za unos - bud zaplat 250000 alebo stoj tri kola a potom funguje ako zeleny dolnik a odovzdas ho na kopku. mozes ho predat.
