import random

class Account:
    def __init__(self):
        self.account_number = random.randint(10000, 99999)
        self.balance = 0
        self.transactions = [] 
        print(f"Welcome! Your new account number is: {self.account_number}")

    def deposit(self):
        amount = self.get_positive_float_input("Enter amount to be deposited: ")
        self.balance += amount
        self.transactions.append((amount, 'Deposit'))
        print(f"\nAmount deposited: {amount}")
        self.display_balance()

    def withdraw(self):
        amount = self.get_positive_float_input("Enter amount to be withdrawn: ")
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append((amount, 'Withdrawal'))
            print(f"\nAmount withdrawn: {amount}")
        else:
            print("\nInsufficient balance.")
        self.display_balance()

    def display_balance(self):
        print(f"\nCurrent Balance: {self.balance}")

    def delete_account(self):
        self.__init__()
        print("Account deleted successfully.")

    def create_account(self):
        self.account_number = random.randint(10000, 99999)
        self.balance = 0
        self.transactions = [] 
        print(f"Account created successfully. Your new account number is: {self.account_number}")

    @staticmethod
    def get_positive_float_input(prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                return amount
            except ValueError as e:
                print(f"Invalid input: {e}")

    def choose_option(self):
        while True:
            print("\nPlease choose an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Display Balance")
            print("4. Delete Account")
            print("5. Create Account")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.display_balance()
            elif choice == '4':
                self.delete_account()
            elif choice == '5':
                self.create_account()
            elif choice == '6':
                print("Exiting program. Thank You & Goodbye! Have A Nice Day!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 6.")



account = Account()
account.choose_option()
