from values import *
def multiply_money(kolko):
    global stav
    stav = stav * kolko
def add_money(kolko):
    global stav
    if kolko > 0:
        stav = stav + kolko
    else:
        if vykupne_za_unos_owner == 'hrac':
            a = input("Chceš zaplatiť? (y/n) ")
            if a.lower == 'y':
                stav = stav + kolko
            else:
                print('Vyhol si sa platbe, ale strácaš kartičku.')
                vykupne_za_unos_owner = ''
        else:
            stav = stav + kolko

def zivel(kolko):
    global stav, cenyzivel1, cenyzivel2, vykupne_za_unos_owner
    if vykupne_za_unos_owner != 'hrac':

        sukrpoz = {p["cislo"] for p in súkromné_pozemky}

        cenyzivel1 = [p["cena"] for p in pozemky if p["cislo"] in sukrpoz]
        #################################################################
        sukrfir = {p["cislo"] for p in súkromné_pozemky}

        cenyzivel2 = [p["cena"] for p in firmy if p["cislo"] in sukrfir]
            
        stav = stav - ((cenyzivel1 * kolko) + (cenyzivel2 * kolko))
    else:
        a = input('Chceš zaplatiť? (y/n) ')
        if a.lower() == 'y':

            sukrpoz = {p["cislo"] for p in hracove_pozemky}

            cenyzivel1 = [p["cena"] for p in pozemky if p["cislo"] in sukrpoz]
            #################################################################
            sukrfir = {p["cislo"] for p in hracove_firmy}

            cenyzivel2 = [p["cena"] for p in firmy if p["cislo"] in sukrfir]
                
            stav = stav - ((cenyzivel1 * kolko) + (cenyzivel2 * kolko))
        else:
            print('Vyhol si sa platbe, ale strácaš kartičku.')
            vykupne_za_unos_owner = ''

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
        global hracove_statie
        hracove_statie = 3
def vykupne():
    vykupneinput = input("Zaplatíš 250 000 kčs alebo stojíš tri kolá? (1/2) ")
    if vykupneinput == "1":
        global stav
        stav = stav - 250000
        print(f"Na účte máš teraz {stav} kčs.")
    if vykupneinput == "2":
        global hracove_statie
        hracove_statie = 3
        print("Stojíš tri kolá.")
    vykupne_za_unos_owner = 'hrac'
    print('Dostal si kartičku s výkupným. Môžeš si ju nechať a potom neplatiť paragrafy, alebo ju môžeš predať.')
#vykupne za unos - bud zaplat 250000 alebo stoj tri kola a potom funguje ako zeleny dolnik a odovzdas ho na kopku. mozes ho predat.

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
            {'cislo': '18','text': 'Výkupné za únos. Zaplať 250 000 kčs alebo stoj tri kolá.', 'akcia': lambda: vykupne()}
            
]

def aimultiply_money(kolko):
    global aistav
    aistav = stav * kolko
def aiadd_money(kolko):
    global aistav
    if kolko > 0:
        aistav = aistav + kolko
    else:
        if vykupne_za_unos_owner == 'ai':
            print('Vyhol sa platbe, ale stráca kartičku.')
            vykupne_za_unos_owner = ''
        else: 
            aistav = aistav + kolko

def aizivel(kolko):
    global aistav, cenyzivel1, cenyzivel2, vykupne_za_unos_owner
    if vykupne_za_unos_owner != 'ai':

        sukrpoz = {p["cislo"] for p in ai_pozemky}

        cenyzivel1 = [p["cena"] for p in pozemky if p["cislo"] in sukrpoz]
        #################################################################
        sukrfir = {p["cislo"] for p in ai_firmy}

        cenyzivel2 = [p["cena"] for p in firmy if p["cislo"] in sukrfir]
            
        aistav -= ((cenyzivel1 * kolko) + (cenyzivel2 * kolko))
    else:
        a = input('Chceš zaplatiť? (y/n) ')
        if a.lower() == 'y':

            sukrpoz = {p["cislo"] for p in ai_pozemky}

            cenyzivel1 = [p["cena"] for p in pozemky if p["cislo"] in sukrpoz]
            #################################################################
            sukrfir = {p["cislo"] for p in ai_firmy}

            cenyzivel2 = [p["cena"] for p in firmy if p["cislo"] in sukrfir]
                
            aistav -= ((cenyzivel1 * kolko) + (cenyzivel2 * kolko))
        else:
            print('Vyhol sa platbe, ale stráca kartičku.')
            vykupne_za_unos_owner = ''
            

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
    global aistav
    if aistav > 20000:
        aistav = aistav - 15000
        print(f"Na účte má teraz {aistav} kčs.")
    else:
        global ai_statie
        ai_statie = 3

def vykupne():
    global vykupne_za_unos_owner, aistav
    if aistav > 255000:
        aistav = aistav - 250000
        print(f"Na účte má teraz {aistav} kčs.")
    else:
        global ai_statie
        ai_statie = 3
        print("Stojíš tri kolá.")
    vykupne_za_unos_owner = 'ai'
    print('Dostal kartičku s výkupným. Môže si ju nechať a potom neplatiť paragrafy, alebo ju môže predať.')

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
            {'cislo': '18','text': 'Výkupné za únos. Zaplať 250 000 kčs alebo stoj tri kolá.', 'akcia': lambda: add_money(1)}

]