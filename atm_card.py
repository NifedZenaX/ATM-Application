class ATMCard:
    def __init__(self, defaultPIN, defaultBalance):
        self.defaultPIN = defaultPIN
        self.defaultBalance = defaultBalance
    
    def GetPIN(self):
        return self.defaultPIN

    def GetBalance(self):
        return self.getBalance