#from email.generator import Generator
import random
import csv
class PasswordGenerator:
    def __init__(self, passwordLength: int):
        self.passwordLength = passwordLength
        
    
    
    def Generator(self):
        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        symbols = "_!&"
        all = lower + upper + numbers + symbols
        length = self.passwordLength 
        password = " ".join(random.sample(all,length))
        print(password)
        return password 
    
class writeANDstorePassword(PasswordGenerator): 
    def __init__(self, NewPassword: str):
        self.NewPassword = NewPassword
    
       
    def savePassword(self):
        with open('savePassword.txt', 'w') as PasswordText:
         PasswordText.write(NewPassword)   
    
NewPassword = PasswordGenerator(8)
SavePassword = writeANDstorePassword(NewPassword)