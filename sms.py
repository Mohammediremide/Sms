sms = str(input("Dial *737# to load options\n>> "))
while True:
    print("Welcome to GTBank!!!\n1. Airtime self\n2. Airtime others\n3. Data\n4. Transfer-GTB\n5. Transfer- Others\n6. Exit")
    user_choice = int(input("Please choose an option from (1-7)\n>> "))
        
    if user_choice == 1:
        amount = float(input("Please enter amount\n>> "))
        print(f"Account recharge of N{amount} was successful!")
        break
    elif user_choice == 2:
        thirdparty_number = int(input("Please enter third party Phone number\n>> "))
        thirdparty_amount = float(input("Please enter amount\n>> "))
        pin_code = int(input("Enter 737 PIN\n>> "))  
        print(f"Account recharge for {thirdparty_number} with an amount of N{thirdparty_amount} was successful.")
        break
    elif user_choice == 3:
        reply = int(input("Are you buying for:\n1. Self\n2. Third Party\n>> "))
        if reply == 1:
            data_response = int(input("Please select bundle\n1. 500MB Daily Plan\n2. 1GB Monthly Plan\n3. 2GB Monthly Plan\n4. 5GB Monthly Plan\n>>  "))
            if data_response == 1:
                print("Acivation of 500MB Daily Plan was successful!!")
                break
            elif data_response == 2:
                print("Acivation of 1GB Monthly Plan was successful!!")
                break
            elif data_response == 3:
                print("Acivation of 2GB Monthly Plan was successful!!")
                break
            elif data_response ==4:
                print("Acivation of 5GB Monthly Plan was successful!!")
                break
        elif reply ==2:
            thirdparty_number = int(input("Please enter third party Phone number\n>> "))
            data_response = int(input("Please select bundle\n1. 500MB Daily Plan\n2. 1GB Monthly Plan\n3. 2GB Monthly Plan\n4. 5GB Monthly Plan\n>>  "))
            if data_response == 1:
                pin_code = int(input("Enter 737 PIN\n>> "))
                print(f"The activation of the 500MB Daily Plan for {thirdparty_number} was successful!")
                break
            elif data_response == 2:
                pin_code = int(input("Enter 737 PIN\n>> "))
                print(f"The activation of the 1GB Monthly Plan for {thirdparty_number} was successful!")
                break
            elif data_response == 3:
                pin_code = int(input("Enter 737 PIN\n>> "))
                print(f"The activation of the 2GB Monthly Plan for {thirdparty_number} was successful!")
                break
            elif data_response ==4:
                pin_code = int(input("Enter 737 PIN\n>> "))
                print(f"The activation of the 5GB Monthly Plan for {thirdparty_number} was successful!")
                break
        else:
            print("Invalid Input. Try Again!")
            break
    elif user_choice == 4:
        account_number = int(input("Please enter Account number\n>> "))
        transfer_amount = float(input("Please enter amount\n>> "))
        pin_code = int(input("Enter 737 PIN\n>> "))          #limit to four digits
        print(f"Your have successfully transferred NGN {transfer_amount} to {account_number}")
        break
    elif user_choice == 5:
        bank = int(input("Please select bank\n1. Access Bank\n2. First bank\n3. FCMB\n4. Zenith\n5. Others\n>> "))
        account_number = int(input("Please enter Account number\n>> "))
        transfer_amount = float(input("Please enter amount\n>> "))
        pin_code = int(input("Enter 737 PIN\n>> "))          #limit to four digits
        print(f"Your have successfully transferred NGN {transfer_amount} to {account_number}")
        break
    elif user_choice == 6:
        print("Thank you for using GTBank. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")