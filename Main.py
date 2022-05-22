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
    return




#clear command
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')





#main menu function
def main_menu():
    clear()
    time.sleep(0.75)
    
    if session_status == 'guest':

        menu ='''Welcome to OEMS, The Online Event Management System!
What would you like to do?

1. Log In
2. Register An Account
3. View Event Information
4. Exit

Choice: '''

        answer = int(input(menu))
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
            quit()


    elif session_status == 'admin':
        
        print(f'Welcome to the OEMS admin menu, {acc_name}')
        
        menu ='''What would you like to do?

1. Add New Event
2. Modify Event 
3. View Event Information 
4. Customer Records #function to be created
5. Exit

Choice: '''

        answer = int(input(menu))
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
            quit()



    elif session_status == 'registered':
        
        print(f'Welcome back {acc_name}!')
        
        menu ='''What would you like to do?

1. View Event Information 
2. View Cart
3. Exit

Attention: Please note that cart items will only remain for this session only. Cart items will be deleted on exit.

Choice: '''

        answer = int(input(menu))
        if answer == 1:
            list_event_menu()
            return
        elif answer == 2:
            view_cart()
            return
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
                                        return
                                                                           
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

            log_in_retry = input(log_in_retry)
            if log_in_retry == '1':
                clear()
                time.sleep(0.75)
                continue
            
            elif log_in_retry == '2':
                info_file.close
                acc_name = None
                acc_register()
                return  

            elif log_in_retry =='3':
                main_menu()                     
                return
    
    return



#account registration function
def acc_register():
    
    TF = True
    clear()
    time.sleep(0.75)
    amount_spent = 0

    while TF == True:
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
            acc_info = [acc_name, acc_password, amount_spent]
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
    while TF == True: 
        choice = int(input(option))

        if choice == 1:
            TF = False
            main_menu()
            return
        elif choice == 2:
            TF = False
            log_in()
            return
        elif choice == 3:
            quit()
        else:
            print("Invalid option please try again")
            continue 
    #execute command given by user




#show category function
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
    
    while TF == True:
        answer = int(input(events))
        
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
            print("Invalid option please try again.")
            clear()
            time.sleep(0.75)
            continue

    #asking user to choose category




#event adding function
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
        TF == False
        main_menu()
        return
    return
    



#modify event function
def modify_event():
    event_list()
    choice_id = input("Which event would you like to modify?[ID]: ")

    fhandler_read = open('event.txt','r', 1)
    
    for line in fhandler_read:
        event_info = line.split(',')
        event_id = event_info[0].strip()
        event_category = event_info[1].strip()
        event_name = event_info[2].strip()
        event_price =  event_info[3].strip()
        
        option = '''Options available:
1. Change event category
2. Change event name
3. Change event price
4. Delete event 

Choice: '''
        if event_id == choice_id:

            option_input = int(input(option))

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

            elif option_input == 2:
                new_name = input('Please enter new event name: ')
                break
            
            elif option_input == 3:
                new_price = (input('Please enter new price[RM]: '))
                break


    fhandler_read.close()

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
    main_menu()
    return
        



#list event function
def event_list():
    choice = category()
    clear()
    time.sleep(0.75)

    event_file = open('event.txt', 'r')
    

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
        
        
        if categoryid == event_info_category:
            print(f'ID:{event_info_id}          Event:{event_info_name}          Price:RM{event_info_price}')

    




