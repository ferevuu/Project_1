slova = set()


while len(slova) != 3:
    slovo = input("Zadej slovo na 4 znaky: ".upper())

    if slovo in slova:
        print("Slovo", slovo, " je již uložené")

    elif len(slovo) == 4:
        slova.add(slovo)

    else:
        print("Slovo není dlouhé 4 znaky: ")

else:
    print("Už mám uložené tři slova")
    print(slova)

    




