from values import *
from paragrafy import *
from artificial_logic import *
import random
def pohyb():
    global policko
    kocka = 0
    while True:
        hod = random.randint(1, 6)
        print(f"Hráč hodil {hod}")
        kocka += hod
        if hod != 6:
            break
        print('Hráč hodil 6')

    policko_a_kocka = int(policko) + kocka
    if policko_a_kocka > 32:
        a32 = 32 - policko
        policko = kocka - a32
        if policko >= 2:
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
        print(f"AI hodilo {hod}")
        kocka += hod
        if hod != 6:
            break
        print('AI hodilo 6')

    policko_a_kocka = aipolicko + kocka
    if policko_a_kocka > 32:
        a32 = 32 - aipolicko
        aipolicko = kocka - a32
        print(f"Teraz je na políčku {aipolicko}. 1")
        if aipolicko >= 2:
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

def aivyber_paragrafu():
    global random_index
    random_index = random.randrange(len(aiparagrafy))
    print(f'paragraf má {random_index}')
    print(aiparagrafy[random_index]["text"])
    aiparagrafy[random_index]["akcia"]()

def obchodovanie_s_polickomhrac():
    while True:
        xpolicko = input('S ktorým políčkom chceš obchodovať?')
        xpolicko = int(xpolicko)
        if xpolicko in hracove_políčka:
            break
    xpozemok = policka_detaily[xpolicko - 1]['pozemok'] #cislo pozemku na policku
    xpozemok = int(xpozemok)
    print(f'pozemok: {xpozemok}')
    xfirma = policka_detaily[xpolicko - 1]['firma']#cislo firmy na policku
    xfirma = int(xfirma)
    print(f'firma: {xfirma}')
    xhodnota = pozemky[xpozemok - 1]['cena'] + firmy[xfirma - 1]['cena']

    xcena = input(f'Za akú cenu chceš predať polícko {xpolicko}, ktore má hodnotu {xhodnota}? \n')
    aisituacia1 = [[int(xhodnota), int(xcena), int(aistav)]]
    print(aisituacia1)
    rozhodnutie = model2.predict(aisituacia1)[0]
    print("kupit" if rozhodnutie == 1 else "preskocit")
    if rozhodnutie == 1:
        policka_detaily[xpolicko - 1]['vlastnik'] = 'ai'
        hracove_políčka.remove(xpolicko)
        ai_políčka.append(xpolicko) 

def obchodovanie_s_vykupnymhrac():
    xcena = input(f'Za akú cenu chceš predať kartičku výkupné za únos? \n')

    aisituacia1 = [[25000, int(xcena), int(aistav)]]
    print(aisituacia1)
    rozhodnutie = model2.predict(aisituacia1)[0]
    print("kupit" if rozhodnutie == 1 else "preskocit")
    if rozhodnutie == 1:
        global vykupne_za_unos_owner
        vykupne_za_unos_owner = 'ai'