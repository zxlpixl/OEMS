import time
import os

session_status = 'guest'

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
    print('OEMS Loading...')
    time.sleep(3)
    print('Done!')
    time.sleep(1)
    clear()
    menu ='''Welcome to OEMS, The Online Event Management System!
What would you like to do?

1. Log In
2. Register An Account
3. Event Information
4. Exit

Choice: '''

    answer = int(input(menu))
    if answer == 1:
        log_in()
    elif answer == 2:
        acc_register()
    elif answer == 3:
        event_info()
    elif answer == 4:
        quit()


#log in function
#def log_in():


#account registration function
def acc_register():
    clear()
    time.sleep(0.75)
    while True:
        print('OEMS Account Registration\n')
        acc_name = input('Please Enter Your Username: ')
        acc_password = input('Please Enter Your Password: ')
        confirmation = input('Please Confirm your Password: ')

        if acc_password != confirmation:
            continue
        
        else:
            acc_info = [acc_name, acc_password]
            file = open('account_info.txt', 'a')
            file.write(str(acc_info).strip('[]').replace("'", '') + '\n')
            file.close
            print('Your account has been successfully created, you will be redirected to the login screen.')
            break
    #login() goes here when done

#show event information
def event_info():
    clear()
    events = '''Events Categories Available:
    
    1. Sports
    2. E-Sports
    3. Technology
    4. Art
    5. General Entertainment
    6. Back to Main Menu
    7. Exit
    
    Choice: '''
    answer = int(input(events))
    #to be continued




main_menu()