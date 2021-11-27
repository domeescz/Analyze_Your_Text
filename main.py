import random
odd = "----" * 10
usspass = {'bob':'123','ann':'pass123','mike':'password123','liz':'pass123'} #definice přihlašovacích údajů
#users = {"bob","ann","mike","liz"}
#password = {"123","pass123","password123","pass123"}
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


login = input("Zadej přihlašovací jméno: ")
log_pass = input("Zadej heslo: ")

if usspass.get(login) == log_pass:
    print(odd)
    print("Prohlášení proběhlo úspěšně!")
    print(odd)
else:
    print("Špatné údaje.")
    quit()
choose = input("Zvol si číslo textu (1-3), které chceš zobrazit: ")
print(odd)
if choose == '1': ## TEXT 1
    ## POČET MEZER
        pocet_m = 0
        pocet_m += (TEXTS[0].count(' '))
        print("Mezer je:" + str(pocet_m))

    ## POČET slov s velkým počátečním písmenem
        pocet_big = 0
        rozdel = TEXTS[0].split(" ") #rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if(i.istitle()):
                pocet_big += 1
        print("Počet slov s velkým počátečním písmenem je: ",pocet_big)

    ## POČET slov jen s velkými písmeny
        pocet_onlyB = 0
        rozdel = TEXTS[0].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.isupper()):
                pocet_onlyB += 1
        print("Počet slov s velkými písmeny je: ",pocet_onlyB)

    ## POČET slov jen s malými písmeny
        pocet_onlyL = 0
        rozdel = TEXTS[0].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.islower()):
                pocet_onlyL += 1
        print("Počet malých písmen je :",pocet_onlyL)

    ##POČET čísel

        pocet_num = 0
        rozdel = TEXTS[0].split(" ") # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if(i.isnumeric()):
                pocet_num += 1
        print(f"Počet čísel je {pocet_num}")

    # VYPSÁNÍ SUMY VŠECH ČÍSEL V TEXTU
        all_num = list()
        for i in TEXTS:
            rozdel_vse = i.split(" ")
            for i in rozdel_vse:
                if (i.isnumeric()):
                    all_num.append(i)
        all_num = list(map(int, all_num))
        print("Suma všech čísel v textu je: ", sum(all_num))


#NÁHODNÁ SLOVA V TEXTU (předdefinovaný počet 11-ti slov)
        rozdel = TEXTS[0].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        print(odd)
        print("LEN","OCCURENCES".center(30),"NR.")
        print(odd)
        x = str(11)
        for a in rozdel:
            if a < x:
                x=int(11)
                for a in range (1,x):
                    nahodny = random.choice(rozdel)
                    delka = len(nahodny)
                    print(a,(len(nahodny)*'*').center(30),len(nahodny), sep='\t')
                break


elif choose == '2': ## TEXT 2
        ## POČET MEZER
        pocet_m = 0
        pocet_m += (TEXTS[1].count(' '))
        print("Mezer je:" + str(pocet_m))

        ## POČET slov s velkým počátečním písmenem
        pocet_big = 0
        rozdel = TEXTS[1].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.istitle()):
                pocet_big += 1
        print("Počet slov s velkým počátečním písmenem je: ", pocet_big)

        ## POČET slov jen s velkými písmeny
        pocet_onlyB = 0
        rozdel = TEXTS[1].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.isupper()):
                pocet_onlyB += 1
        print("Počet slov s velkými písmeny je: ", pocet_onlyB)

        ## POČET slov jen s malými písmeny
        pocet_onlyL = 0
        rozdel = TEXTS[1].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.islower()):
                pocet_onlyL += 1
        print("Počet malých písmen je :", pocet_onlyL)

        ##POČET čísel

        pocet_num = 0
        rozdel = TEXTS[1].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.isnumeric()):
                pocet_num += 1
        print(f"Počet čísel je {pocet_num}")

        # VYPSÁNÍ SUMY VŠECH ČÍSEL V TEXTU
        all_num = list()
        for i in TEXTS:
            rozdel_vse = i.split(" ")
            for i in rozdel_vse:
                if (i.isnumeric()):
                    all_num.append(i)
        all_num = list(map(int, all_num))
        print("Suma všech čísel v textu je: ", sum(all_num))

        # NÁHODNÁ SLOVA V TEXTU (předdefinovaný počet 11-ti slov)
        rozdel = TEXTS[0].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        print(odd)
        print("LEN", "OCCURENCES".center(30), "NR.")
        print(odd)
        x = str(11)
        for a in rozdel:
            if a < x:
                x = int(11)
                for a in range(1, x):
                    nahodny = random.choice(rozdel)
                    delka = len(nahodny)
                    print(a, (len(nahodny) * '*').center(30), len(nahodny), sep='\t')
                break



elif choose == '3': ##TEXT 3
        ## POČET MEZER
        pocet_m = 0
        pocet_m += (TEXTS[2].count(' '))
        print("Mezer je:" + str(pocet_m))

        ## POČET slov s velkým počátečním písmenem
        pocet_big = 0
        rozdel = TEXTS[2].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.istitle()):
                pocet_big += 1
        print("Počet slov s velkým počátečním písmenem je: ", pocet_big)

        ## POČET slov jen s velkými písmeny
        pocet_onlyB = 0
        rozdel = TEXTS[2].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.isupper()):
                pocet_onlyB += 1
        print("Počet slov s velkými písmeny je: ", pocet_onlyB)

        ## POČET slov jen s malými písmeny
        pocet_onlyL = 0
        rozdel = TEXTS[2].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.islower()):
                pocet_onlyL += 1
        print("Počet malých písmen je :", pocet_onlyL)

        ##POČET čísel

        pocet_num = 0
        rozdel = TEXTS[2].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        for i in rozdel:
            if (i.isnumeric()):
                pocet_num += 1
        print(f"Počet čísel je {pocet_num}")

        # VYPSÁNÍ SUMY VŠECH ČÍSEL V TEXTU
        all_num = list()
        for i in TEXTS:
            rozdel_vse = i.split(" ")
            for i in rozdel_vse:
                if (i.isnumeric()):
                    all_num.append(i)
        all_num = list(map(int, all_num))
        print("Suma všech čísel v textu je: ", sum(all_num))

        # NÁHODNÁ SLOVA V TEXTU (předdefinovaný počet 11-ti slov)
        rozdel = TEXTS[0].split(" ")  # rozdělení stringu na jednotlivá slova v listu
        print(odd)
        print("LEN", "OCCURENCES".center(30), "NR.")
        print(odd)
        x = str(11)
        for a in rozdel:
            if a < x:
                x = int(11)
                for a in range(1, x):
                    nahodny = random.choice(rozdel)
                    delka = len(nahodny)
                    print(a, (len(nahodny) * '*').center(30), len(nahodny), sep='\t')
                break


else:
        print("Ve zvoleném nic není.")








