import random

# def check(user_code, correct_code):
#     """
#     Checks if´s there is correct guess in the Bulls and Cows game and return values
#     First code is the code that user is typing and trying to guess
#     Second code is the correct code which he needs to guess
#     """

#     guess_code = str(user_code)
#     random_number = str(correct_code)
#     user_codes = dict()
#     correct_codes = dict()
#     common_numbers = dict()
#     same_code = []
#     bulls = dict()

#     for i, x in enumerate(guess_code):
#         user_codes[i] = x

#     for ix, y in enumerate(random_number):
#         correct_codes[ix] = y

#     for key1, value1 in user_codes.items(): # Uzivatel hada
#         for key2, value2 in correct_codes.items(): # Spravny kod
#             if value1 == value2:
#                 common_numbers[key1] = [value2]
#                 print(common_numbers)
#             elif key1 in correct_codes and correct_codes[key1] == value1:
#                 bulls[key1] = value1
#                 if len(bulls) == 1:
#                     print(len(bulls), "Bull")
#                 elif len(bulls) == 0 or len(bulls) < 1:
#                     print(len(bulls), "Bulls")
#                     continue

#     for i, key in enumerate(user_codes.values()):
#         if key in correct_codes.values(): # and user_codes.values() == correct_codes.values():
#             same_code.append(key)
#             if len(same_code) == 1:
#                 print(len(same_code), "Cow")

            
#    return print(type(guess_code)), print(type(random_number)), print(user_codes), print(correct_codes)

# def compare(user_code, correct_code):
#     """
#     Checks if´s there is correct guess in the Bulls and Cows game and return values
#     First code is the code that user is typing and trying to guess
#     Second code is the correct code which he needs to guess
#     """

#     guess_code = str(user_code)
#     random_number = str(correct_code)
#     user_codes = dict()
#     correct_codes = dict()
#     common_numbers = dict()
#     same_code = []
#     bulls = dict()


#     for i, x in enumerate(guess_code):
#         user_codes[i] = x

#     for ix, y in enumerate(random_number):
#         correct_codes[ix] = y


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



def duplicities(code):
    """
    Converts 4 Digit input code to a string to compare the values
    """
    string = str(code)
    # It compares if the lenght of the strings is the same or not
    return len(string) != len(set(string))


# while True:
#     random_number = random.randrange(1000, 9999)
#     if duplicities(random_number) is False:
#         break
#     else:
#         continue
# print(random_number)

code = input("Enter a 4 Digits Number: ")
random_number = 1234
cows(code, random_number)
    
