from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.__balance = 0.0 # Private attribute

    # Getter and setter methods
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance

    # Abstract methods
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Bank):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.interest_rate = 0.05

    # Abstract method so we need to implement it
    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)
    
    # Abstract method so we need to implement it
    def withdraw(self, amount):
        # Check if the balance is sufficient
        if self.get_balance() >= amount: 
            # Deduct withdrawal amount from balance
            self.set_balance(self.get_balance() - amount)
        else:
            print("Insufficient balance")

    # Class specific method
    def calculate_interest(self):
        return self.get_balance() * self.interest_rate
    
class CurrentAccount(Bank):
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.overdraft_limit = 1000.0

    # Abstract method so we need to implement it
    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)

    # Abstract method so we need to implement it
    def withdraw(self, amount):
        if amount > self.get_balance() + self.overdraft_limit:
            print ('Insufficient funds')
        else:
            self.set_balance(self.get_balance() - amount)
            return self.get_balance()

c = CurrentAccount('Kim')
c.set_balance(1000) # Starting balance - 1000 
c.withdraw(2000) # Insufficient funds
print(c.get_balance()) # -1000
c.deposit(500) # Deposit 500
print(c.get_balance()) # -500

s = SavingsAccount('Kim')
s.set_balance(5000) # Starting balance - 1000
s.withdraw(2000) # Withdraw 2000
print(s.get_balance()) # 3000
s.deposit(500) # Deposit 500
print(s.get_balance()) # 3500
print(s.calculate_interest()) # 175.0