class Bank:        
    def __init__(self,branch):
        self.__branch = branch
        customer1 = Customer("John Smith")
        customer2 = Customer("Jane Doe")
        customer3 = Customer("Alice Johnson")
        print(f"Welcome to {branch} branch of the bank.")
        print("We have 3 customers: John Smith, Jane Doe, and Alice Johnson.")
        while(True):
            customerSelector = input("Select customer (1/2/3): (q for Quit Anytime) ").strip()
            if customerSelector == "1":
                print("You have selected John Smith.")
                print("Please enter password to continue.")                            
                if customer1.authenticate():
                    customer1.customer_menu()
                else:
                    print("Authentication failed for John Smith.")
            elif customerSelector == "2":
                print("You have selected Jane Doe.")
                print("Please enter password to continue.")
                if customer2.authenticate():
                    customer2.customer_menu()
                else:
                    print("Authentication failed for Jane Doe.")
            elif customerSelector == "3":
                print("You have selected Alice Johnson.")
                print("Please enter password to continue.")
                if customer3.authenticate():
                    customer3.customer_menu()
                else:
                    print("Authentication failed for Alice Johnson.")
            elif customerSelector.lower() == "q":
                print("Thank you for visiting. Goodbye!")
                break
            else:
                print("Invalid customer selection.")

class Customer:
    def __init__(self, name):        
        self.__name = name
        self.__password = "password123"  # Simple password for demonstration
        self.__savingsAccount = Account("Savings", self.get_name()+"'s Savings Account", 100)
        self.__loanAccount = Account("Loan", self.get_name()+"'s Loan Account", 100)

    def authenticate(self):
        entered_password = input(f"Enter password for {self.__name}: ")
        # in real applications we run sql query to check password from database
        # if it matches return true else false
        if entered_password == self.__password:
            print("Authentication successful.")
            return True
        else:
            print("Incorrect password.")
        return False

    def get_name(self):
        return self.__name

    def statement(self):
        print(f"Customer Name: {self.__name}")
        print("Account Statements:")
        self.__savingsAccount.show_balance()
        self.__loanAccount.show_balance()

    def customer_menu(self):

        print(f"Welcome {self.__name} to the banking system.")
        while(True):
            print("You have two accounts: Savings and Loan.")
            print(f"Savings Account Balance {self.__savingsAccount.get_balance()}")
            print(f"Loan Account Balance {self.__loanAccount.get_balance()}")
            accountSelector = input("Select (s for savings / l for loan) Or Select t for Transfer: (q for Quit Anytime) ").strip().lower()

            if accountSelector == "s":
                self.__savingsAccount.menu()
            elif accountSelector == "l":
                self.__loanAccount.menu()
            elif accountSelector == "t":
                amount = float(input("Enter amount to transfer: "))
                target_account = input("Enter target account (s/l): ").strip().lower()
                if target_account == "s":
                    self.__loanAccount.transfer(amount, self.__savingsAccount)
                elif target_account == "l":
                    self.__savingsAccount.transfer(amount, self.__loanAccount)
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

class AccessControl:
    def __init__(self):
        self.__username = "admin"
        self.__password = "neo"

    def menu(self):
        loopController = True
        while(loopController):
            print("Welcome to Banking System",self.__username)
            switchController = input("Select an option. (L – Log in as a customer.; A – Log in as the manager.; X – Exit.) ").strip().lower()
            if switchController == "l":
                # Log in as a customer
                break
            if switchController == "a":
                print("Manager access granted.")
                bestBankofSydney = Bank("Sydney's Best Bank")
                break
            if switchController == "x":
                loopController = False
                print("Exiting Banking System.")
                break

if __name__ == "__main__":
    access_control = AccessControl()
    access_control.menu()