def list_event_menu():
    event_list()

    global session_status

    TF = True
    if session_status == 'guest':
        event_menu = '''What would you like to do?

1.Back to category menu
2.Back to main menu

Choice: '''

        while TF == True:
            print('\n')
            choice = input(event_menu)
            if choice == '1':
                TF = False
                category()
                return
            elif choice == '2':
                TF = False
                main_menu()
                return
            else:
                clear()
                print('Invalid choice, please try again.')
                time.sleep(3)
                clear()
                continue

    if session_status == 'admin':
        event_menu = '''What would you like to do?

1.Modify event records
2.Back to category menu
3.Back to main menu

Choice: '''

        while TF == True:
            print('\n')
            choice = input(event_menu)
            if choice == '1':
                TF = False
                modify_event()
                return
            elif choice == '2':
                TF = False
                category()
                return
            elif choice == '3':
                TF = False
                main_menu()
                return
            else:
                clear()
                print('Invalid choice, please try again.')
                time.sleep(3)
                clear()
                continue

    if session_status == 'registered':
        event_menu = '''What would you like to do?

1.Add events to cart
2.Back to category menu
3.Back to main menu

Choice: '''
        while TF == True:
            print('\n')
            choice = input(event_menu)
            if choice == '1':
                TF = False
                cart()
                return
            elif choice == '2':
                TF = False
                category()
                return
            elif choice == '3':
                TF = False
                main_menu()
                return
            else:
                clear()
                print('Invalid choice, please try again.')
                time.sleep(3)
                clear()
                continue
    return



#cart_function
def cart():
    clear()
    time.sleep(0.75)
    event_list()
    print('\n')
    TF = True

    
    while TF == True:
        event_choice = input("Which event[ID] would you like to add to cart? (Type 'n' to cancel): ")
        with open('event.txt', 'r') as event_file:
            
            event_file_read = event_file.readlines()

            for item in event_file_read:
                events = item.split(',')
                
                event_id = events[0].strip()
                event_category = events[1].strip()
                event_name = events[2].strip()
                event_price = events[3].strip()

                
                if event_choice == event_id:
                    with open('cart.txt', 'a', 1) as cart_file:
                        event_info = [event_id, event_category, event_name, event_price]
                        cart_file.write (str(event_info).strip('[]').replace("'", '') + '\n')
                        clear()
                        time.sleep(0.75)
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

                elif event_choice == 'n' or event_choice == 'N':
                    TF = False
                    print('Aborting...Sending you to main menu...')
                    time.sleep(3)
                    main_menu()
                    return
    return
                            




def view_cart():
    global acc_name
    clear()
    time.sleep(0.75)
    
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
    print(f"Total Price: ${total_price}")

    view_cart_menu = '''What would you like to do?

1.Proceed to checkout
2.Back to main menu

Choice: '''
    answer = input(view_cart_menu)
    if answer == '1':
        confirmation = input('Are you sure you would like to checkout all items? (y/n): ')
        if confirmation == 'y' or confirmation == 'Y':
            print('Processing...')

            
            with open('account_info.txt') as fhandler_read:
        
                account_data_temp = []         
                account_data = fhandler_read.readlines()
                for account in account_data:
                    accounts = account.split(',')
                    account_name = accounts[0].strip()
                    amount_spent = accounts[2].strip()
                    new_total_price = str(total_price + int(amount_spent))
                    
                    if account_name == acc_name:
                        account = account.replace(amount_spent, new_total_price)
                        
                    account_data_temp.append(account)
                
            
            
            with open('account_info.txt', 'w', 1) as fhandler_write:
                for account in account_data_temp:
                    fhandler_write.write(account)


            print('Checkout complete, the bill will be sent to you by the end of the month, Thank you!')
            print('Redirecting you to the main menu...')
            main_menu()
            return

        elif confirmation == 'n' or confirmation == 'N':
            view_cart()
            return


    elif answer == '2':
        print('Sending you to main menu...')
        time.sleep(3)
        main_menu()
        return
    return       



def customer_records():
    clear()
    time.sleep(0.75)
    TF = True

    with open('account_info.txt') as fhandler:
        accounts = fhandler.readlines()
        for item in accounts:
            account = item.split(',')
            account_name = account[0].strip()
            ammount_spent = account[2].strip()

            print(f'Username:{account_name}          Ammount spent:{ammount_spent}')

    menu = '''What would you like to do?
    
1.Back to main menu

Choice: '''


    while TF == True:

        option = input(menu)

        if option == '1':
            clear()
            time.sleep(0.75)
            print('Sending you back to the main menu...')
            time.sleep(3)
            TF = False
            main_menu()
            return

        else:
            print('Invalid option, please try again.')
            time.sleep(0.75)
            continue









 



start()