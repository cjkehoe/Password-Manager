import json
import random
import string

def createaccount(): 
    name = input('Enter the name of the item: ')   
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    with open('accounts.txt', 'a') as f:
        f.write(f"{name}|{username}|{password}\n")
    print('Account successfully added.')

def accounts():
    
    print('\nHere are the accounts you have saved')
    # Prints account options for the user to print
    num = 1
    with open('accounts.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            names, usernames, passwords = data.split('|')
            print(f'{num}) Name: {names}')
            num += 1

    # Lets user select which account to print and prints
    with open('accounts.txt', 'r') as f:
        data = f.readlines()
        userchoice = int(input('\nWhich account do you want to access?: ')) - 1
        account = (data[userchoice])
        names, usernames, passwords = account.split('|')
        print(f'\nHere is the information to your {names} account \nUsername: {usernames}, Password: {passwords}')  

def pass_gen():

    letters = list(string.ascii_letters)
    digits = list(string.digits)
    characters = list('!@#$%^&*()')

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

# def delete_account():
#     with open('accounts.txt', 'r') as f:
#         lines = f.readlines()
    
#     with open('accounts.txt', 'w') as f:
#         for line in lines:
#             if line.strip('\n') 
