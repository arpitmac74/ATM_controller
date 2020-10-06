# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 00:34:38 2020

@author: Oshi
"""
import numpy as np 
from ATM_class import ATM
from dummy_bank import dummybank_API
import random

# for testing please use 
# card number as 12345
# pin as 1234
# balance is 100 units by default for testing 


def main():
    dummy_bank = dummybank_API()
    while(1):
        account = ATM(int(input("Insert Card: ")))  #taking any 10 digit number as an input since card number 
        if(dummy_bank.check_valid_account(account.getacc_id())):
            while True:
                #enter pin and check 
                account.pin = int(input("\nEnter account pin: "))
                
                #loop till correct pin is entered
                while account.pin < 1000 or account.pin > 9999:
                    account.pin = int(input("\nInvalid Id.. Re-enter: "))
                
                if(dummy_bank.check_pin(account.getacc_id(),account.get_pin())):
                    #session begins
                    while True:
                        #menu
                        print("\n 1 - Check Balance \n 2 - Withdraw \n 3 - Deposit \n 4 - Exit\n ")
                        
                        sel = int(input("\nEnter your selection: "))
                        
                        #operations
                        #check balance 
                        if sel == 1:
                            print("your balance is")
                            account.print_bal()
                        #withdraw
                        elif(sel == 2):
                            amt = int(input("\nEnter amount to withdraw: "))
                            if(amt < account.get_balance()):
                                account.withdraw(amt)
                                print("\nUpdated Balance: "+ str(account.get_balance()) +"\n")
                        #deposit
                        elif(sel == 3):
                            amt = int(input("\nEnter amount to deposit: "))
                            account.deposit(amt)
                            print("\nNew Balance: " + str(account.get_balance()) + "\n")
                        elif(sel == 4):
                             print("Transaction is now complete.")
                             print("Transaction number: ", random.randint(10000, 1000000))
                             print("Have a great day")
                             exit()
                        else:
                            print("That's an invalid choice-\n Enter Again---")
                            continue
                            
                                
                            
                            
                else:
                    continue
                    #check for pin wirh account number 
        else:
            continue
            
        
                
                    
                
                
                
                
            
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()