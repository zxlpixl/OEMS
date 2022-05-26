import time
import os




#the session_status and acc_name variables here are used for resetting the program to its base form, and acts as a sort of "automatic logout" on program exit.
session_status = 'guest' #the program consists of 3 different session statuses, guest(not logged in), registered(logged in with a valid account), admin(logged in with admin account)
acc_name = None 




#start function: helps with initiating the program
def start():
    clear()
    print('OEMS is loading...')
    cartfile = open('cart.txt', 'w', 1)  #used to clear the cart, as the cart works on a per session basis
    cartfile.close()
    time.sleep(3)
    print('Done!')
    time.sleep(1)
    main_menu()
    return




#clear function: helps with clearing the terminal, mainly for aesthetic purposes
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




#main menu function: helps with showing the user the main menu of the program for the ease of access to other functions in the program
def main_menu():
    clear()
    time.sleep(0.75)
    
    TF = True

    #checks if session status is guest
    if session_status == 'guest':

        menu ='''Welcome to OEMS, The Online Event Management System!
What would you like to do?

1. Log In
2. Register An Account
3. View Event Information
4. Exit

Choice: '''
    
        #execute user's choice
        while TF == True:
            try:
                answer = int(input(menu))
            except:
                print('Invalid option, please try again.')
                time.sleep(0.75)
                clear()
                continue

            if answer == 1:
                log_in()
                return
            elif answer == 2:
                acc_register()
                return
            elif answer == 3:
                list_event_menu()
                return
            elif answer == 4:
                clear()
                quit()
            else:
                print('Invalid option, please try again.')
                time.sleep(0.75)
                clear()
                continue
                    
            

    #checks if session status to "admin"
    elif session_status == 'admin': 
        
        print(f'Welcome to the OEMS admin menu, {acc_name}')
        
        menu ='''What would you like to do?

1. Add New Event
2. Modify Event 
3. View Event Information 
4. Customer Records 
5. Logout
6. Exit

Choice: '''

        #execute user's choice
        while TF == True:
            try:
                answer = int(input(menu))
            except:
                print('Invalid option, please try again.')
                time.sleep(0.75)
                clear()
                continue
            if answer == 1:
                add_event()
                return
            elif answer == 2:
                modify_event()
                return
            elif answer == 3:
                list_event_menu()
                return
            elif answer == 4:
                customer_records()
                return
            elif answer == 5:
                log_out()
                return
            elif answer == 6:
                clear()
                quit()
            else:
                print('Invalid option, please try again.')
                time.sleep(0.75)
                clear()
                continue
            
            
                
    #checks if session status to "registered"
    elif session_status == 'registered':
        
        print(f'Welcome back {acc_name}!')
        
        menu ='''What would you like to do?

1. View Event Information
2. Add Events to cart
3. View Cart
4. Log Out
5. Exit

Attention: Please note that cart items will only remain for this session only. Cart items will be deleted on exit.

Choice: '''

        #executes user's choice
        while TF == True:
            try:
                answer = int(input(menu))
            except:
                print('Invalid option, please try again.')
                time.sleep(0.75)
                clear()
                continue
            if answer == 1:
                list_event_menu()
                return
            elif answer == 2:
                cart()
                return
            elif answer == 3:
                view_cart()
                return
            elif answer == 4:
                log_out()
                return
            elif answer == 5:
                clear()
                quit()
            else:
                print('Invalid option, please try again.')
                time.sleep(0.75)
                clear()
                continue
            
            
        

