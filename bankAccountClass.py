class User:
    bank_name = "First National Dojo"
    all_accounts = []

    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):
    # have this method decrease the user's balance by the amount specified
        self.account_balance -= amount
        return self

    def display_user_balance(self): 
        self.balance_display = print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    #have this method print the user's name and account balance to the terminal, e.g. "User: Guido van Rossum, Balance: $150

    def transfer_money(self, other_user, amount): 
        self.account_balance -= amount
        other_user.account_balance += amount
        self.balance_display = print(f"User: {self.name}, Balance: ${self.account_balance}")
        other_user.balance_display = print(f"User: {other_user.name}, Balance: ${other_user.account_balance}")
        return self
    #have this method decrease the user's balance by the amount and add that amount to other other_user's balance

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(cls.bank_name)
    
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum


a1 = User("Lucky Day", "lucky@3amigos.com")
a2 = User("Dusty Bottoms", "dusty@3amigos.com")
a3 = User("Ned Nederlander", "ned@3amigos.com")

print(a1.name)
print(a2.name)
print(a3.name)

# a1.make_deposit(33)
# a1.make_deposit(33)
# a1.make_deposit(33)
# a1.make_withdrawal(20)
# a1.display_user_balance()

a1.make_deposit(33).make_deposit(33).make_deposit(33).make_withdrawal(20).display_user_balance()

# a2.make_deposit(50)
# a2.make_deposit(50)
# a2.make_withdrawal(25)
# a2.make_withdrawal(25)
# a2.display_user_balance()

a2.make_deposit(50).make_deposit(50).make_withdrawal(25).make_withdrawal(25).display_user_balance()

# a3.make_deposit(79)
# a3.make_withdrawal(40)
# a3.make_withdrawal(20)
# a3.make_withdrawal(20)
# a3.display_user_balance() 

a3.make_deposit(79).make_withdrawal(40).make_withdrawal(20).make_withdrawal(20).display_user_balance()

a1.transfer_money(a3, 19)

class BankAccount:
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # self.int_rate = 0.01
        # self.balance = 0
        print(f"Accounted created.  Current balance is ${self.balance} with a current interest rate of {self.int_rate}.")
        # return self
    
    def deposit (self, amount): 
        self.balance += amount
        print(f"Deposit accepted: ${amount}.  New balance: ${self.balance}.")

    # def withdraw (self, amount):
    #     if self.balance < self.amount:
    #         self.balance -= 5
    #         print("Insufficient funds: now we just charged you $5 fee... and you cant do shit about it.  Thank you for voting Republican!  We could not do this without their protection.")
    #     else: 
    #         self.balance -= amount
    #         print(f"withdrawl of {amount} completed.  We will find another way to steal your money next time.")
    #     return self

    # def display_account_info (self):
    #     self.display_account_info = print(f"Balance: ${self.balance}")
    #     return self

    # def yield_interest(self):
    #     if self.balance > 0:
    #         self.balance = self.balance * self.int_rate + self.balance
    #         print(f"interest yield added to account.  New Account Balance: {self.balance}.")
    #     else: 
    #         print(f"No interest yield payment: account balance less than or equal to zero.")
    #     return self

acct1 = BankAccount(0.02,100)
# acct2 = BankAccount("500", "0.03")

acct1.deposit(100)
# .deposit("100").deposit("100").withdraw("50").yield_interest


# below from lesson example 
"""
def with_draw (self, amount):
    if BankAccount.can_withdraw(self.balance, amount):
        self.balance -= amount
    else:
        print("Insufficient Funds")
    return self

@staticmethod
def can_withdraw(balance, amount):
    if (balance - amount) < 0:
        return False
    else: 
        return True
"""