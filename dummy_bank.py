# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 01:20:14 2020

@author: Oshi
"""

class dummybank_API:

    def __init__(self):  #assunimg 5 digit bank accoount number 
        self.my_dict = {12345:1234, 22222:2345}  #hardcoding the dictionary for testing 
        self.account_number = None
        self.pin = None 
        
    def enter_values(self,account_num,pin):  #input from bank database or staff 
        self.my_dict[account_num] = pin     #not implemented in current code
        
    def check_valid_account(self,account_num):
        if(account_num in self.my_dict):
            print("Accepted\n")
            return True
        else:
            print("Swipe card again/enter number again\n")
            return False
    
    def check_pin(self,account_num,pin):
        if(self.my_dict[account_num]== pin):
            print("Correct Pin\n")
            return True
        else:
            print("invalid Pin - Enter again\n")
            return False
        

        
        