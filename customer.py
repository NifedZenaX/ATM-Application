from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance
    
    def GetCustID(self):
        return self.id
    
    def GetCustPin(self):
        return self.custPin

    def GetCustBalance(self):
        return self.custBalance
    
    def Withdraw(self, nominal):
        self.custBalance -= nominal

    def Deposit(self, nominal):
        self.custBalance += nominal