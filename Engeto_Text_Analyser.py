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





# Proměné k verifikaci loginu
username = input("Please, log in with your username: ")
password = input("Please verify with your password: ")
print(cara)

# Podmínky k verifikaci
if username in uzivatele and uzivatele[username] == password: #Pokud jmeno a heslo jsou stejne, může dál
    print("Thanks for the verification, here is the TEXT offer to analyze:")
    print(cara)      

else:
    print("Sorry, but you have entered wrong credentials" )
    print("Closing Text Analyzer")
    quit()


for index, texty in enumerate(TEXTS, start=1): # Rozdělí texty přehledně pod sebe a odděleně
    print(f"Text {index}:\n{texty}\n") 
    continue


while True:
    a_text = int(input("Enter the number of TEXT you want to Analyze (1 - 3): "))
    if 1 <= a_text <= 3:
        vyber = TEXTS[a_text - 1]
        print(cara)
        print(f"analyzing\n {vyber}")
        break
    else:
        print("Invalid Input, You have to choose number betwwen 1 and 3")
        break
    



