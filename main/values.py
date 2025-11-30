hracove_statie = 0
ai_statie = 0
hrac_stoji = False
ai_stoji = False
vykupne_za_unos_owner = ''

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