#log in function: helps the user to be able to log in to the program, into a normal registered account, or an admin account
def log_in():
    clear()
    time.sleep(0.75)
    global session_status
    global acc_name
    TF = True

    #asks user to input a username
    while TF == True:  
        info_file = open('account_info.txt', 'r', 1)
        print('OEMS Login')
        acc_name = input('Please enter your username: ')
        if acc_name == "":
            print('No username entered, please try again.')
            time.sleep(0.75)
            clear()
            continue
    
        for line in info_file:
            acc_info = line.split(',')
            acc_info_name = acc_info[0].strip()
            acc_info_password = acc_info[1].strip()

            if acc_name == acc_info_name:

                #asks user to input password
                while TF == True:
                    
                    acc_password = input('Please enter your password: ')
                   
                    if acc_password == "":
                        print('No password entered, please try again.')
                        time.sleep(0.75)
                        continue
                
                    elif acc_password == acc_info_password:
                        clear()
                        time.sleep(0.75)                      
                        print(f'Logged in successfully. Welcome back {acc_name}.')
                        time.sleep(0.75)

                        while TF == True:
                            
                            #user is required to answer y/n, to confirm if they are/aren't an admin
                            admin_confirmation = input('Are you an admin? (y/n) ')
                            
                            if admin_confirmation == 'y' or admin_confirmation == 'Y':
                                clear()
                                time.sleep(0.75)

                                while TF == True:
                                    clear()
                                    try:
                                        #if user is an admin, an admin code is required, here "000" is used for an example
                                        admin_code = int(input('Please enter admin code (use this code for testing purposes:000) \nCode: '))
                                    except:
                                        print('No admin code entered, please try again.')
                                        time.sleep(0.75)
                                        continue

                                    #checks the admin code
                                    if admin_code == 000:
                                        clear()
                                        time.sleep(0.75)
                                        print('Thank you, redirecting you to the admin menu...')
                                        info_file.close
                                        session_status = 'admin'
                                        TF = False
                                        time.sleep(3)
                                        main_menu()
                                        return
                                                                           
                                    else:
                                        clear()
                                        time.sleep(0.75)
                                        print('Admin code does not exist, please try again.')
                                        time.sleep(0.75)
                                        continue

                            elif admin_confirmation == 'n' or admin_confirmation == 'N':
                                clear()
                                time.sleep(0.75)
                                print('Redirecting you to the menu...')
                                info_file.close
                                session_status = 'registered'
                                TF = False
                                main_menu()
                                return

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
            #executes user's choice
            while TF == True:
                try:
                    log_in_retry = int(input(log_in_retry))
                except:
                    print('Invalid option, please try again.')
                    clear()
                    time.sleep(0.75)
                    continue
                
                if log_in_retry == 1:
                    log_in()
                    return
                
                elif log_in_retry == 2:
                    info_file.close
                    acc_name = None
                    acc_register()
                    return  

                elif log_in_retry == 3:
                    main_menu()                     
                    return

                else:
                    print('Invalid option, please try again.')
                    time.sleep(0.75)
                    continue

            
                
    return




#logout function: helps with logging out the user from a logged in session into a guest session
def log_out():
    clear()
    time.sleep(0.75)
    global session_status
    global acc_name
    session_status = 'guest'
    acc_name = None
    print('Logging out...')
    time.sleep(3)
    main_menu()
    return




#account registration function: helps users register an account
def acc_register():
    
    TF = True
    clear()
    time.sleep(0.75)
    amount_spent = 0

    while TF == True:
        
        status = True
        print('OEMS Account Registration\n')
        acc_name = input('Please enter your username: ')
            #ask for username
        if acc_name == "":
            print('No username entered, please enter a username.')
            time.sleep(0.75)
            clear()
            continue

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
            #checking name availability  
    
        while TF == True:
            #asks user for credit/debit card info for payment purposes
            payment_card = input('Please enter your credit/debit card number [**** **** **** ****]: ')
                
            if payment_card == '':
                print('No credit/debit card entered, please enter your credit/debit card number.')
                time.sleep(0.75)
                continue
            break
        
        while TF == True:
            #asks user to enter password
            acc_password = input('Please enter your password: ')
                
            if acc_password == "":
                print('No password entered, please enter your password.')
                time.sleep(0.75)
                continue
            break

        while TF == True:
            #asks user to confirm their password
            confirmation = input('Please confirm your password: ')
            
            if confirmation == "":
                print('No password entered, please enter your password.')
                time.sleep(0.75)
                continue
            break
        
        

        if acc_password != confirmation:
            clear()
            time.sleep(0.75)
            print("Incorrect password, please try again.")
            continue 
            #password confirmation
        
        elif acc_password == confirmation:
            clear()
            time.sleep(0.75)
            acc_info = [acc_name, acc_password, payment_card, amount_spent]
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
    #executes user's choice
    while TF == True: 
        try:
            choice = int(input(option))
        except:
            print('Invalid option, please try again.')
            time.sleep(0.75)
            clear()
            continue

        if choice == 1:
            TF = False
            main_menu()
            return
        elif choice == 2:
            TF = False
            log_in()
            return
        elif choice == 3:
            clear()
            quit()
        else:
            print("Invalid option, please try again.")
            continue 

    


