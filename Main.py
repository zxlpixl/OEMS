import time
import os


#clear command
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


#exit program
def exit():
    quit


#main menu function
def main_menu():
    clear()
    menu = '''
Welcome to OEMS, The Online Event Management System!
What would you like to do?
1. Log In
2. Register An Account
3. Event Information
4. Exit'''

    print(menu)


#log in function
def log_in():


#account registration function
def acc_register():
    temp_1 = 0
    file_name = 'test.txt'
    while temp_1 == 0:
        account_name = input("Enter your username: ")
        account_password = input("Enter your password: ")
        confirmation_password = input("Reenter to confirm your password: ")
        if confirmation_password != account_password:
            print("Password does not match")
            continue    
        else: 
            account_information = [account_name, account_password]
            fhandler = open(file_name,'a')
            fhandler.write = (str(account_information).strip("[]").replace("'","") +"\n")
            fhandler.close
            print("Account has been created")
            temp_1 += 1


acc_register()


#show event information
def event_info():
