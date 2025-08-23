class Bank:        
    def __init__(self):        
        self.__balance = 0.0

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if(self.__balance <= 1000):
            self.__balance = amount
            print("Balance updated successfully.")
        else: 
            print("Error: Balance cannot exceed $1000.")

    def show_balance(self): 
        print(f"Current balance: ${self.__balance:.2f}")
    
    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount cannot be negative.")
            return
        self.__balance += amount
        print(f"Successfully deposited ${amount:.2f}.")
        self.show_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: You have to enter a positive number")
            return

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount:.2f}.")
        else:
            print("Error: Insufficient funds.")
            return

    def main(self):
        loopController = True      
        while(loopController): 
            switchController = input("What do we want to do Today (d/w/s/q) ").strip().lower()
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

if __name__ == "__main__":
    bank = Bank()
    bank.main()