import random
import string

letters = list(string.ascii_letters)
digits = list(string.digits)
characters = list('!@#$%^&*()')

def pass_gen():

    #Creating empty list
    password = []

    
    num = int(input('Enter the number of characters for your password: '))

    letters_count = int(input('How many letters in your password: '))
    if letters_count > 0:
        letters_syntax = (input('Would you like these letters to be uppercase (Y/N/Blank): '))

    digits_count = int(input('How many numbers in your password: '))

    characters_count = int(input('How many characters in your password: '))

    if num != letters_count + digits_count + characters_count:
        print("The characters don't add up to the correct total")

    for i in range(0, letters_count):
        password.append(random.choice(letters))
    
    for i in range(0, digits_count):
        password.append(random.choice(digits))

    for i in range(0, characters_count):
        password.append(random.choice(characters))

    #Shuffling the list and creating it into a string
    random.shuffle(password)
    rPassword = ''.join(password)

    #Uppercase check
    if letters_syntax == 'Y':
            rPassword = rPassword.upper()
    elif letters_syntax == 'N':
            rPassword = rPassword.lower()

    #Printing random password
    print(f"\nYour random password is {rPassword}")
