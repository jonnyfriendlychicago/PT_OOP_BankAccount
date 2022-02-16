
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
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
        #above newly added
        print(f"Accounted created.  Current balance is ${self.balance} with a current interest rate of {self.int_rate}.")
        # return None
    
    def display_account_info (self):
        # self.display_account_info = print(f"Balance: ${self.balance}")
        #11pm here... just realized how funky above line is.  not sure why ever wrote it that way.  below is attempted fix
        print(f"Balance: ${self.balance}")
        # return self    
    
    def deposit (self, amount): 
        self.balance += amount
        # print(f"Deposit accepted: ${amount}.  New balance: ${self.balance}.")
        print(f"Deposit accepted: ${amount}.")
        # print(f"Balance: ${self.balance}")
        self.display_account_info()
        #***********************
        # above line "self.display_account_info()" works here... but never works again in any of the other methods that try to use it.  WHY????
        return self

    def withdraw (self, amount):
        if self.balance < amount:
            self.old_balance = self.balance
            self.balance -= 5
            print(f"Insufficient funds.  You tried to withdraw ${amount} but your balance was only ${self.old_balance}.  For even attempting that, we just charged you a completely unjustifiable $5 fee... and you cant do jack about it.")
            self.display_account_info()
            # print(f"Balance: ${self.balance}")
        else: 
            self.balance -= amount
            print(f"Withdrawl completed: ${amount} ")
            self.display_account_info()
            # print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.int_added = self.balance * self.int_rate
            self.balance =  self.int_added + self.balance
            print(f"Interest yield added to account in the amount: ${self.int_added}.")
            self.display_account_info()
            # print(f"Balance: ${self.balance}")
        else: 
            print(f"No interest yield payment: account balance less than or equal to zero.")
            self.display_account_info()
            # print(f"Balance: ${self.balance}")
        return self

    @classmethod
    def print_all_accounts(cls):
        print("List of all account balances:::::::::::::::::::")
        for x in cls.accounts:
            x.display_account_info()
    """
    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        print(sum)
    """
acct1 = BankAccount(0.02,100)
acct2 = BankAccount(0.02,1000)

acct1.deposit(1).deposit(2).deposit(3).withdraw(4).yield_interest()

acct2.deposit(2).deposit(200).withdraw(20).withdraw(40).withdraw(60).withdraw(80).yield_interest()

BankAccount.print_all_accounts()

# cls.all_balances ()

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