import pickle
from datetime import datetime

FILENAME = "customers.data"
DATE_FORMAT = "%d/%m/%Y - %H:%M:%S"

def get_current_time():
    return datetime.now().strftime(DATE_FORMAT)

def write_to_file(customers):
    try:
        with open(FILENAME, "wb") as file:
            pickle.dump(customers, file)
    except IOError as e:
        print(f"Error: Could not write to file {FILENAME}. {e}")

def read_from_file():
    try:
        with open(FILENAME, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    except (IOError, pickle.UnpicklingError) as e:
        print(f"Error: Could not read from file {FILENAME}. {e}")
        return []
class Account:

    def __init__(self, account_type, balance=0.0):
        self.type = account_type
        self.balance = float(balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount 
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"{self.type} account has ${self.balance:,.2f}"

class Customer:

    def __init__(self, name, savings_balance, loan_balance):
        self.name = name
        self.accounts = { 
            "Savings": Account("Savings", savings_balance),
            "Loan": Account("Loan", loan_balance)
        }

    def _read_amount(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount > 0:
                    return amount
                print("Amount must be positive.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def deposit(self):
        amount = self._read_amount("Amount to deposit: $")
        self.accounts["Savings"].deposit(amount)
        print("Deposit successful.")
        self.show()

    def withdraw(self):
        amount = self._read_amount("Amount to withdraw: $")
        if not self.accounts["Savings"].withdraw(amount):
            print("Withdrawal failed. Insufficient funds.")
        else:
            print("Withdrawal successful.")
        self.show()

    def transfer(self):
        amount = self._read_amount("Amount to transfer: $")
        if self.accounts["Savings"].withdraw(amount):
            self.accounts["Loan"].withdraw(amount) # Paying off loan decreases its balance
            print("Transfer successful.")
        else:
            print("Transfer failed. Insufficient funds in Savings account.")
        self.show()

    def show(self):
        print(f"\n{self.name} bank statement: {get_current_time()}")
        print(self.accounts["Savings"])
        print(self.accounts["Loan"])
    
    def __str__(self):
        savings_str = str(self.accounts["Savings"])
        loan_str = str(self.accounts["Loan"])
        return f"--> {savings_str} | {loan_str}"

    def use(self):
        menu_options = {
            'd': self.deposit,
            'w': self.withdraw,
            't': self.transfer,
            's': self.show,
        }
        
        while True:
            print(f"\n{self.name} banking menu: {get_current_time()}")
            choice = input("Customer menu (d/w/t/s/x): ").lower()
            if choice == 'x':
                print("Back to Bank menu")
                break
            action = menu_options.get(choice)
            if action:
                action()
            else:
                print("Invalid option. Please try again.")

class Bank:
    def __init__(self):
        self.customers = read_from_file()

    def _commit(self):
        write_to_file(self.customers)

    def _find_customer(self, name):
        for customer in self.customers:
            if customer.name.lower() == name.lower():
                return customer
        return None
    
    def _read_amount(self, prompt):
        while True:
            try:
                balance_str = input(prompt).replace('$', '').replace(',', '')
                balance = float(balance_str)
                if balance >= 0:
                    return balance
                print("Balance cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def add_customer(self):
        name = input("Enter Customer Name: ")
        if self._find_customer(name):
            print("Error: Customer already exists.")
            return

        savings = self._read_amount("Initial Savings balance: $")
        loan = self._read_amount("Initial Loan balance: $")
        
        new_customer = Customer(name, savings, loan)
        self.customers.append(new_customer)
        self._commit()
        print(f"Customer '{name}' added successfully.")

    def remove_customer(self):
        name = input("Enter Customer Name: ")
        customer = self._find_customer(name)
        if customer:
            self.customers.remove(customer)
            self._commit()
            print(f"Customer '{name}' removed successfully.")
        else:
            print("Customer does not exist.")
            
    def search_customer_statement(self):
        name = input("Enter Customer Name: ")
        customer = self._find_customer(name)
        if customer:
            print(customer)
        else:
            print("Customer does not exist.")

    def view_all_customers(self):
        if not self.customers:
            print("No customers in the system.")
            return
        for customer in self.customers:
            print(f"{customer.name}\n{customer}")

    def customer_login(self):
        name = input("Enter Customer Name: ")
        customer = self._find_customer(name)
        if customer:
            customer.use()
            self._commit()
        else:
            print("Customer does not exist.")

class Manager: 
    def __init__(self, bank):
        self.name = "John Smith"
        self.bank = bank

    def use(self):
        menu_options = {
            'a': self.bank.add_customer,
            'r': self.bank.remove_customer,
            's': self.bank.search_customer_statement,
            'v': self.bank.view_all_customers,
        }
        
        while True:
            print(f"\n{self.name} Manager menu: {get_current_time()}")
            choice = input("Customer menu (a/r/s/v/x): ").lower()
            if choice == 'x':
                print("Back to Bank menu")
                break
            action = menu_options.get(choice)
            if action:
                action()
            else:
                print("Invalid option. Please try again.")

class Login:
    def __init__(self):
        self.bank = Bank()
        self.manager = Manager(self.bank)

    def _help(self):
        print("\nMenu options")
        print("L = Login into customer menu")
        print("A = Login into Manager menu")
        print("X = exit")
        
    def main(self):
        menu_options = {
            'l': self.bank.customer_login,
            'a': self.manager.use,
        }
        self._help()
        
        while True:
            print(f"\nBank menu: {get_current_time()}")
            choice = input("Customer menu (L/A/X): ").lower()
            
            if choice == 'x':
                print("Done.")
                break
            
            action = menu_options.get(choice)
            if action:
                action()
            else:
                self._help()

if __name__ == "__main__":
    app = Login()
    app.main()