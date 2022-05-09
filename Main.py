import time
import os


#clear command
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


#main menu function
def main_menu():
    clear()
    menu = '''
Welcome to OEM, The Online Event Management System!
What would you like to do?
1. Log In
2. Register An Account
3. Event Information
4. Exit'''

    print(menu)

main_menu()