ovoce = ["jablko", "banan", "citron", "pomeranc"]
print("Dostupné Ovoce: ", ovoce)

while True:
    vyber = input("Vyber si z dostupného ovoce: ")
    if vyber not in ovoce:
        print("Toto není ovoce ze seznamu!")

    else:
        print("Bezva, toto je ovoce ze seznamu!!!".upper())
        break




