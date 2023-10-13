uvod = print('''Vítej v programu kalkulačka
pro Sčítání zvol:    "+" 
pro odčítání zvol:   "-"''')
oddelovac = "=" * 35


while True:

    operation = input("Vyber si operaci: ")
    if operation == "+" or operation == "-":
        number1 = int(input("Zadejte první číslo: "))
        number2 = int(input("Zadejte druhé číslo: "))
        if operation == "+":
            vysledek = number1 + number2
            print(number1, " ", operation, " ", number2, "= ", vysledek)
            print(oddelovac)
        elif operation == "-":
            vysledek = number1 - number2
            print(number1, " ", operation, " ", number2, "= ", vysledek)
            print(oddelovac)
        odpoved = str(input("Chcete provést další operaci? Napište 'y' pro Yes, jakákoliv jiná hodnota pro ne: "))
        if odpoved == "y":
            continue
        else:
            print("Ukončuji program".upper())
            quit()

    else: 
        print("Vybrali jste neplatný operátor, zkuste to prosím znovu".upper())







