#hrac r17; ai r195
from artificial_logic import model1, model2
from values import *
from funkcie import *
import random
import math
from colorama import init, Fore
from sklearn.tree import DecisionTreeClassifier

aipolicko = 1
aipohyb()
policko = 1
pohyb()
kvarteto = False

while True:
    if hracove_statie == 0:
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

                    if stav > (pozemky[random_index]["cena"]) and vstup_kupit.lower() == 'y':
                        stav = stav - (pozemky[random_index]["cena"])
                        hodnota_majetku = hodnota_majetku + (pozemky[random_index]["cena"])
                        print(f"Na účte Vám zostalo {stav} kčs a Váš majetok má teraz hodnotu {hodnota_majetku} kčs.")

                        súkromné_pozemky.append(pozemky[random_index]["cislo"])
                        obsadené_políčka.append(policko)

                        for policko_info in policka_detaily:
                            if policko_info["cislo"] == str(policko):
                                policko_info["vlastnik"] = "hráč"
                                policko_info["pozemok"] = pozemky[random_index]["cislo"]

                    elif stav < (pozemky[random_index]["cena"]):
                        xddd = math.ceil((pozemky[random_index]["cena"])*0.1)
                        stav -= xddd
                        print(f"Nemáš dostatok peňazí na kúpu tohto pozemku, takže Vám banka z účtu zobrala {xddd}.")

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
        
        elif vstup.lower() == 'obchodovat':
            if vykupne_za_unos_owner == 'hrac':
                if input("Chceš obchodovať s pozemkami alebo s kartičkou výkupné za únos? A/B").lower() == 'a':
                    obchodovanie_s_polickomhrac()
                else: 
                    obchodovanie_s_vykupnymhrac()
            else:
                obchodovanie_s_polickomhrac()

        kvarteto = True
    else:
        hracove_statie -= 1
        pass
    
    if ai_statie == 0:
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
    else:
        hracove_statie -= 1
        pass