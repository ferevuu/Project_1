mesta = {
    "Praha": 1_335_084, 
    "Brno": 382_405, 
    "Ostrava": 284_982,
    "Plzen": 175_219, 
    "Liberec": 104_261
}
mestecka = {}
mestecka["mesto"] = mesta
print(mestecka["mesto"])

print(mesta["Praha"])


nad_100k = {}

for mesto in mesta:
    if mesta[mesto] > 200_000:
        nad_100k[mesto] = mesta[mesto]
else:
    print(f"Klasika: {nad_100k}")


compr = {mesto: mesta[mesto] for mesto in mesta if mesta[mesto] > 200_000}
print(compr)

vice = {
    mesto: mesta[mesto]
    for mesto in mesta
    if mesta[mesto] > 200_000
}
print(f"mesta nad 200K:  {vice}")


jmena = [
    ["Matous", "Marek", "Lukas", "Jan"],
    ["Lucie", "Aneta", "Michaela", "Lenka"],
    ["Helmut", "Hammet", "Hetfield", "Harold"]
]
hledana_jmena = list()

for seznam in jmena:
    for jmeno in seznam:
        if jmeno.startswith("He"):
            hledana_jmena.append(jmeno)

print(hledana_jmena)


seznam_slov = ["jablko", "pomeranc", "banan", "kiwi", "hruska"]

delka_slov = {slovo: len(slovo) for slovo in seznam_slov}
print(delka_slov)


