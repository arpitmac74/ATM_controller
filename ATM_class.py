
class ATM:
    #contruct an ATM object 
    def __init__(self, acc_id):
        self.acc_id = acc_id 
        self.balance = 100
        self.pin = None
    
    def getacc_id(self):
        return self.acc_id
    
    def get_pin(self):
        return self.pin
    
    def get_balance(self):
        return self.balance
    
    def print_bal(self):
        print(self.balance)
    
    def print_num(self):
        print(self.acc_id)
    
    def print_pin(self):
        print(self.pin)
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount
        


        
    