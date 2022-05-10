import time
import os

session_status = 'guest'
acc_name = None

#start
def start():
    clear()
    print('OEMS is loading...')
    time.sleep(3)
    print('Done!')
    time.sleep(1)
    main_menu()




#clear command
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




#exit program
def quit():
    quit




#main menu function
def main_menu():
    clear()
    time.sleep(0.75)
    
    if session_status == 'guest':

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


    elif session_status == 'admin':
        
        print(f'Welcome to the OEMS admin menu, {acc_name}')
        
        menu ='''What would you like to do?

1. Add New Event #function to be created
2. Modify Event #function to be created
3. Event Information #function to be created
4. Customer Records #function to be created
5. Exit

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



    elif session_status == 'registered':
        
        print(f'Welcome back {acc_name}!')
        
        menu ='''What would you like to do?

1. Event Information #function to be created
2. View Cart #function to be created
3. Exit

Choice: '''

        answer = int(input(menu))
        if answer == 1:
            log_in()
        elif answer == 2:
            acc_register()
        elif answer == 3:
            event_info()
        elif answer == 4:
            exit()
        






#log in function
def log_in():
    clear()
    time.sleep(0.75)
    global session_status
    global acc_name
    TF = True

    while TF == True:    
        info_file = open('account_info.txt', 'r', 1)
        print('OEMS Login')
        acc_name = input('Please enter your username: ')
    
        for line in info_file:
            acc_info = line.split(',')
            acc_info_name = acc_info[0].strip()
            acc_info_password = acc_info[1].strip()

            if acc_name == acc_info_name:

                while TF == True:
                    acc_password = input('Please enter your password: ')
                
                    if acc_password == acc_info_password:
                        clear()
                        time.sleep(0.75)                      
                        print(f'Logged in successfully. Welcome back {acc_name}.')
                        
                        time.sleep(0.75)
                        while TF == True:
                            
                            admin_confirmation = input('Are you an admin? [y/n] ')
                            if admin_confirmation == 'y' or admin_confirmation == 'Y':
                                clear()
                                time.sleep(0.75)

                                while TF == True:
                                
                                    admin_code = int(input('Please enter admin code (use this code for testing purposes:000) \nCode: '))
                                    
                                    if admin_code == 000:
                                        time.sleep(0.75)
                                        print('Thank you, redirecting you to the admin menu...')
                                        info_file.close
                                        session_status = 'admin'
                                        TF = False
                                        main_menu()
                                                                           
                                    else:
                                        clear()
                                        time.sleep(0.75)
                                        print('Admin code does not exist, please try again.')
                                        continue

                            elif admin_confirmation == 'n' or admin_confirmation == 'N':
                                clear()
                                time.sleep(0.75)
                                print('Redirecting you to the menu...')
                                info_file.close
                                session_status = 'registered'
                                TF = False
                                main_menu()

                            else:
                                print('Answer not recognized, please try again.')
                                continue  

                    else:
                        clear()
                        time.sleep(0.75)
                        print('OEMS Login')
                        print('Your password is incorrect, please try again.')
                        continue
            else:
                continue
        else:
            clear()
            time.sleep(0.75)

            log_in_retry = '''The entered username does not exist.
What would you like to do?

1. Retry
2. Register new account
3. Main menu

Choice: '''

            log_in_retry = input(log_in_retry)
            if log_in_retry == '1':
                clear()
                time.sleep(0.75)
                continue
            
            elif log_in_retry == '2':
                info_file.close
                acc_name = None
                acc_register()  

            elif log_in_retry =='3':
                main_menu()                     




#account registration function
def acc_register():
    clear()
    time.sleep(0.75)

    while True:
        status = True
        print('OEMS Account Registration\n')
        acc_name = input('Please enter your username: ')
        fhandler = open ('account_info.txt','r')

        for line in fhandler:
            if line.startswith(acc_name):
                status = False
                break
        
        if status == False:
            clear()
            print("This username already exists, please use another username.")
            time.sleep(3)
            clear()
            continue
            #name checking    
        
        acc_password = input('Please enter your password: ')
        confirmation = input('Please confirm your password: ')

        if acc_password != confirmation:
            clear()
            time.sleep(0.75)
            print("Incorrect password, please try again.")
            continue 
            #password confirmation
        
        elif acc_password == confirmation:
            clear()
            time.sleep(0.75)
            acc_info = [acc_name, acc_password]
<<<<<<< HEAD
            file = open('account_info.txt', 'a',1)
            file.write (str(acc_info).strip('[]').replace("'", '') + '\n')
            file.close
            print('Your account has been successfully created.')
            time.sleep(3)
=======
            fhandler = open('account_info.txt', 'a',1)
            fhandler.write (str(acc_info).strip('[]').replace("'", '') + '\n')
            fhandler.close
            print('Your account has been successfully created, you will be redirected to the main menu.')
>>>>>>> 43b067a2dd92cab1009d1b3ab6d4cbc8c312e1e8
            break
            #account registered

    option = '''What would you like to do?

1. Main Menu
2. Log In
3. Exit 
    
Choice: '''
    #options for user
    clear()
    time.sleep(0.75)
    choice = int(input(option))

    if choice == 1:
        main_menu()
    elif choice == 2:
<<<<<<< HEAD
        log_in()
    elif choice == 3:
        quit()
=======
        exit()
>>>>>>> 43b067a2dd92cab1009d1b3ab6d4cbc8c312e1e8
    #execute command given by user


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