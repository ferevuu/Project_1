import random

def check(user_code, correct_code):
    """
    Checks if´s there is correct guess in the Bulls and Cows game and return values
    First code is the code that user is typing and trying to guess
    Second code is the correct code which he needs to guess
    """

    guess_code = str(user_code)
    random_number = str(correct_code)
    user_codes = dict()
    correct_codes = dict()

    for i, x in enumerate(guess_code):
        user_codes[i] = x

    for ix, y in enumerate(random_number):
        correct_codes[ix] = y

    for i, key in enumerate(user_codes):
        if key in correct_codes and user_codes[key] == correct_codes[key]:
            print(i, key)
            continue



    # return print(type(guess_code)), print(type(random_number)), print(user_codes), print(correct_codes)


def duplicities(code):
    """
    Converts 4 Digit input code to a string to compare the values
    """
    string = str(code)
    # It compares if the lenght of the strings is the same or not
    return len(string) != len(set(string))


while True:
    random_number = random.randrange(1000, 9999)
    if duplicities(random_number) is False:
        break
    else:
        continue
print(random_number)

code = input("Enter a 4 Digits Number: ")
check(code, random_number)
    
