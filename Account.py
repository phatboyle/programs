class BankAccount:
    def __init__(self):
        self.AccountNumber = 0
        self.balance = 5
    def __str__(self):
        print self.balance
    def deposit(self,amount):
        self.balance = self.balance + amount
    def withdrawal(self,amount):
        self.balance = self.balance - amount
    def showBalance(self):
        print self.balance

class InterestAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)
        self.interestRate=.1
    def addInterest(self):
        self.balance = self.balance + self.balance+self.interestRate*self.balance
        print self.balance
        
    


        
account = BankAccount()
account.deposit
account.showBalance()

i = InterestAccount()
i.addInterest()









