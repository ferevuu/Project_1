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

def check(user_code, correct_code):
    """
    Checks if´s there is correct guess in the Bulls and Cows game and return values
    First code is the code that user is typing and trying to guess
    Second code is the correct code which he needs to guess
    """
    user_code = []
    correct_code = []
    user_codes = dict()
    correct_codes = dict()
    for i, (k, v) in enumerate(user_code.items()):
        if u
        

def compare(user_code, correct_code):
    """
    Checks if´s there is correct guess in the Bulls and Cows game and return values
    First code is the code that user is typing and trying to guess
    Second code is the correct code which he needs to guess
    """

    guess_code = str(user_code)
    random_number = str(correct_code)
    user_codes = dict()
    correct_codes = dict()
    common_numbers = dict()
    same_code = []
    bulls = dict()


    for i, x in enumerate(guess_code):
        user_codes[i] = x

    for ix, y in enumerate(random_number):
        correct_codes[ix] = y

    for key1, value1 in user_codes.items(): # Uzivatel hada
        for key2, value2 in correct_codes.items(): # Spravny kod
            if value1 == value2:
                common_numbers[key1] = [value2]
                print(common_numbers)
            elif key1 in correct_codes and correct_codes[key1] == value1:
                bulls[key1] = value1
                print("Bulls", bulls)


    for i, key in enumerate(user_codes.values()):
        if key in correct_codes.values(): # and user_codes.values() == correct_codes.values():
            same_code.append(key)
            if len(same_code) == 1:
                print(len(same_code), "Cow")


    return print(type(guess_code)), print(type(random_number)), print(user_codes), print(correct_codes)


def cows(code1, code2)
    """
    Checks if´s there is correct guess in the Bulls and Cows game and return values
    First code is the code that user is typing and trying to guess
    Second code is the correct code which he needs to guess
    """

    guess_code = str(code1)
    random_number = str(code2)
    check_c1 = dict()
    check_c2 = dict()
    common = []

    for x in enumerate(check_c1.values()):
        if x in check_c2.values():
            common.append(x)
            if len(common) == 1:
                print(len(common), "Cow")
            elif len(common) == 0 or len(common) > 1:
                print(len(common), "Cows")


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






        
