from pprint import pprint 
'''
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: František Vůjtek
email: frantisekvujtek@seznam.cz
discord: fere_91948
'''
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

# Základní proměnné
cara = "=" * 40
uzivatele = {"bob": "123",
             "ann": "pass123",
             "mike": "password123", 
             "liz": "pass123"
            }

# Login a Verifikace Usera v loopu dokud nezadá správné heslo
while True:
    username = input("Please Login: ")
    password = input("Pleaste Enter your password: ")
    if username in uzivatele and uzivatele[username] == password:
        print("Welcome to the Text Analyzer! ", username)
        break
    else: 
        print("Wrong Username or Password, Try again!".upper())

# Výběr z nabídky textu 1 až 3
print(cara)

for idx, text in enumerate(TEXTS, 1):
    print(f"Text {idx} to Analyze:\n {text}\n")

# Vybírání textu k Analýze
while True:

    vyber = input("Choose the Text you want to Analyze (1 - 3): ")
    if vyber.isdigit():
        if int(vyber) >= 1 and int(vyber) < 3:
            print(cara)
            textik = TEXTS[int(vyber) - 1]
            print(f"Analyzing Text: {vyber}\n{textik}\n")
            break
        else:
            print("You have to choose between number 1 - 3")
            continue

    else:
        print("You have to choose number between 1 - 3, Don´t enter Text here!")
        print("Closing Analyzer")
        quit()
print(cara)
# Očištění textu o speciální znaky a rozdělení podle mezer
clean_text = "".join(znak for znak in textik if znak not in (".,?!:"))
slova = clean_text.split()

# Vypsaní statistik textu a for cykly pro ně
zac_velke_pismeno = [slovo for slovo in slova if slovo.istitle()]
velke_pismeno = [slovo for slovo in slova  if slovo.isupper()]
male_pismeno = [slovo for slovo in slova if slovo.islower()]
cislo = [slovo for slovo in slova if slovo.isdigit()]
sumaa = sum(int(suma) for suma in cislo if int(suma))

print("Počet slov v Textu: ", len(slova))
print("Počet slov začínajících velkými písmeny: ", len(zac_velke_pismeno))
print("Počet slov psané malými písmeny: ", len(male_pismeno))
print("Počet slov psané Velkými písmeny: ", len(velke_pismeno))
print("Počet čísel v Textu: ", len(cislo))
print("Součet čísel v Textu: ", sumaa)

# Sekce pro výpočet grafu, který indikuje četnost a počet písmen v textu
print(cara)
print(f"LEN | OCCURENCES | NR")
print(cara)

grafik = {}

for graf in slova:
    slovo = len(graf)
    if graf not in grafik:
        grafik[slovo] = 1
    else:
        grafik[slovo] += 1

seradit = sorted(grafik.items(), reverse=True)

for graf, hvezdy in seradit:
    hvezda = "*" * hvezdy
    print(f"{graf:2} | {hvezda:20} | {hvezdy}")