#show category function: helps with showing all existing categories 
def category():
    TF = True
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
    
    #executes user's choice
    while TF == True:
        try:
            answer = int(input(events))
        except:
            print('Invalid option, please try again.')
            time.sleep(0.75)
            clear()
            continue
            
        if answer <= 6:
            if answer == 6:
                TF = False
                main_menu()
                return
            else:
                return answer
        
        else:
            clear()
            time.sleep(0.75)
            print("Invalid option, please try again.")
            time.sleep(0.75)
            clear()
            continue
            
        

    
#event adding function: helps admins to add events
def add_event():
    TF = True
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

    while TF == True:
        status = True
        
        #asks for the name of event
        event_name = input('Please enter the event name: ')
        if event_name == "":
            print('No event name entered, please enter an event name.')
            time.sleep(0.75)
            continue
       
        fhandler = open('event.txt','r')
        for line in fhandler:
                event_info = line.split(',')
                name_availability = event_info[2].strip()

                if name_availability == event_name:     
                    status = False
        
        #checks for the availability of event name
        if status == False:
            print("Event exists please try again")
            continue
        
        #asks user price of event
        while TF == True:
            try:
                event_price = int(input('How much is the event?(RM): '))
                if event_price == '' or event_price == 0:
                    print('No price entered, please enter price.')
                    time.sleep(0.75)
                    continue
                break
            except:
                print('No price entered, please enter a price.')
                time.sleep(0.75)
                continue
        #asking for name and price
            

        #adds the information of event to file
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
        TF == False
        main_menu() #once done, sends user back to main menu
        return
    return
    



#modify event function: helps admins to modify the information of events
def modify_event():
    event_list()
    print('\n')
    TF = True

    while TF == True:
        
        #asks user the ID of event which they would likke to modify
        choice_id = input("Which event would you like to modify?[ID]: ")
        
        if choice_id == "":
            print('No event ID entered, please enter an event ID.')
            time.sleep(0.75)
            continue
        
        else:
            break
        
    #reads information of selected event
    fhandler_read = open('event.txt','r', 1)
    
    for line in fhandler_read:
        event_info = line.split(',')
        event_id = event_info[0].strip()
        event_category = event_info[1].strip()
        event_name = event_info[2].strip()
        event_price =  event_info[3].strip()
        
        clear()
        time.sleep(0.75)
        option = '''Options available:

1. Change event category
2. Change event name
3. Change event price
4. Delete event 
5. Cancel

Choice: '''
        if event_id == choice_id:

            while TF == True:
                try:
                    option_input = int(input(option))
                    
                except:
                    print('Invalid option, please try again.')
                    time.sleep(0.75)
                    clear()
                    continue 

                #category of event is to be modified, lists all categories for user to select
                if option_input == 1:
                    choice = category()
                    
                    if choice == 1:
                        new_category = 'Sports'
                        break
                    elif choice == 2:
                        new_category = 'E-Sports'
                        break
                    elif choice == 3:
                        new_category = 'Technology'
                        break
                    elif choice == 4:
                        new_category = 'Art'
                        break
                    elif choice == 5:
                        new_category = 'General Entertainment'
                        break
                
                #name of event is to be modified, asks user to input new name for the event
                elif option_input == 2:
                    while TF == True:
                        new_name = input('Please enter new event name: ')
                        if new_name == "":
                            print('No new event name entered, please enter a new event name.')
                            time.sleep(0.75)
                            continue
                        else:
                            break

                #price of event is to be modified, asks user to input new price for the event
                elif option_input == 3:
                    while TF == True:
                        new_price = (input('Please enter new price[RM]: '))
                        if new_price == '' or new_price == '0':
                            print('No new price entered, please enter new price.')
                            time.sleep(0.75)
                            continue
                        else:
                            break
                
                #cancel modification and return to main menu
                elif option_input == 5:
                    main_menu()
                    return

                else:
                    print('Invalid option, please try again.')
                    time.sleep(0.75)
                    clear()
                    continue
            break            

    fhandler_read.close()

    #assigns new changes to file
    with open('event.txt') as fhandler_read:
        
        list_data_temp = []         
        list_data = fhandler_read.readlines()
        for line in list_data:
            
            if line.startswith(choice_id):
                if option_input == 1:
                    line = line.replace(event_category, new_category)
                elif option_input == 2:
                    line = line.replace(event_name, new_name)
                elif option_input == 3:
                    line = line.replace(event_price, new_price)
                elif option_input == 4:
                    line = ""
            list_data_temp.append(line)
        
    with open('event.txt', 'w') as fhandler_write:
        for line in list_data_temp:
            fhandler_write.write(line)
        
    clear()
    time.sleep(0.75)
    print("Modified complete, redirecting to main menu......")
    time.sleep(3)
    main_menu() #sends users back to main menu when done
    return
        



