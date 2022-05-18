import random
import functions
import os

if not os.path.exists('masspass.txt'):
    with open('masspass.txt', 'w'):
        pass

filesize = os.path.getsize('masspass.txt')

if filesize == 0:
    master_password = input('Create your master password here: ')
    with open('masspass.txt','w') as f:
        f.write(master_password)
    master_password_input = master_password
else:
    master_password_input = input('Enter your master password here: ')

with open('masspass.txt', 'r') as f:
    master_password = f.read()

while master_password_input != master_password:
    master_password_input = input('Try again: ')

print('\nWelcome to your password manager!\n')

print('1) Look up an account \
    \n2) Add a new account\
    \n3) Generate random password\
    \n4) Delete an existing account\n')
input = int(input('Enter a choice: '))

if input == 1:
    functions.accounts()
elif input == 2:
    functions.createaccount()
elif input == 3:
    functions.pass_gen()
elif input == 4:
    functions.delete_account()
else:
    print('Choice not recognized')
    quit()