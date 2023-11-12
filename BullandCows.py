"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""

import pprint
import random


line = "-" * 40


def duplicities(code):
    """
    Converts 4 Digit input code to a string to compare the values
    """
    string = str(code)
    # It compares if the lenght of the strings is the same or not
    return len(string) != len(set(string))

def length(code):
    """
    Checks if entered input is 4 digits long and if it´s and integer
    """

    if len(code) < 4 or len(code) > 4 and code.isdigit():
        print("The number you have entered must be a 4 digit code")
        value = False
    elif len(code) > 4 or len(code) < 4 and code is str(code):
        print("You have to enter numbers, not a text")
        value = False
    elif not code.isdigit():
        print("You have to enter 4 digit number")
        value = False
    else:
        value = True
    return value
        
def nozero(code):
    """
    Checks if entered input code starts with 0
    """
    if code.startswith("0"):
        print("The code CAN´T starts with 0!")

def check(code):
    """
    Checks if´s there is correct guess in the Bulls and Cows game and return values
    """
    check = {}
    for i, (k, v) in enumerate(code.items()):
        






# Presentation and rules
print("Hi There!")
print(line)
print("""
        I Have generated a random 4 digit code for you.
        Let´s play Bulls & Cows game.
""")
print(line)

    

# generates random 4 Digits number for the game & It does not starts with 0
while True:
    random_number = random.randrange(1000, 9999)
    if duplicities(random_number) is False:
        break
    else:
        continue
print(random_number)


while True:
    first_try = input("Enter a 4 Digits Number: ")
    if length(first_try) == False:
        continue
    while True:
        number = input("Guess: ")
        if length(number) == False:
            continue
        if number or first_try == random_number: # Correct answer wins the game
            print("Correct, You have guessed the right number!")
            break
        else:
            number is not random_number
            print("Nope, continue")
            continue



# pokud uhadne vypsat vysledek

# Trefí číslo i pozici = 1 BULL
# Trefí ČÍslo ale ne Pozici = 1 COW
# Program bude umět množné sklonovani






        