#list event function: helps with listing all events under specific categories
def event_list():
    choice = category()
    clear()
    time.sleep(0.75)

    event_file = open('event.txt', 'r')
    
    #checks which category has been selected by user
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

    
    
    print('Category:',categoryid,'\n')

    for line in event_file:
        event_info = line.split(',')
        event_info_id = event_info[0].strip()
        event_info_category = event_info[1].strip()
        event_info_name = event_info[2].strip()
        event_info_price = event_info[3].strip()
        
        #prints out information of events under selected category
        if categoryid == event_info_category:
            print(f'ID:{event_info_id}          Event:{event_info_name}          Price:RM{event_info_price}')




#list event menu function: helps with showing a menu to users on what to do next for the event_list function
def list_event_menu():
    event_list()


    TF = True
    
    event_menu = '''What would you like to do?

1.Back to category menu
2.Back to main menu

Choice: '''

    #executes user's choice
    while TF == True:
        print('\n')
        try:
            choice = int(input(event_menu))
        except:
            print('Invalid choice, please try again.')
            time.sleep(0.75)
            continue
            
        if choice == 1:
            list_event_menu()
            return
        elif choice == 2:
            TF = False
            main_menu()
            return
        else:
            print('Invalid choice, please try again.')
            time.sleep(0.75)
            continue
    

    return




#cart function: helps with adding events to customer's cart
def cart():
    clear()
    time.sleep(0.75)
    event_list()
    print('\n')
    TF = True

    #asks which event user would like to add to their cart
    while TF == True:
        
        event_choice = input("Which event[ID] would you like to add to cart? (Type 'n' to cancel): ")
        if event_choice == "":
            print('No event ID entered, please enter an event ID.')
            time.sleep(0.75)
            continue

        with open('event.txt', 'r') as event_file:
            
            event_file_read = event_file.readlines()

            for item in event_file_read:
                events = item.split(',')
                
                event_id = events[0].strip()
                event_category = events[1].strip()
                event_name = events[2].strip()
                event_price = events[3].strip()

                #writes information into cart file
                if event_choice == event_id:
                    with open('cart.txt', 'a', 1) as cart_file:
                        event_info = [event_id, event_category, event_name, event_price]
                        cart_file.write (str(event_info).strip('[]').replace("'", '') + '\n')
                        clear()
                        time.sleep(0.75)
                        
                        #asks if user would like to add other events to cart
                        add_another_event = input('Event successfully added to cart, would you like to add another event? (y/n): ')
                            

                        if add_another_event == 'y' or add_another_event == 'Y':
                            event_list()
                            continue
                        elif add_another_event == 'n' or add_another_event == 'N':
                            clear()
                            time.sleep(0.75)
                            print('Sending you to main menu...')
                            time.sleep(3)
                            main_menu()
                            return
                        else:
                            print('Invalid option, please try again.')
                            time.sleep(0.75)
                            continue

                elif event_choice == 'n' or event_choice == 'N':
                    TF = False
                    print('Aborting...Sending you to main menu...')
                    time.sleep(3)
                    main_menu()
                    return

                else:
                    print('The event ID you entered does not exist, please try again.')
                    time.sleep(0.75)
                    break
            continue
                
    return
                            



