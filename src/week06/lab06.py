class Bank:        
    def __init__(self,branch):
        self.__branch = branch
        customer1 = Customer("John Smith")
        customer2 = Customer("Jane Doe")
        print(f"Welcome to {branch} branch of the bank.")
        while(True):
            customerSelector = input("Select customer (1 for John Smith / 2 for Jane Doe): (q for Quit Anytime) ").strip()
            if customerSelector == "1":
                customer1.customer_menu()
            elif customerSelector == "2":
                customer2.customer_menu()
            elif customerSelector.lower() == "q":
                print("Thank you for visiting. Goodbye!")
                break
            else:
                print("Invalid customer selection.")

class Customer:
    def __init__(self, name):        
        self.__name = name

    def get_name(self):
        return self.__name

    def customer_menu(self):
        savingsAccount = Account("Savings", self.get_name()+"'s Savings Account", 100)
        loanAccount = Account("Loan", self.get_name()+"'s Loan Account", 100)
        print(f"Welcome {self.__name} to the banking system.")
        while(True):
            print("You have two accounts: Savings and Loan.")
            print(f"Savings Account Balance {savingsAccount.get_balance()}")
            print(f"Loan Account Balance {loanAccount.get_balance()}")
            accountSelector = input("Select (s for savings / l for loan) Or Select t for Transfer: (q for Quit Anytime) ").strip().lower()

            if accountSelector == "s":
                savingsAccount.menu()
            elif accountSelector == "l":
                loanAccount.menu()
            elif accountSelector == "t":
                amount = float(input("Enter amount to transfer: "))
                target_account = input("Enter target account (s/l): ").strip().lower()
                if target_account == "s":
                    loanAccount.transfer(amount, savingsAccount)
                elif target_account == "l":
                    savingsAccount.transfer(amount, loanAccount)
            elif accountSelector == "q":
                print("Exiting transfer menu.")
                break

class Account:
    def transfer(self, amount, target_account):
        if amount >= 0:
            self.withdraw(amount)
            target_account.deposit(amount)
        else:
            print("Error: Transfer amount must be positive.")
            return

    def menu(self):
        loopController = True
        while(loopController):
            print("Welcome to account",self.__title)
            switchController = input("What do we want to do Today in (d/w/s/q) ").strip().lower()
            if switchController == "d":
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            if switchController == "w":
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            if switchController == "s":
                self.show_balance()
            if switchController == "q":
                answer = input("Do you want to continue? (y/n): ").strip().lower()
                if(answer == "n"):
                    loopController = False
                    print("Thank you for using the bank system. Goodbye!")
        
    def __init__(self, type, title, balance):        
        self.__balance = balance
        self.__type = type
        self.__title = title
    
    def get_balance(self):
            return self.__balance
    
    def set_balance(self, amount):
        if(self.__balance <= 1000):
            self.__balance = amount
            print("Balance updated successfully.")
        else: 
            print("Error: Balance cannot exceed $1000.")

    def show_balance(self): 
        print(f"Current balance: ${self.__balance:.2f} in {self.__title}")
    
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount cannot be negative.")
            return
        self.__balance += amount
        print(f"Successfully deposited ${amount:.2f}. in {self.__title}")
        self.show_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Error: {self.__title} You have to enter a positive number")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. in {self.__title}")
        else:
            print("Error: Insufficient funds.")
            return

if __name__ == "__main__":
   bestBankofSydney = Bank("Sydney's Best Bank")