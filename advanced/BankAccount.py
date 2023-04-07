
class Account: #Main Account

    def __init__(self, ac_number, inicial_deposit):
        self.ac_number = ac_number
        self.balance = inicial_deposit
        print('########     Account     ##########')
    
    def __str__(self):
        return f'${self.balance:.2f}'
    
    def deposit(self,deposit):
        self.balance += deposit

    def withdraw(self,withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
        else:
            return 'Funds Unavailable'

class Checking(Account):

    def __init__(self, ac_number, inicial_deposit):
        Account.__init__(self, ac_number, inicial_deposit)
        print('----- This is Checking Account ----')

    def __str__(self):
        return f'Checking Account #{self.ac_number}\nBalance: {Account.__str__(self)}'

class Savings(Account):

    def __init__(self,ac_number, inicial_deposit):
        super().__init__(ac_number, inicial_deposit) ## must define which argumentt

    
    def __str__(self):
        return f'Savings Account #{self.ac_number}\nBalance: {Account.__str__(self)}'

class Business(Account):
    def __init__(self, ac_number, inicial_deposit):
        super().__init__(ac_number, inicial_deposit)
    
    def __str__(self):
        return f'Business Account #{self.ac_number}\n  Balance: {Account.__str__(self)}'

class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN
        self.accts = {'C':[],'S':[],'B':[]} #dictonary for objects

    def __str__(self):
        return self.name
        
    def open_checking(self, ac_number, inicial_deposit):
        self.accts['C'].append(Checking(ac_number, inicial_deposit))
    
    def open_savings(self, ac_number, inicial_deposit):
        self.accts['S'].append(Savings(ac_number, inicial_deposit))
        
    def open_business(self, ac_number, inicial_deposit):
        self.accts['B'].append(Business(ac_number, inicial_deposit))
        
    def get_total_deposits(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f'Combined Deposits: ${total:.2f}')


bob = Customer('Bob',1)
print('\n')
bob.open_checking(1001, 500)
bob.get_total_deposits()
print('----------------------')
bob.open_savings(5001, 440)
bob.get_total_deposits()
print('----------------------')

nancy = Customer('Nancy',2)
print('\n')
nancy.open_business(9001, 89000)
nancy.get_total_deposits()