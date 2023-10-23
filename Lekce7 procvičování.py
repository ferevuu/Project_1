
# def scitej_dve_hodnoty(cislo_1, Cislo_2):
#     """
#     Vrací soucet dvou hodnot uvnitr parametru.

#     """
#     return cislo_1 + Cislo_2


# scitej_dve_hodnoty(1,2)


# rada_cisel =  (34, 544, 644, 324, "gf")
# rada_cisel1 = (546, 54, 62511, 846)
# rada_cisel2 = (56, 999, 111, 0, 45)

# def soucet_cisel(sekvence):
#     soucet = 0
#     """
#     Sčítá hodnoty v tuplu i když je v tuplu obsažen string
#     """
#     for cislo in sekvence:
#         if isinstance(cislo, str) and not cislo.isnumeric():
#             continue
#         soucet = soucet + int(cislo)

#     else: print(soucet)

# soucet_cisel(rada_cisel)
# soucet_cisel(rada_cisel1)
# soucet_cisel(rada_cisel2)



# anagram = ("ship", "hips", "phis")

# def je_anagram(*args) -> bool:
#     """
#     Dokumentace k funkci
#     """
#     vzor = sorted(args[0])

#     for slovo in args:
#         if sorted(slovo) != vzor:
#             return False
#     else:
#         return True
    
# print(
#     je_anagram("ship", "hips", "hisp"),
#     je_anagram("ship", "hips", "duck"),
#     sep="\n"
# )



# def vynasob(num1, num2):
#     """
#     Funkce určená k násobení dvou hodnot  
#     """
#     vysledek = num1 * num2
#     return print("Výsledek je: ", vysledek)

# print(vynasob(5, 5))


# def prumer(sekvence):
#     """
#     Vypíše průmer z hodnot listu
#     """
#     avg = sum(sekvence) / len(sekvence)
#     return round(avg, 2)


# sekvence_cisel = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

# print(prumer(sekvence_cisel))

# vstup = ("Doprdele práce")

# def zdvojeni(list: str) -> str:
#     """
#     Zdvojnásobí všechny znaky ve stringu
#     """
#     zdvojene = []
#     for pismeno in list:
#         zdvojene.append(pismeno * 3)
#     return "".join(zdvojene)
    
# vysledek = zdvojeni(vstup)

# print(vysledek)

# import sys

# os = print(sys.platform.startswith)
# print(os)

# def windows(path):
#     for cesta in path:
#         if str(cesta) == "home" in path:
#             False
#         else:
#             True

# print(windows(os))


# moznost1 = 1
# moznost2 = 3,
# print(type(moznost1))
# print(type(moznost2))

# import os
# var_1 = 1
# var_2 = 1,
# # různé datové typy
# print(type(var_1), type(var_2), sep="\n", end="\n\n")  
#  # rozdělení jména a přípony souboru
# jmeno, pripona = os.path.splitext("poznamky.txt") 
# print(jmeno, pripona, sep="\n", end="\n\n")
# *cele, = os.path.splitext("poznamk.y.txt")
# # uchování jména i přípony v jednom objektu
# print(cele)

sumy = [4562, 456 , 54654]
print(sum(sumy))