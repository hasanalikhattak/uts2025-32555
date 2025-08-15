class Bank:        
    def __init__(self):        
        self.__balance = 0.0

    def get_balance(self):        
        return self.__balance
    @property
    def balance(self):
        return self.__balance
    
    def set_balance(self, amount):        
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount
        
    def show_balance(self): 
        print(f"Current balance: ${self.balance:.2f}")

    def deposit(self, amount=None):
        if amount is None:
            while True:
                try:
                    amount = float(input("Enter amount to deposit: $"))
                    if amount < 0:
                        print("Error: Deposit amount cannot be negative. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid number.")
        
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        
        self.set_balance(self.balance + amount)
        print(f"Successfully deposited ${amount:.2f}")
        self.show_balance()

    def withdraw(self, amount=None):
        if amount is None:
            while True:
                try:
                    amount = float(input("Enter amount to withdraw: $"))
                    if amount < 0:
                        print("Error: Withdrawal amount cannot be negative. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid number.")
        
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        
        if amount <= self.balance:
            self.set_balance(self.balance - amount)
            print(f"Successfully withdrew ${amount:.2f}")
        else:
            print(f"Error: Insufficient funds. Available balance: ${self.balance:.2f}")
        self.show_balance()        

    def main(self):        
        self.deposit()
        self.withdraw()

if __name__ == "__main__":
    bank = Bank()
    bank.main()