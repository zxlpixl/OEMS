import time
import os

session_status = 'guest'


#start
def start():
    clear()
    print('OEMS Loading...')
    time.sleep(3)
    print('Done!')
    time.sleep(1)
    clear()
    main_menu()


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
def log_in():
    clear()
    time.sleep(0.75)


    while True:    
        info_file = open('account_info.txt', 'r')

        acc_name = input('Please enter your username: ')
    

        for line in info_file:
            acc_info = line.split(',')
            acc_info_name = acc_info[0].strip()
            acc_info_password = acc_info[1].strip()

            if acc_name == acc_info_name:

                while True:
                    acc_password = input('Please enter your password: ')
                
                    if acc_password == acc_info_password:
                        clear()
                        time.sleep(0.75)
                        print(f'Logged in successfully. Welcome back {acc_name}.')
                        time.sleep(0.75)
                        while True:
                            
                            admin_confirmation = input('Are you an admin? [y/n] ')
                            if admin_confirmation == 'y' or admin_confirmation == 'Y':
                                clear()
                                time.sleep(0.75)
                                while True:
                                    clear()
                                    admin_code = int(input('Please enter admin code (use this code for testing purposes:000) \nCode: '))
                                    if admin_code == 000:
                                        time.sleep(0.75)
                                        print('Thank you, redirecting you to the admin menu...')
                                        session_status = 'admin'
                                        #admin menu funtion goes here
                                    else:
                                        clear()
                                        time.sleep(0.75)
                                        print('Admin code does not exist, please try again.')
                                        continue
                            
                            elif admin_confirmation == 'n' or admin_confirmation == 'N':
                                clear()
                                time.sleep(0.75)
                                print('Redirecting you to the menu...')
                                session_status = 'registered'
                                #registered menu function goes here

                            else:
                                print('Answer not recognized, please try again.')
                                continue                   
                    else:
                        time.sleep(0.75)
                        clear()
                        print('Your password is incorrect, please try again.')
                        continue
            else:
                continue
        else:
            log_in_retry = input('The entered username does not exist, would you try again? [y/n]. ')
            if log_in_retry == 'y' or log_in_retry == 'Y':
                clear()
                continue
            
            elif log_in_retry == 'n' or log_in_retry == 'N':
                clear()
                main_menu()
           

            

                                  





#account registration function
def acc_register():
    status = True
    while True:
        print('OEMS Account Registration\n')
        acc_name = input('Please Enter Your Username: ')
        file = open ('test.txt','r')
        for line in file:
            if line.startswith(acc_name):
                status = False
                break
        if status == False:
            print("Username exists")
            continue

        acc_password = input('Please Enter Your Password: ')
        confirmation = input('Please Confirm your Password: ')

        if acc_password != confirmation:
            print("Incorrect password please try again")
            continue 
        else:
            acc_info = [acc_name,acc_password]
            file = open('account_info.txt', 'a')
            file.write(str(acc_info).strip('[]').strip().replace("'", '') + ',\n')
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




start()