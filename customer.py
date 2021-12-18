import atm_card

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