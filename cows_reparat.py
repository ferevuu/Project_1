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

def check_duplicities(code, show_print):
    """
    Converts 4 Digit input code to a string to and then it compares the length of the set.
    """
    string = str(code)

    if len(string) != len(set(string)):
        if show_print: 
            print("Duplicities are not allowed, Enter unique numbers")
        return False
        
    return True

def control(code):
    """
    Checks if entered input is 4 digits long and if it´s an integer nad if the code starts with zero
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
    Second code is the correct code which user needs to guess
    """

    check_c1 = list(code1)
    check_c2 = list(code2)
    bulls = 0
    cows = 0

    for c1, c2 in zip(code1, code2):
        if c1 == c2:
            bulls += 1
        elif c1 in code2:
            cows += 1

    if bulls == 1 and cows != 1:
        print(bulls, "Bull", cows, "Cows")
    elif bulls != 1 and cows == 1:
        print(bulls, "Bulls", cows, "Cow")
    elif bulls == 1 and cows == 1:
        print(bulls, "Bull", cows, "Cow")
    else:
        print(bulls, "Bulls", cows, "Cows")

    if bulls == 4:
        print("### You won, the correct number is: ",random_number, "###")
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


code = random.sample(range(10), 4)  # Generate 4 digit code
if code[0] == 0:
    code[0] = random.randint(1, 9)  

random_number = int(''.join(map(str, code)))  # Convert the list of digits to an integer

while True: # Checks if user can guess the number on his first try, if not, continue in next loop
    print("Enter a 4 Digit Number: ") 
    start_time = time.time()

    while True: # Checks if user guess the number in the game
        code = input(">>>: ")
        if control(code) == False:
            continue
        elif check_duplicities(code, True) == False:
            continue
        elif check(code, str(random_number)) == True:
            break
    break

end_time = time.time()
elapsed_time = end_time - start_time
time = math.ceil(elapsed_time)
print(line)
print("You have guessed the code in: ", time, "Seconds !")






        
