from bank import BankAccount

def main():
    
    account = BankAccount("Lukas", 1000.0)
    print(f"Account created for {account.account_holder} with an initial balance of ${account.get_balance():.2f}.")

    account.deposit(500)
    account.withdraw(200)
    account.withdraw(1500)  
    account.deposit(-100)   

    final_balance = account.get_balance()
    print(f"Final balance: ${final_balance:.2f}")

if __name__ == "__main__":
    main()
