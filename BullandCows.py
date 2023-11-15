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

    if len(string) != len(set(string)):
        value = False
        print("Duplicities are not allowed, Enter unique numbers")
    else:
        value = True

    # It compares if the lenght of the strings is the same or not
    return value

def control(code):
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
        value = False
    else:
        value = True

    return value


def cows(code1, code2):
    """
    Checks if´s there is correct guess in the Bulls and Cows game and return values
    First code is the code that user is typing and trying to guess
    Second code is the correct code which he needs to guess
    """

    guess_code = str(code1)
    random_number = str(code2)
    check_c1 = []
    check_c2 = []
    bulls = []
    cows = []

    for i, x in enumerate(guess_code):
        check_c1.append(x)

    for i, y in enumerate(random_number):
        check_c2.append(y)

    while True:
        for i, x in enumerate(check_c1):
            for ix, y in enumerate(check_c2):
                if ix == i and x == y:
                    bulls.append(x)
                elif x in check_c2 and not ix == i and x == y:
                    cows.append(y)

        if len(bulls) == 1 and len(cows) == 1:
            print(f"{len(bulls)} Bull, {len(cows)} Cow")
        elif len(bulls) != 1 and len(cows) != 1:
            print(f"{len(bulls)} Bulls, {len(cows)} Cows")
        if len(bulls) == 1 and len(cows) != 1:
            print(f"{len(bulls)} Bull, {len(cows)} Cows")
        elif len(bulls) != 1 and len(cows) == 1:
            print(f"{len(bulls)} Bulls, {len(cows)} Cow")
            
        break

    return

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
    first_try = input("Enter a 4 Digit Number: ")
    if control(first_try) == False:
        continue
    elif nozero(first_try) == False:
        continue
    elif duplicities(first_try) == False:
        continue
    else:
        cows(first_try, random_number)
    while True:
        code1 = input(">>>: ")
        cows(code1, random_number)




while True:
    first_try = input("Enter a 4 Digits Number: ")
    if control(first_try) == False:
        continue
    while True:
        number = input("Guess: ")
        if control(number) == False:
            continue
        if number or first_try == random_number: # Correct answer wins the game
            print("Correct, You have guessed the right number!")
            break
        else:
            number is not random_number
            print("Nope, continue")
            continue






        