#view cart function: helps with allowing registered users view items in their cart
def view_cart():
    global acc_name
    clear()
    time.sleep(0.75)
    TF = True
    
    #reads and shows the cart information
    try:
        with open('cart.txt') as cart_file:
            cart_file_read = cart_file.readlines()
            total_price = 0
            
            print(f"{acc_name}'s cart.\n")
            
            
            for item in cart_file_read:
                events = item.split(',')
                event_id = events[0].strip()
                event_category = events[1].strip()
                event_name = events[2].strip()
                event_price = events[3].strip()
                total_price = total_price + int(event_price) 

                print(f'ID:{event_id}          Category:{event_category}          Event:{event_name}          Price:RM{event_price}')

    except:
        clear()
        time.sleep(0.75)
        print('No records in cart, redirecting to main menu...')
        time.sleep(3)
        main_menu()
        return



    print('\n')
    print(f"Total Price: RM{total_price}")
    print('\n')

    view_cart_menu = '''What would you like to do?

1.Proceed to checkout
2.Back to main menu

Choice: '''
    
    #executes user's choice
    while TF == True:
        try:
            answer = int(input(view_cart_menu))
            break
        except:
            print('Invalid option, please try again.')
            time.sleep(0.75)
            continue

    if answer == 1:
        
        while TF == True:
            
            #confirms with user if they are certain to checkout
            confirmation = input('Are you sure you would like to checkout all items? (y/n): ')
          
            
            if confirmation == 'y' or confirmation == 'Y':
                print('Processing...')

                
                #reads and calculates required information
                with open('account_info.txt') as fhandler_read:
            
                    account_data_temp = []         
                    account_data = fhandler_read.readlines()
                    for account in account_data:
                        accounts = account.split(',')
                        account_name = accounts[0].strip()
                        amount_spent = accounts[3].strip()
                        new_total_price = str(total_price + int(amount_spent))
                        
                        if account_name == acc_name:
                            account = account.replace(amount_spent, new_total_price)
                            
                        account_data_temp.append(account)
                    
                
                #writes new information into user's account
                with open('account_info.txt', 'w', 1) as fhandler_write:
                    for account in account_data_temp:
                        fhandler_write.write(account)

                #clears the cart file after checkout
                cartfile = open('cart.txt', 'w', 1)
                cartfile.close()

                clear()
                time.sleep(0.75)
                print('Purchase complete, the receipt will be sent to you by the end of the month, Thank you!')
                time.sleep(3)
                clear()
                print('Redirecting you to the main menu...')
                time.sleep(3)
                main_menu() #sends user back to main menu when done
                return

            elif confirmation == 'n' or confirmation == 'N':
                view_cart()
                return
            
            else:
                print('Invalid option, please try again.')
                time.sleep(0.75)
                continue

            

    elif answer == 2:
        print('Sending you to main menu...')
        time.sleep(3)
        main_menu()
        return
    return       




#customer records function: helps admins view information about all customers
def customer_records():
    clear()
    time.sleep(0.75)
    TF = True
    print('Customer records\n')
    #reads the account information file
    with open('account_info.txt') as fhandler:
        accounts = fhandler.readlines()
        for item in accounts:
            account = item.split(',')
            account_name = account[0].strip()
            ammount_spent = account[2].strip()

            #prints information of all registered accounts
            print(f'Username:{account_name}          Ammount spent:{ammount_spent}')

    menu = '''What would you like to do?
    
1.Back to main menu

Choice: '''

    #executes user's choice
    while TF == True:
        try:
            option = int(input(menu))
        except:
            print('Invalid option, please try again.')
            time.sleep(0.75)
            continue

        if option == 1:
            clear()
            time.sleep(0.75)
            print('Sending you back to the main menu...')
            time.sleep(3)
            TF = False
            main_menu()
            return

        else:
            print('\n')
            print('Invalid option, please try again.')
            time.sleep(0.75)
            continue




#starts the program
start()