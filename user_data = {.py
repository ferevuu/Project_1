# List of texts
texts = ['''
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

# Split the list into separated texts
separated_texts = [text.strip() for text in texts]

# Print the separated texts and allow the user to select one
for i, text in enumerate(separated_texts, start=1):
    print(f"Text {i}:\n{text}\n")

# Prompt the user to choose a text
while True:
    try:
        selection = int(input("Enter the number of the text you want to select (1, 2, or 3): "))
        if 1 <= selection <= 3:
            selected_text = separated_texts[selection - 1]
            print(f"You selected Text {selection}:\n{selected_text}")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")

