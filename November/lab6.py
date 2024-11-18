def main():
    #define dictionary for the user account, set the balance to 1000 and the pin to 1111
    user_account = {"balance": 1000, "pin": 1111}
    print("Welcome to the ATM! (Pin is 1111)")
    #run the authenticate function which asks the user to enter their pin
    if authenticate(user_account) == False:
        #if the user fails to enter the correct pin, exit the program
        exit()
    while True:
        #always run the atm menu screen at the start of the loop
        atm_menu()
        try:
            #check which choice the user enters
            choice = int(input("Select an option (1-5): "))
            if choice == 1:
                check_balance(user_account)
            elif choice == 2:
                deposit_money(user_account)
            elif choice == 3:
                withdraw_money(user_account)
            elif choice == 4:
                change_pin(user_account)
            elif choice == 5:
                print("Thank you for using the ATM.")
                break
            else:
                print("Invalid option, please select a number between 1 and 5.")
        #handle errors where the wrong datatype is entered (ex. str)
        except ValueError:
            print("Invalid input, try entering a number next time")



def atm_menu():
    #atm menu screen, this is always run at the start of the while loop in 'main'
    print("----ATM Menu----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Exit")

def check_balance(account):
    #print the current account balance rounded to 2 decimal places to the user
    print(f"Your current balance is: ${account['balance']:.2f}")

def deposit_money(account):
    try:
        #take input for amount and convert to float to handle decimal inputs
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            #add the amount to the total balance 
            account['balance'] += amount
            #print how much has been deposited and the updated balance
            print(f"${amount:.2f} has been deposited. Your new balance is: ${account['balance']:.2f}")
        else:
            #handle errors for when negative values are given
            print("Please enter a positive number")
    except ValueError:
        #handle inputs that are the wrong datatype such as strings
        print("Invalid input, try entering a number next time")

def withdraw_money(account):
    try:
        #take input for the amount to withdraw and convert to float to handle decimal values
        amount = float(input("Enter amount to withdraw: $"))
        if amount > 0:
            #check if the amount is less than the balance
            if amount <= account['balance']:
                #subract the amount from the balance
                account['balance'] -= amount
                #print the amount and the updated balance
                print(f"${amount:.2f} has been withdrawn. Your new balance is: ${account['balance']:.2f}")
            else:
                #handle inputs that are less than the balance
                print("Insufficient funds.")
        else:
            #handle inputs that are negative numbers
            print("Please enter a positive amount.")
    except ValueError:
        #handle inputs that are in the wrong datatype, such as strings
        print("Invalid input, try entering a number next time.")

def change_pin(account):
    try:
        #take input for the pin
        pin = int(input("Enter your new PIN (4 digits): "))
        #check if the pin is 4 digits
        if pin <= 9999 and pin >= 1000:
            #set the pin equal to the inputted pin
            account['pin'] = pin
            print("Your PIN has been updated")
        else:
            #handle inputs that are greater or less than 4 digits
            print("Invalid PIN, make sure it is 4 digits")
    except ValueError:
        #handle inputs that are in the wrong datatype, such as trings
        print("Invalid input, try entering a number next time")

def authenticate(account):
    try:
        #take input for the pin
        pin = int(input("Enter your PIN: "))
        #check if the inputted pin is equal to the account pin
        if pin == account['pin']:
            return True
        else:
            #return false if the wrong pin is entered
            print("Incorrect PIN, access denied.")
            return False
    except ValueError:
        print('Invalid input, please try entering a number next time')
        return False
    
if __name__ == '__main__':
    main()
