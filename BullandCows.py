"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: František Vůjtek
email: frantisekvujtek@seznam.cz
discord: fere_91948
"""

import random
import time
import math

line = "-" * 40

def duplicities(code, show_print):
    """
    Converts 4 Digit input code to a string to and it compares the values
    """
    string = str(code)

    if len(string) != len(set(string)):
        if show_print: # If random number generates number with duplicated numbers in code, skip it and print it only when user enters duplicated numbers.
            print("Duplicities are not allowed, Enter unique numbers")
        return False
        
    return True

def control(code):
    """
    Checks if entered input is 4 digits long and if it´s an integer
    """

    if len(code) != 4 and code.isdigit(): 
        print("The number you have entered must be a 4 digit code")
        return False
    elif not code.isdigit():
        print("You have to enter numbers, not a text")
        return False
    elif code.startswith("0"):
        print("The code CAN´T starts with 0!")
        return False
    else:
        return True

        

def check(code1, code2):
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

    for i, x in enumerate(guess_code): # Indexing user attempts to compare values with Random generated code
        check_c1.append(x)

    for i, y in enumerate(random_number): # Indexing Random generated code to compare values with user´s attempts
        check_c2.append(y)

    while True: # Indexing Lists of those 2 codes and compares if the positions and numbers are common or not and if yes, it adds it to the Lists
        for i, x in enumerate(check_c1):
            for ix, y in enumerate(check_c2):
                if ix == i and x == y:
                    bulls.append(x)
                elif x in check_c2 and not ix == i and x == y:
                    cows.append(y)

        if len(bulls) == 1 and len(cows) == 1: # Bulls and Cows mechanisms which returns the output to the user if he guessed the positions or numbers.
            print(f"{len(bulls)} Bull, {len(cows)} Cow")
        elif len(bulls) != 1 and len(bulls) != 4 and len(cows) != 1: # If user guess 4 correct numbers and 4 correct positions, Don´t return any print about Bulls and Cows
            print(f"{len(bulls)} Bulls, {len(cows)} Cows")
        if len(bulls) == 1 and len(cows) != 1:
            print(f"{len(bulls)} Bull, {len(cows)} Cows")
        elif len(bulls) != 1  and len(cows) == 1:
            print(f"{len(bulls)} Bulls, {len(cows)} Cow")
            
        if len(bulls) == 4:  # If the Value it´s False, End the Loop - False is when There are 4 Correct numbers and positions
            print(" #### You won, the correct number is: ", random_number, " ####")
            return True
        
        return False

# Presentation and rules
print("Hi There!")
print(line)
print("""
    I Have generated a random 4 digit code for you.
    Let´s play Bulls & Cows game.
    Basic Rules: 
    - The Code can´t start with 0
    - Numbers in the Code canno´t be twice
    - The Code must be 4 Digits long
""")
print(line)

while True: # generates random 4 Digits number for the game & It does not starts with 0
    random_number = random.randrange(1000, 9999)
    if duplicities(random_number, False) is True:
        break
    else:
        continue

while True: # Checks if user can guess the number on his first try, if not, continue in next loop
    print("Enter a 4 Digit Number: ") 
    start_time = time.time()

    while True: # Checks if user guess the number in the game
        code = input(">>>: ")
        if control(code) == False:
            continue
        elif duplicities(code, True) == False:
            continue
        elif check(code, random_number) == True:
                break
    break

for i in range(100000): # Measures the Elapsed time when users enters first attempt
    result = i * i

end_time = time.time()
elapsed_time = end_time - start_time
time = math.ceil(elapsed_time)
print(line)
print("You have guessed the code in: ", time, "Seconds !")






        
