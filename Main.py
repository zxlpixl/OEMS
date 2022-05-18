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
            list_event()
        elif answer == 4:
            quit()


    elif session_status == 'admin':
        
        print(f'Welcome to the OEMS admin menu, {acc_name}')
        
        menu ='''What would you like to do?

1. Add New Event
2. Modify Event #function to be created
3. Event Information 
4. Customer Records #function to be created
5. Exit

Choice: '''

        answer = int(input(menu))
        if answer == 1:
            add_event()
        elif answer == 2:
            acc_register()
        elif answer == 3:
            list_event()
        elif answer == 4:
            quit()
        elif answer == 5:
            quit()



    elif session_status == 'registered':
        
        print(f'Welcome back {acc_name}!')
        
        menu ='''What would you like to do?

1. Event Information 
2. View Cart #function to be created
3. Exit

Choice: '''

        answer = int(input(menu))
        if answer == 1:
            list_event()
        elif answer == 2:
            print('placeholder')#view cart function here 
        elif answer == 3:
            quit()
       
        



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
                                        clear()
                                        time.sleep(0.75)
                                        print('Thank you, redirecting you to the admin menu...')
                                        info_file.close
                                        session_status = 'admin'
                                        TF = False
                                        time.sleep(3)
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
        #ask for username

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
            #checking name availability  
        
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
            file = open('account_info.txt', 'a',1)
            file.write (str(acc_info).strip('[]').replace("'", '') + '\n')
            file.close
            print('Your account has been successfully created.')
            time.sleep(3)
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
    while True: 
        choice = int(input(option))

        if choice == 1:
            main_menu()
        elif choice == 2:
            log_in()
        elif choice == 3:
            quit()
        else:
            print("Invalid option please try again")
            continue 
    #execute command given by user




#show category function
def category():

    clear()
    time.sleep(0.75)
    events = '''Events Categories Available:
    
1. Sports
2. E-Sports
3. Technology
4. Art
5. General Entertainment
6. Back to Main Menu

Choice: '''
    
    while True:
        answer = int(input(events))
        
        if answer <= 6:
            if answer == 6:
                main_menu()
            else:
                return answer
        
        else:
            clear()
            time.sleep(0.75)
            print("Invalid option please try again.")
            clear()
            time.sleep(0.75)
            continue

    #asking user to choose category




#event adding function
def add_event():
    choice = category()

    if choice == 1:
        categoryid = 'Sports'
    elif choice == 2:
        categoryid = 'E-Sports'
    elif choice == 3:
        categoryid = 'Technology'
    elif choice == 4:
        categoryid = 'Art'
    elif choice == 5:
        categoryid = 'General Entertainment'
    #setting category based on user's input

    while True:
        status = True
        event_name = input('Please enter the event name: ')
        fhandler = open('event.txt','r')
        for line in fhandler:
                event_info = line.split(',')
                name_availability = event_info[2].strip()

                if name_availability == event_name:     
                    status = False
        
        if status == False:
            print("Event exists please try again")
            continue

        clear()
        time.sleep(0.75)

        event_price = int(input('How much is the event?(RM): '))
        #asking for name and price

        listid=1
        fhandler = open ('event.txt','r')
        for line in fhandler:
            if line.endswith("\n"):
                listid +=1
        
        event_list = [listid, categoryid, event_name, event_price]
        fhandler = open ('event.txt','a',1)
        fhandler.write (str(event_list).strip('[]').replace("'", '') + '\n')
        fhandler.close
        #appending what was input into text file
        clear()
        time.sleep(0.75)
        print('Your event has been added.')
        time.sleep(3)
        main_menu()
    

#modify event function
def modify_function():
    
    list_event()
    choice_id = int(input("Which event would you like to modify?[ID]: "))

    fhandler = open('test.txt','r')
    for line in fhandler:
        event_info = line.split(',')
        event_id = event_info[0].strip()
        event_category = event_info[1].strip()
        event_name = event_info[2].strip()
        event_price =  event_info[3].strip()


        option = '''Options available:
            1. Change event category
            2. Change event name
            3. Change event price
            4. Delete event ''' 

        if event_id == choice_id:
            option_input = int(input(option))
            if option_input == 1:
                choice = category()
                if choice == 1:
                    new_category = 'Sports'
                elif choice == 2:
                    new_category = 'E-Sports'
                elif choice == 3:
                    new_category = 'Technology'
                elif choice == 4:
                    new_category = 'Art'
                elif choice == 5:
                    new_category = 'General Entertainment'
            
            fhandler = open('event.txt','w',1)
            fhandler.write (str(new_category).replace(event_category,new_category))
            fhandler.close


#list event function
def list_event():
    choice = category()
    clear()
    time.sleep(0.75)

    event_file = open('event.txt', 'r')
    

    if choice == 1:
        categoryid = 'Sports'
    if choice == 2:
        categoryid = 'E-Sports'
    if choice == 3:
        categoryid = 'Technology'
    if choice == 4:
        categoryid = 'Art'
    if choice == 5:
        categoryid = 'General Entertainment'

    

    for line in event_file:
        event_info = line.split(',')
        event_info_id = event_info[0].strip()
        event_info_category = event_info[1].strip()
        event_info_name = event_info[2].strip()
        event_info_price = event_info[3].strip()
        
        print('Category:',categoryid,'\n')
        if categoryid == event_info_category:
            print(f'ID:{event_info_id}          Event:{event_info_name}          Price:RM{event_info_price}')




def list_event_menu():
    global session_status

 
    if session_status == 'guest':
        event_menu = '''What would you like to do?

1.Back to main menu

Choice: '''

        while True:
            choice = input(event_menu)
            if choice == '1':
                main_menu()
            else:
                clear()
                print('Invalid choice, please try again.')
                time.sleep(3)
                clear()
                continue

    if session_status == 'admin':
        event_menu = '''What would you like to do?

1.Modify event records
2.Back to main menu

Choice: '''

        while True:
            choice = input(event_menu)
            if choice == '1':
                #MODIFY EVENT FUNCTION
            elif choice == '2':
                main_menu()
            else:
                clear()
                print('Invalid choice, please try again.')
                time.sleep(3)
                clear()
                continue

    if session_status == 'registered':
        event_menu = '''What would you like to do?

1.Add events to cart
2.Back to main menu

Choice: '''
        while True:
            choice = input(event_menu)
            if choice == '1':
                #CART FUNCTION
            elif choice == '2':
                main_menu()
            else:
                clear()
                print('Invalid choice, please try again.')
                time.sleep(3)
                clear()
                continue


#cart_function
def cart():











start()