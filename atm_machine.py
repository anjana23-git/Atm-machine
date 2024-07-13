import time

def atm_simulation():
    print("Please insert your CARD")
    time.sleep(5)
    
    Password = 1234
    Balance = 5000
    Transaction_history = []
    
    try:
        Pin = int(input("Enter your ATM pin: "))
    except ValueError:
        print("Invalid pin format. Please enter numbers only.")
        return
    
    while True:
        if Pin == Password: 
            print(""" 
                1 == Account Balance Inquiry
                2 == Cash Withdrawal
                3 == Cash Deposit
                4 == Pin Change
                5 == Transaction History
                6 == Exit
                """)
            try:
                option = int(input("Please enter your choice: "))
            except ValueError:
                print("Please enter a valid option.")
                continue
            
            if option == 1:
                print(f"Your current balance is {Balance}")
                
            elif option == 2:
                try:
                    withdraw_amount = int(input("Please enter your withdrawal amount: "))
                except ValueError:
                    print("Invalid amount format. Please enter numbers only.")
                    continue
                
                if withdraw_amount > Balance:
                    print("Insufficient balance!")
                else:
                    Balance -= withdraw_amount
                    print(f"{withdraw_amount} amount is debited from your account.")
                    print(f"Your updated balance is {Balance}.")
                    Transaction_history.append(f"Withdrawn: {withdraw_amount}")
                
            elif option == 3:
                try:
                    deposit_amount = int(input("Please enter your deposit amount: "))
                except ValueError:
                    print("Invalid amount format. Please enter numbers only.")
                    continue
                
                Balance += deposit_amount
                print(f"{deposit_amount} amount is credited to your account.")
                print(f"Your updated balance is {Balance}.")
                Transaction_history.append(f"Deposited: {deposit_amount}")
                
            elif option == 4:
                try:
                    new_pin = int(input("Enter your new PIN: "))
                except ValueError:
                    print("Invalid pin format. Please enter numbers only.")
                    continue
                
                Password = new_pin
                print("Your PIN has been successfully changed.")
                
            elif option == 5:
                print("Transaction History:")
                for transaction in Transaction_history:
                    print(transaction)
                    
            elif option == 6:
                print("Thank you for using our ATM. Goodbye!")
                break
                
            else:
                print("Invalid option. Please try again.")
                        
        else:
            print("Wrong pin! Please try again.")
            break

atm_simulation()
