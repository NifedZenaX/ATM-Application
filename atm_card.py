class ATMCard:
    def __init__(self, defaultPIN, defaultBalance):
        self.defaultPIN = defaultPIN
        self.defaultBalance = defaultBalance
    
    def getPIN(self):
        return self.defaultPIN

    def getBalance(self):
        return self.getBalance